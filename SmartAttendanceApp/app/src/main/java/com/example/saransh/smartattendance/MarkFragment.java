package com.example.saransh.smartattendance;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MarkFragment extends Fragment {

    Button getAttendance;
    Button markAttendance;
    private RequestQueue mQueue;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.mark_attendance, container, false);
        getAttendance = (Button) rootView.findViewById(R.id.attendance);

        getAttendance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), present.class);
                startActivity(intent);
            }
        });

        markAttendance = (Button) rootView.findViewById(R.id.mark);
        markAttendance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mQueue = Volley.newRequestQueue(getActivity());
                String url = "http://192.168.43.210:5000/mark";
                JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,

                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                try {
                                    JSONArray jsonArray = response.getJSONArray("present");

                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error.printStackTrace();

                    }
                });

                mQueue.add(request);

            }
        });

        return rootView;
    }
}
