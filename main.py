from moviepy import *

def crop_left_video(input_path, output_path):

    # Load the video file
    video = VideoFileClip(input_path)

    # Crop the video to the left-most 9:16 slice
    y2 = video.size[1]
    x2 = y2 * (9 / 16)
    cropped_video = video.with_effects([vfx.Crop(x1=0, y1=0, x2=x2, y2=y2)])

    # Save the cropped video
    cropped_video.write_videofile(output_path)

def crop_right_video(input_path, output_path):

    # Load the video file
    video = VideoFileClip(input_path)

    # Crop the video to the left-most 9:16 slice
    y2 = video.size[1]
    x1 = video.size[0] - (y2 * (9 / 16))
    cropped_video = video.with_effects([vfx.Crop(x1=x1, y1=0, x2=video.size[0], y2=y2)])

    # Save the cropped video
    cropped_video.write_videofile(output_path)
# Example usage:

if __name__ == "__main__":
    import sys 
    input_video_path = sys.argv[1]
    input_video_name = input_video_path.split('/')[-1].split('.')[0]
    input_video_extension = input_video_path.split('/')[-1].split('.')[-1]
    crop_left_video(input_video_path, f"{input_video_name}_left_cropped.{input_video_extension}")
    crop_right_video(input_video_path, f"{input_video_name}_right_cropped.{input_video_extension}")