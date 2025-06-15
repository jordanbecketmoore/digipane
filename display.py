import subprocess

MPV_OPTIONS = ["--fullscreen", "--no-audio", "--loop-file=inf"]

MPV_PROCESSES = []

def play_video(video_path):
    # Terminate any existing MPV processes before starting a new one
    if len(MPV_PROCESSES) > 0:
        for process in MPV_PROCESSES:
            process.terminate()
        MPV_PROCESSES.clear()
    # Start a new MPV process to play the video
    try:
        MPV_PROCESSES.append(subprocess.Popen(["mpv"] + MPV_OPTIONS + [video_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while playing video: {e}")
    except FileNotFoundError:
        print("mpv is not installed or not found in PATH.")

if __name__ == "__main__":
    video_path = "vid.webm"  # Replace with your video file path
    play_video(video_path)
