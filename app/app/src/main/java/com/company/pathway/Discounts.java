package com.company.pathway;

import android.content.DialogInterface;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.Toast;

public class Discounts extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_discounts);

        View.OnClickListener notenough = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(Discounts.this, "You don't have enough points", Toast.LENGTH_SHORT).show();
            }
        };
        final int points = getSharedPreferences("POINTS", MODE_PRIVATE).getInt("points", 542);
        LinearLayout first = findViewById(R.id.first);
        LinearLayout second = findViewById(R.id.second);
        LinearLayout third = findViewById(R.id.third);
        LinearLayout fourth = findViewById(R.id.fourth);
        fourth.setOnClickListener(notenough);
        third.setOnClickListener(notenough);
        second.setOnClickListener(notenough);
        if (points > 600) {
            first.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    new AlertDialog.Builder(Discounts.this)
                            .setTitle("Claim reward")
                            .setMessage("Are you sure you want to claim this reward? 600 points will be removed from your account, and you will be notified about your rewad from your insurance company.")

                            // Specifying a listener allows you to take an action before dismissing the dialog.
                            // The dialog is automatically dismissed when a dialog button is clicked.
                            .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int which) {
                                    getSharedPreferences("POINTS", MODE_PRIVATE).edit().putInt("points", points - 600).apply();
                                }
                            })

                            // A null listener allows the button to dismiss the dialog and take no further action.
                            .setNegativeButton(android.R.string.cancel, null)
                            .setIcon(android.R.drawable.ic_dialog_alert)
                            .show();
                }
            });
        } else {
            first.setOnClickListener(notenough);
        }
    }
}
