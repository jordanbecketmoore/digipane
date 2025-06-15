from flask import Flask, request, jsonify
import os
from crop import crop_left_video, crop_right_video
from download import download_youtube_video
from display import play_video


app = Flask(__name__)

@app.route('/api/videos', methods=['POST'])
def post_videos():
    try:
        # Extract the "url" field from the JSON payload
        data = request.get_json()
        url = data.get("url")
        
        if not url:
            return jsonify({"error": "Missing 'url' field in request payload"}), 400
        
        # Call the download_youtube_video function
        downloaded_path = download_youtube_video(url)
        
        return jsonify({"message": "Video downloaded successfully", "path": downloaded_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/display', methods=['PUT'])
def display_video():
    try:
        # Extract the "path" field from the JSON payload
        data = request.get_json()
        path = data.get("path")
        
        if not path:
            return jsonify({"error": "Missing 'path' field in request payload"}), 400
        
        # Check if the file exists
        if not os.path.exists(path):
            return jsonify({"error": f"File not found: {path}"}), 404
        
        # Display the video (this is a placeholder, actual display logic would depend on your frontend)
        play_video(path)
        return jsonify({"message": f"Displaying video at {path}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3141, debug=True)