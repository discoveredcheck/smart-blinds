package com.example.blindscontrol;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ProgressBar;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.w3c.dom.Text;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    String SERVER = "http://192.168.1.181:5000/";
    //String SERVER = "http://0.0.0.0:5000/";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        System.out.println("HEREHEREHERER");
        ProgressBar bar = (ProgressBar) findViewById(R.id.progressBar);
        bar.setVisibility((View.VISIBLE));
        findViewById(R.id.btn_down).setEnabled(false);
        findViewById(R.id.btn_up).setEnabled(false);
        connectionCheck();
        findViewById(R.id.btn_down).setOnClickListener(new View.OnClickListener(){
            public void onClick(View v) {
                sendRequest("close");
            }
        });
        findViewById(R.id.btn_up).setOnClickListener(new View.OnClickListener(){
            public void onClick(View v) {
                sendRequest("open");
            }
        });
        findViewById(R.id.btn_stop).setOnClickListener(new View.OnClickListener(){
            public void onClick(View v) {
                sendRequest("stop");
            }
        });
    }

    public void sendRequest(String suffix) {
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = this.SERVER+suffix;
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        System.out.println(response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                error.printStackTrace();
            }
        });
        queue.add(stringRequest);
    }

    public void connectionCheck() {
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = this.SERVER;
        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        System.out.println(response);
                        findViewById(R.id.progressBar).setVisibility(View.GONE);
                        findViewById(R.id.btn_down).setEnabled(true);
                        findViewById(R.id.btn_up).setEnabled(true);
                        findViewById(R.id.btn_stop).setEnabled(true);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                error.printStackTrace();
                findViewById(R.id.progressBar).setVisibility(View.VISIBLE);
                findViewById(R.id.btn_down).setEnabled(false);
                findViewById(R.id.btn_up).setEnabled(false);
                findViewById(R.id.btn_stop).setEnabled(true);
            }
        });
        queue.add(stringRequest);
    }
}