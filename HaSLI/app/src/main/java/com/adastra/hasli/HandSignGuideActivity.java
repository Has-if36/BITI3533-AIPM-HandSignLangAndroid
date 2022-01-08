package com.adastra.hasli;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageButton;

import androidx.appcompat.app.AppCompatActivity;

public class HandSignGuideActivity extends AppCompatActivity implements View.OnClickListener {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hand_sign);

        ImageButton backButton = findViewById(R.id.guide_back_button);
        backButton.setOnClickListener(this);

        ImageButton aButton = findViewById(R.id.a_button);
        ImageButton bButton = findViewById(R.id.b_button);
        ImageButton cButton = findViewById(R.id.c_button);
        ImageButton dButton = findViewById(R.id.d_button);
        ImageButton eButton = findViewById(R.id.e_button);
        ImageButton fButton = findViewById(R.id.f_button);
        ImageButton gButton = findViewById(R.id.g_button);
        ImageButton hButton = findViewById(R.id.h_button);
        ImageButton iButton = findViewById(R.id.i_button);
        ImageButton jButton = findViewById(R.id.j_button);
        ImageButton kButton = findViewById(R.id.k_button);
        ImageButton lButton = findViewById(R.id.l_button);
        ImageButton mButton = findViewById(R.id.m_button);
        ImageButton nButton = findViewById(R.id.n_button);
        ImageButton oButton = findViewById(R.id.o_button);
        ImageButton pButton = findViewById(R.id.p_button);
        ImageButton qButton = findViewById(R.id.q_button);
        ImageButton rButton = findViewById(R.id.r_button);
        ImageButton sButton = findViewById(R.id.s_button);
        ImageButton tButton = findViewById(R.id.t_button);
        ImageButton uButton = findViewById(R.id.u_button);
        ImageButton vButton = findViewById(R.id.v_button);
        ImageButton wButton = findViewById(R.id.w_button);
        ImageButton xButton = findViewById(R.id.x_button);
        ImageButton yButton = findViewById(R.id.y_button);
        ImageButton zButton = findViewById(R.id.z_button);
        aButton.setOnClickListener(this);
        bButton.setOnClickListener(this);
        cButton.setOnClickListener(this);
        dButton.setOnClickListener(this);
        eButton.setOnClickListener(this);
        fButton.setOnClickListener(this);
        gButton.setOnClickListener(this);
        hButton.setOnClickListener(this);
        iButton.setOnClickListener(this);
        jButton.setOnClickListener(this);
        kButton.setOnClickListener(this);
        lButton.setOnClickListener(this);
        mButton.setOnClickListener(this);
        nButton.setOnClickListener(this);
        oButton.setOnClickListener(this);
        pButton.setOnClickListener(this);
        qButton.setOnClickListener(this);
        rButton.setOnClickListener(this);
        sButton.setOnClickListener(this);
        tButton.setOnClickListener(this);
        uButton.setOnClickListener(this);
        vButton.setOnClickListener(this);
        wButton.setOnClickListener(this);
        xButton.setOnClickListener(this);
        yButton.setOnClickListener(this);
        zButton.setOnClickListener(this);

        /*
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
         */
    }

    @Override
    public void onClick(View v) {
        Intent intent;

        switch (v.getId()) {
            case R.id.guide_back_button:
                finish();
                break;
            case R.id.a_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.a);
                intent.putExtra("alpha", 'A');
                startActivity(intent);
                break;
            case R.id.b_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.b);
                intent.putExtra("alpha", 'B');
                startActivity(intent);
                break;
            case R.id.c_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.c);
                intent.putExtra("alpha", 'C');
                startActivity(intent);
                break;
            case R.id.d_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.d);
                intent.putExtra("alpha", 'D');
                startActivity(intent);
                break;
            case R.id.e_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.e);
                intent.putExtra("alpha", 'E');
                startActivity(intent);
                break;
            case R.id.f_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.f);
                intent.putExtra("alpha", 'F');
                startActivity(intent);
                break;
            case R.id.g_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.g);
                intent.putExtra("alpha", 'G');
                startActivity(intent);
                break;
            case R.id.h_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.h);
                intent.putExtra("alpha", 'H');
                startActivity(intent);
                break;
            case R.id.i_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.i);
                intent.putExtra("alpha", 'I');
                startActivity(intent);
                break;
            case R.id.j_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.j);
                intent.putExtra("alpha", 'J');
                startActivity(intent);
                break;
            case R.id.k_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.k);
                intent.putExtra("alpha", 'K');
                startActivity(intent);
                break;
            case R.id.l_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.l);
                intent.putExtra("alpha", 'L');
                startActivity(intent);
                break;
            case R.id.m_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.m);
                intent.putExtra("alpha", 'M');
                startActivity(intent);
                break;
            case R.id.n_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.n);
                intent.putExtra("alpha", 'N');
                startActivity(intent);
                break;
            case R.id.o_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.o);
                intent.putExtra("alpha", 'O');
                startActivity(intent);
                break;
            case R.id.p_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.p);
                intent.putExtra("alpha", 'P');
                startActivity(intent);
                break;
            case R.id.q_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.q);
                intent.putExtra("alpha", 'Q');
                startActivity(intent);
                break;
            case R.id.r_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.r);
                intent.putExtra("alpha", 'R');
                startActivity(intent);
                break;
            case R.id.s_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.s);
                intent.putExtra("alpha", 'S');
                startActivity(intent);
                break;
            case R.id.t_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.t);
                intent.putExtra("alpha", 'T');
                startActivity(intent);
                break;
            case R.id.u_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.u);
                intent.putExtra("alpha", 'U');
                startActivity(intent);
                break;
            case R.id.v_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.v);
                intent.putExtra("alpha", 'V');
                startActivity(intent);
                break;
            case R.id.w_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.w);
                intent.putExtra("alpha", 'W');
                startActivity(intent);
                break;
            case R.id.x_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.x);
                intent.putExtra("alpha", 'X');
                startActivity(intent);
                break;
            case R.id.y_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.y);
                intent.putExtra("alpha", 'Y');
                startActivity(intent);
                break;
            case R.id.z_button:
                intent = new Intent(getApplicationContext(), VideoPlayActivity.class);
                intent.putExtra("file", R.raw.z);
                intent.putExtra("alpha", 'Z');
                startActivity(intent);
                break;
        }
    }
}
