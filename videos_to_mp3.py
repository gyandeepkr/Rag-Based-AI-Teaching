# converts the videos to mp3

import os 
import subprocess

files = os.listdir("videos")
for file in files:
    # print(file)
    tutorial_number= file.split(" @")[0]
    print(tutorial_number)
    subprocess.run(["ffmpeg","-i",f"videos/{file}", f"audios/{tutorial_number}.mp3"])