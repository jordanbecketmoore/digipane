import yt_dlp 

output_path = "library"
def download_youtube_video(url): 
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio quality
        'merge_output_format': 'mp4',         # Merge video and audio into MP4 format
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file template
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'unknown_title')
        video_extension = info_dict.get('ext', 'mp4')
        downloaded_path = f"{output_path}/{video_title}.{video_extension}"
    
    return downloaded_path