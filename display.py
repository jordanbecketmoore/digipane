import subprocess
from moviepy import VideoFileClip
import mpv

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
    player_left = mpv.MPV()
    # player_left["fullscreen"] = True
    
    player_left["loop-file"] = "inf"  # Loop the video indefinitely
    player_left["video-crop"] = f"{display_width:.0f}x{display_height:.0f}+{left_x:.0f}+{left_y:.0f}"

    player_right = mpv.MPV()
    # player_right["fullscreen"] = True
    player_right["loop-file"] = "inf"  # Loop the video indefinitely
    player_right["video-crop"] = f"{display_width:.0f}x{display_height:.0f}+{right_x:.0f}+{right_y:.0f}"

    # Play the video in both players
    player_left.play(video_path)
    player_right.play(video_path)
    # Wait for both players to finish
    player_left.wait_for_playback()
    player_right.wait_for_playback()

if __name__ == "__main__":
    video_path = "vid.webm"  
    play_video(video_path)
