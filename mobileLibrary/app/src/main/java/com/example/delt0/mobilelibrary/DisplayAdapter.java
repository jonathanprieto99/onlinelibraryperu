package com.example.delt0.mobilelibrary;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class DisplayAdapter extends RecyclerView.Adapter<DisplayAdapter.ViewHolder> {

    public JSONArray elements;
    private Context mContext;

    public DisplayAdapter(JSONArray elements, Context mContext) {
        this.elements = elements;
        this.mContext = mContext;
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView friendLine;
        TextView myLine;
        RelativeLayout container;

        public ViewHolder(View itemView) {
            super(itemView);
            friendLine = itemView.findViewById(R.id.element_view_friend_line);
            myLine = itemView.findViewById(R.id.element_view_me_line);
            container = itemView.findViewById(R.id.element_view_container);
        }
    }

    @NonNull
    @Override
    public DisplayAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(
                parent.getContext()).inflate(
                R.layout.activity_book_adapter, parent, false
        );
        return new DisplayAdapter.ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull DisplayAdapter.ViewHolder holder, int position) {
        try{
            JSONObject element = elements.getJSONObject(position);
            String descripcion = element.getString("descripcion");
            holder.myLine.setText("");
            holder.friendLine.setText(descripcion);

        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    @Override
    public int getItemCount() {
        return elements.length();
    }
}

