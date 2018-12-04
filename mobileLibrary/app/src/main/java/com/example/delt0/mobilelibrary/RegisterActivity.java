package com.example.delt0.mobilelibrary;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class RegisterActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_register);
            setTitle("onlineLibrary - Peru");
        }

        public void showMessage(String message) {
            Toast.makeText(this, message, Toast.LENGTH_LONG).show();
        }

        public Activity getActivity() {
            return this;
        }

        public void onClickBtnRegister(View v) {
            EditText txtUsername = (EditText) findViewById(R.id.txtUsername);
            EditText txtPassword = (EditText) findViewById(R.id.txtPassword);

            //IMPORTANTE
            //No se olviden de cambiar su puerto de acuerdo a su servidor (8080 o 5000)
            String url = "http://10.0.2.2:5000/mobile_register";
            RequestQueue queue = Volley.newRequestQueue(this);

            Map<String, String> params = new HashMap();
            params.put("email", txtUsername.getText().toString());
            params.put("password", txtPassword.getText().toString());

            JSONObject parameters = new JSONObject(params);
            JsonObjectRequest jsonObjectRequest = new JsonObjectRequest
                    (
                            Request.Method.POST,
                            url,
                            parameters,
                            new Response.Listener<JSONObject>() {
                                @Override
                                public void onResponse(JSONObject response) {
                                    try {
                                        boolean ok = response.getBoolean("response");
                                        if (ok) {
                                            Intent intent = new Intent(getActivity(), BooksActivity.class);
                                            startActivity(intent);
                                        } else {
                                            showMessage("Wrong Email or Password");
                                        }
                                    } catch (JSONException e) {
                                        e.printStackTrace();
                                    }
                                }
                            },
                            new Response.ErrorListener() {
                                @Override
                                public void onErrorResponse(VolleyError error) {
                                    error.printStackTrace();
                                    showMessage(error.getMessage());
                                }
                            });
            queue.add(jsonObjectRequest);
        }
    }
