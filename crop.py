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