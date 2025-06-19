import yt_dlp 
from PIL import Image
from moviepy import VideoFileClip
import os
from db import *

output_path = "library"

def add_youtube_video(url):

    # Ensure the output directories exist
    os.makedirs(f"{output_path}/videos", exist_ok=True)
    os.makedirs(f"{output_path}/thumbnails", exist_ok=True)

    video_path = download_youtube_video(url)
    title = os.path.splitext(os.path.basename(video_path))[0]
    thumbnail_path = extract_thumbnail(video_path)

    new_video = Video.create(
        title=title,
        thumbnail_path=thumbnail_path,
        video_path=video_path
    )


def download_youtube_video(url): 
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio quality
        'merge_output_format': 'mp4',         # Merge video and audio into MP4 format
        'outtmpl': f'{output_path}/videos/%(title)s.%(ext)s',  # Output file template
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'unknown_title')
        video_extension = info_dict.get('ext', 'mp4')
        video_duration = info_dict.get('duration', 0)  # Duration in seconds
        downloaded_path = f"{output_path}/videos/{video_title}.{video_extension}"

    # Check if the video is longer than 15 minutes
    if video_duration > 15 * 60:
        midpoint = video_duration // 2
        start_time = max(midpoint - 5 * 60, 0)  # Start time for trimming
        end_time = min(midpoint + 5 * 60, video_duration)  # End time for trimming
        trimmed_path = f"{output_path}/videos/{video_title}_trimmed.{video_extension}"

        # Use moviepy to trim the video
        with VideoFileClip(downloaded_path) as video:
            trimmed_video = video.subclip(start_time, end_time)
            trimmed_video.write_videofile(trimmed_path, codec="libx264", audio_codec="aac")

    
    extract_thumbnail(downloaded_path)

    return downloaded_path

def extract_thumbnail(video_path):
    # Define the output image path
    output_image_path = f"{output_path}/thumbnails/{video_path.split('/')[-1].split('.')[0]}.jpg"
    
    # Ensure the thumbnails directory exists
    thumbnails_dir = os.path.dirname(output_image_path)
    os.makedirs(thumbnails_dir, exist_ok=True)
    
    # Load the video file
    with VideoFileClip(video_path) as video:
        # Get the frame at the specified time
        frame = video.get_frame(video.duration / 2)  # Get the middle frame of the video
        
        # Convert the frame (numpy array) to a PIL image
        pil_image = Image.fromarray(frame)
        
        # Save the image as a thumbnail
        pil_image.save(output_image_path)
    return output_image_path