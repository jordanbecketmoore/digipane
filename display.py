import subprocess
from moviepy import VideoFileClip

MPV_OPTIONS = ["--fullscreen", "--no-audio", "--loop-file=inf"]

MPV_PROCESSES = []

def play_video(video_path):
    # Terminate any existing MPV processes before starting a new one
    if len(MPV_PROCESSES) > 0:
        for process in MPV_PROCESSES:
            process.terminate()
        MPV_PROCESSES.clear()
    
    # Calculate crop dimensions

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
    
    # Start a new MPV process to play the video
    try:
        # MPV_PROCESSES.append(subprocess.Popen(["mpv"] + MPV_OPTIONS + [f"--video-crop={display_width}x{display_height}+{left_x}+{right_x}"] + [video_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        MPV_PROCESSES.append(subprocess.Popen(["mpv"] + MPV_OPTIONS + [f"--video-crop={display_width:.0f}x{display_height:.0f}+{left_x:.0f}+{left_y:.0f}"] + [video_path]))
        MPV_PROCESSES.append(subprocess.Popen(["mpv"] + MPV_OPTIONS + [f"--video-crop={display_width:.0f}x{display_height:.0f}+{right_x:.0f}+{right_y:.0f}"] + [video_path]))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while playing video: {e}")
    except FileNotFoundError:
        print("mpv is not installed or not found in PATH.")

if __name__ == "__main__":
    video_path = "vid.webm"  # Replace with your video file path
    play_video(video_path)
