from moviepy.editor import *
from sys import argv
import shutil
import os
import glob
import subprocess


images = []
texts = []
clip_number = 0
line_number = 1

# get image  and text for each clip
for line in open(argv[1], 'r'):
	all_words = line.split()
	word_count = 0
	new_text = ""
	for word in all_words:
		new_text += word + " "
		word_count += 1
		if word_count == 10:
			new_text += "\n"
			word_count = 0

	images.append("./images/" + str(line_number) + ".jpg")
	texts.append(new_text)
	clip_number += 1
	line_number += 1

# create 8 second clips, exported to tmp folder
for x in range(clip_number):
	image_clip = ImageClip(images[x]).resize( (1280,720) ).set_duration(1)
	w, h = image_clip.size

	text_clip = TextClip(texts[x].replace('&', '\n'), font='Amiri-regular', fontsize = 36, color = 'white')
	text_clip = text_clip.on_color(size=(1280, text_clip.h), color=(0,0,0), col_opacity=0.6)
	# text_clip = text_clip.set_pos(lambda t: (max(w/30,int(w-1.5*w*t)), max(5*h/6,int(100*t))) )
	text_clip = text_clip.set_pos(lambda t: (max(0, 0), max(4 * h / 7, int(110 * t))))


	title = (CompositeVideoClip([image_clip.to_ImageClip(), text_clip]).fadein(.5).set_duration(9))
	tmp_video = concatenate_videoclips([title, image_clip], method="compose")
	tmp_video.write_videofile("./tmp/" + str(x) + ".mp4", fps=30)

# combine clips and create final video

videos = []
for x in range(clip_number):
	videos.append("./tmp/" + str(x) + ".mp4")

clips = [VideoFileClip(m)
         for m in videos]

audio_clip = AudioFileClip("music.mp3")

final_video = concatenate_videoclips(clips, method="compose")
final_video = final_video.set_audio(audio_clip.set_duration(final_video.duration))
final_video.write_videofile("final.mp4", audio_codec='aac',fps=30)

# delete tmp files
shutil.rmtree('./tmp')
os.mkdir('./tmp')

# launch video

# upload to youtube
subprocess.call(['./youtube-uploader.sh'])





