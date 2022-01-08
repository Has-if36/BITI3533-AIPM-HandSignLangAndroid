// Copyright 2021 The MediaPipe Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package com.adastra.hasli;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.exifinterface.media.ExifInterface;

import com.google.mediapipe.formats.proto.ClassificationProto;
import com.google.mediapipe.formats.proto.LandmarkProto;
import com.google.mediapipe.formats.proto.LandmarkProto.NormalizedLandmark;
import com.google.mediapipe.solutioncore.CameraInput;
import com.google.mediapipe.solutioncore.SolutionGlSurfaceView;
import com.google.mediapipe.solutioncore.VideoInput;
import com.google.mediapipe.solutions.hands.HandLandmark;
import com.google.mediapipe.solutions.hands.Hands;
import com.google.mediapipe.solutions.hands.HandsOptions;
import com.google.mediapipe.solutions.hands.HandsResult;

import java.io.IOException;
import java.io.InputStream;

/** Main activity of MediaPipe Hands app. */
public class CameraActivity extends AppCompatActivity {
    private static final String TAG = "CameraActivity";
    private static String alphaArray = "";

    private Hands hands;
    // Run the pipeline and the model inference on GPU or CPU.
    private static final boolean RUN_ON_GPU = true;

    private enum InputSource {
        UNKNOWN,
        //IMAGE,
        VIDEO,
        CAMERA,
    }
    private InputSource inputSource = InputSource.UNKNOWN;

    // Video demo UI and video loader components.
    private VideoInput videoInput;
    private ActivityResultLauncher<Intent> videoGetter;
    // Live camera demo UI and camera components.
    private CameraInput cameraInput;
    private static CameraInput.CameraFacing cameraType = CameraInput.CameraFacing.FRONT;

    //FPS
    private static long startTimeFPS = 0;
    private static long startTimeDetect = 0;

    private SolutionGlSurfaceView<HandsResult> glSurfaceView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        cameraType = CameraInput.CameraFacing.FRONT;
        setupLiveDemoUiComponents();

        TextView sentView = findViewById(R.id.cam_text_word);

        ImageButton backButton = findViewById(R.id.cam_back_button);
        ImageButton camButton = findViewById(R.id.cam_switch_camera);
        ImageButton guideButton = findViewById(R.id.cam_hand_guide);
        Button spaceBtn = findViewById(R.id.cam_space_btn);
        Button takeBtn = findViewById(R.id.cam_take_btn);
        Button clearBtn = findViewById(R.id.cam_clear_btn);

        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        camButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (cameraType == CameraInput.CameraFacing.FRONT)
                    cameraType = CameraInput.CameraFacing.BACK;
                else if (cameraType == CameraInput.CameraFacing.BACK)
                    cameraType = CameraInput.CameraFacing.FRONT;
                // setupLiveDemoUiComponents();
                inputSource = InputSource.UNKNOWN;
                CameraActivity.this.setupLiveDemoUiComponents();
            }
        });
        guideButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), HandSignGuideActivity.class);
                startActivity(intent);
            }
        });
        spaceBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                alphaArray += ' ';
                sentView.setText(alphaArray);
            }
        });
        takeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView alphabet = findViewById(R.id.cam_text_alphabet);
                alphaArray += String.valueOf(alphabet.getText());

                sentView.setText(alphaArray);
            }
        });
        clearBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                alphaArray = "";
                sentView.setText(alphaArray);
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (inputSource == InputSource.CAMERA) {
            // Restarts the camera and the opengl surface rendering.
            cameraInput = new CameraInput(this);
            cameraInput.setNewFrameListener(textureFrame -> hands.send(textureFrame));
            glSurfaceView.post(this::startCamera);
            glSurfaceView.setVisibility(View.VISIBLE);
        } else if (inputSource == InputSource.VIDEO) {
            videoInput.resume();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (inputSource == InputSource.CAMERA) {
            glSurfaceView.setVisibility(View.GONE);
            cameraInput.close();
        } else if (inputSource == InputSource.VIDEO) {
            videoInput.pause();
        }
    }

    private Bitmap rotateBitmap(Bitmap inputBitmap, InputStream imageData) throws IOException {
        int orientation =
                new ExifInterface(imageData)
                        .getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL);
        if (orientation == ExifInterface.ORIENTATION_NORMAL) {
            return inputBitmap;
        }
        Matrix matrix = new Matrix();
        switch (orientation) {
            case ExifInterface.ORIENTATION_ROTATE_90:
                matrix.postRotate(90);
                break;
            case ExifInterface.ORIENTATION_ROTATE_180:
                matrix.postRotate(180);
                break;
            case ExifInterface.ORIENTATION_ROTATE_270:
                matrix.postRotate(270);
                break;
            default:
                matrix.postRotate(0);
        }
        return Bitmap.createBitmap(
                inputBitmap, 0, 0, inputBitmap.getWidth(), inputBitmap.getHeight(), matrix, true);
    }

    /** Sets up the UI components for the live demo with camera input. */
    private void setupLiveDemoUiComponents() {
        if (inputSource == InputSource.CAMERA) {
            return;
        }
        stopCurrentPipeline();
        setupStreamingModePipeline(InputSource.CAMERA);

        //Button startCameraButton = findViewById(R.id.button_start_camera);
        //startCameraButton.setOnClickListener(
        //        v -> {
        //            if (inputSource == InputSource.CAMERA) {
        //                return;
        //            }
        //            stopCurrentPipeline();
        //            setupStreamingModePipeline(InputSource.CAMERA);
        //        });
    }

    /** Sets up core workflow for streaming mode. */
    private void setupStreamingModePipeline(InputSource inputSource) {
        this.inputSource = inputSource;
        startTimeFPS = System.currentTimeMillis();
        startTimeDetect = System.currentTimeMillis();

        // Initializes a new MediaPipe Hands solution instance in the streaming mode.
        hands =
                new Hands(
                        this,
                        HandsOptions.builder()
                                .setStaticImageMode(false)
                                .setMaxNumHands(1)
                                .setRunOnGpu(RUN_ON_GPU)
                                .build());

        hands.setErrorListener((message, e) -> Log.e(TAG, "MediaPipe Hands error:" + message));

        if (inputSource == InputSource.CAMERA) {
            cameraInput = new CameraInput(this);
            cameraInput.setNewFrameListener(textureFrame -> hands.send(textureFrame));
        } else if (inputSource == InputSource.VIDEO) {
            videoInput = new VideoInput(this);
            videoInput.setNewFrameListener(textureFrame -> hands.send(textureFrame));
        }

        // Initializes a new Gl surface view with a user-defined HandsResultGlRenderer.
        glSurfaceView =
                new SolutionGlSurfaceView<>(this, hands.getGlContext(), hands.getGlMajorVersion());
        glSurfaceView.setSolutionResultRenderer(new HandsResultGlRenderer());
        glSurfaceView.setRenderInputImage(true);

        hands.setResultListener(
                handsResult -> {
                    //logWristLandmark(handsResult, false); //showPixelValues
                    if (System.currentTimeMillis() - startTimeDetect > 300) {
                        //Log.i("HandSign", "READING");
                        startTimeDetect = System.currentTimeMillis();
                        HandSign hs = new HandSign(this);
                        hs.read(handsResult);
                    }
                    glSurfaceView.setRenderData(handsResult);
                    glSurfaceView.requestRender();

                    long endTimeFPS = System.currentTimeMillis();
                    long fps = Math.round(1/((double)(endTimeFPS - startTimeFPS)/1000));
                    startTimeFPS = endTimeFPS;
                    Log.i("FPS", String.format("%d", fps));
                    //hs.setFPS((int) fps);

                    int disp_fps;
                    if (fps > 999)
                        disp_fps = 999;
                    else
                        disp_fps = (int) fps;

                    this.runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            TextView textFPS = (TextView) findViewById(R.id.cam_text_fps);
                            textFPS.setText(String.valueOf(disp_fps));
                        }
                    });
                });

        // The runnable to start camera after the gl surface view is attached.
        // For video input source, videoInput.start() will be called when the video uri is available.
        if (inputSource == InputSource.CAMERA) {
            glSurfaceView.post(this::startCamera);
        }

        // Updates the preview layout.
        FrameLayout frameLayout = findViewById(R.id.preview_display_layout);
        frameLayout.removeAllViewsInLayout();
        frameLayout.addView(glSurfaceView); // glSurfaceView
        glSurfaceView.setVisibility(View.VISIBLE);
        frameLayout.requestLayout();
    }

    private void startCamera() {
        cameraInput.start(
                this,
                hands.getGlContext(),
                cameraType,
                glSurfaceView.getWidth(),
                glSurfaceView.getHeight());
    }

    private void stopCurrentPipeline() {
        if (cameraInput != null) {
            cameraInput.setNewFrameListener(null);
            cameraInput.close();
        }
        if (videoInput != null) {
            videoInput.setNewFrameListener(null);
            videoInput.close();
        }
        if (glSurfaceView != null) {
            glSurfaceView.setVisibility(View.GONE);
        }
        if (hands != null) {
            hands.close();
        }
    }

    private void logWristLandmark(HandsResult result, boolean showPixelValues) {
        if (result.multiHandLandmarks().isEmpty()) {
            return;
        }
        NormalizedLandmark wristLandmark =
                result.multiHandLandmarks().get(0).getLandmarkList().get(HandLandmark.WRIST);
        // For Bitmaps, show the pixel values. For texture inputs, show the normalized coordinates.
        if (showPixelValues) {
            int width = result.inputBitmap().getWidth();
            int height = result.inputBitmap().getHeight();
            Log.i(
                    TAG,
                    String.format(
                            "MediaPipe Hand wrist coordinates (pixel values): x=%f, y=%f",
                            wristLandmark.getX() * width, wristLandmark.getY() * height));
        } else {
            Log.i(
                    TAG,
                    String.format(
                            "MediaPipe Hand wrist normalized coordinates (value range: [0, 1]): x=%f, y=%f",
                            wristLandmark.getX(), wristLandmark.getY()));
        }
        if (result.multiHandWorldLandmarks().isEmpty()) {
            return;
        }
        LandmarkProto.Landmark wristWorldLandmark =
                result.multiHandWorldLandmarks().get(0).getLandmarkList().get(HandLandmark.WRIST);
        Log.i(
                TAG,
                String.format(
                        "MediaPipe Hand wrist world coordinates (in meters with the origin at the hand's"
                                + " approximate geometric center): x=%f m, y=%f m, z=%f m",
                        wristWorldLandmark.getX(), wristWorldLandmark.getY(), wristWorldLandmark.getZ()));
    }

  /*
  private void logWristLandmark(HandsResult result, boolean showPixelValues) {
    for (int j=0; j<20; j++) {
      NormalizedLandmark wristLandmark = Hands.getHandLandmark(result, 0, j);
      int width = result.inputBitmap().getWidth();
      int height = result.inputBitmap().getHeight();
      Log.i(
              TAG,
              String.format(
                      "Point %d: x=%f, y=%f",
                      j, wristLandmark.getX() * width, wristLandmark.getY() * height));

    // For Bitmaps, show the pixel values. For texture inputs, show the normalized coordinates.
    //
    //  if (showPixelValues) {
    //    int width = result.inputBitmap().getWidth();
    //    int height = result.inputBitmap().getHeight();
    //    Log.i(
    //            TAG,
    //            String.format(
    //                    "MediaPipe Hand wrist coordinates (pixel values): x=%f, y=%f",
    //                    wristLandmark.getX() * width, wristLandmark.getY() * height));
    //  } else {
    //    Log.i(
    //            TAG,
    //            String.format(
    //                    "MediaPipe Hand wrist normalized coordinates (value range: [0, 1]): x=%f, y=%f",
    //                    wristLandmark.getX(), wristLandmark.getY()));
    //  }
    //}
    }
  }
   */
}
