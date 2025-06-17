from flask import Flask, request, jsonify
import os
from crop import crop_left_video, crop_right_video
from download import download_youtube_video
import mpv
from moviepy import VideoFileClip


app = Flask(__name__)

player_right = mpv.MPV()
player_left = mpv.MPV()

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
def put_display():
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

@app.route('/api/display', methods=['DELETE'])
def delete_display():
    try:
        player_left.stop()
        player_right.stop()
        return jsonify({"message": "Display closed."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def play_video(video_path): 
    ## Load the video file
    video = VideoFileClip(video_path)

    ## Calcualte width and height for cropping
    display_height = video.size[1]
    display_width = display_height * (9 / 16)

    ## Set left and right crop starting points
    left_x = 0
    left_y = 0
    right_x = video.size[0] - display_width
    right_y = 0

    # Configure MPV players
    
    # player_left["fullscreen"] = True
    player_left["loop-file"] = "inf"  # Loop the video indefinitely
    player_left["video-crop"] = f"{display_width:.0f}x{display_height:.0f}+{left_x:.0f}+{left_y:.0f}"

    # player_right["fullscreen"] = True
    player_right["loop-file"] = "inf"  # Loop the video indefinitely
    player_right["video-crop"] = f"{display_width:.0f}x{display_height:.0f}+{right_x:.0f}+{right_y:.0f}"

    # Play the video in both players
    player_left.play(video_path)
    player_right.play(video_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3141, debug=True)