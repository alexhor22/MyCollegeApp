package com.mcc_commit.mycollegecalories;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    public final static String EXTRA_START = "com.mcc_commit.mycollegecalories.START";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /** Called when the user clicks the Start button */
    public void startButton(View view) {
        Intent intent = new Intent(this, DisplayAppOptions.class);
        startActivity(intent);
    }
}
