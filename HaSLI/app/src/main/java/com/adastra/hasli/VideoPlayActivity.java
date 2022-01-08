package com.adastra.hasli;

import android.content.Intent;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.VideoView;

import androidx.appcompat.app.AppCompatActivity;

public class VideoPlayActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video_alpha);

        ImageButton backButton = findViewById(R.id.video_back_button);
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });


        Bundle inputs = getIntent().getExtras();
        int file = inputs.getInt("file");
        char alpha = inputs.getChar("alpha");
        /*
        if (inputs != null) {
            String file = inputs.getString("file");
            char alpha = inputs.getChar("alpha");
            //The key argument here must match that used in the other activity
        }
         */

        TextView title_alpha = findViewById(R.id.video_title);
        title_alpha.setText("Letter " + alpha);

        // VideoView videoAlpha = findViewById(R.id.video_view);
        // String path = "android.resource://" + getPackageName() + "/" + R.raw.b;
        VideoView videoAlpha = findViewById(R.id.video_view);
        String path = "android.resource://" + getPackageName() + "/" + file;
        Uri uri = Uri.parse(path);
        videoAlpha.setVideoURI(uri);
        videoAlpha.requestFocus();
        videoAlpha.start();

        videoAlpha.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
            @Override
            public void onPrepared(MediaPlayer mp) {
                mp.setLooping(true);
            }
        });

    }
}
