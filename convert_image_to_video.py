###
This will convert the images produced by Tensorflow Object Detection API back to an MP4 video. 
Source: http://www.sroboto.com/2017/09/pass-video-into-tensorflow-object.html
###

from moviepy.editor import ImageSequenceClip
clip = ImageSequenceClip("video_output/output", fps=2)
clip.to_videofile("video_output/output/output.mp4", fps=2) # many options available
