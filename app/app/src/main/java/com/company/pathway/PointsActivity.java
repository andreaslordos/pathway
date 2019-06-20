package com.company.pathway;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.text.MessageFormat;

import me.tankery.lib.circularseekbar.CircularSeekBar;

public class PointsActivity extends AppCompatActivity {
    SharedPreferences.Editor sharedPreferences;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_points);
        sharedPreferences = getSharedPreferences("POINTS", MODE_PRIVATE).edit();
        sharedPreferences.putInt("points", 642).apply();

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(PointsActivity.this, Discounts.class));
            }
        });
    }

    @Override
    protected void onResume(){
        super.onResume();
        SharedPreferences prefs = getSharedPreferences("POINTS", MODE_PRIVATE);
        int points = prefs.getInt("points", 542);
        TextView point = findViewById(R.id.points);
        point.setText(String.valueOf(points));
        CircularSeekBar seekBar = findViewById(R.id.circle);
        TextView pointsleft = findViewById(R.id.left);
        if(points<600){
            seekBar.setProgress(100*(((float)points)/600));
            pointsleft.setText(MessageFormat.format("{0} {1}", 600 - points, getString(R.string.points_left)));
        }
        else if(points<1000){
            seekBar.setProgress(((float)points)/10);
            pointsleft.setText(MessageFormat.format("{0} {1}", 1000 - points, getString(R.string.points_left)));
        }
    }
}
