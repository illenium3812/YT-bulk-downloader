# importing the module 
import sys
import os
import shutil
import pandas as pd
from moviepy.editor import *
import pytube 

def read_csv(PATH,label):
    try:
        df = pd.read_csv(PATH)
    except:
        print('ERROR :File not found, check file path again')
      
    lables = df['label'].tolist()
    youtube_ids = df['youtube_id'].tolist()
    time_start = df['time_start'].tolist()
    time_end = df['time_end'].tolist()
    l = []

    for i in range(len(lables)):
        if label in lables[i]:
            l.append(lables[i] + "," + f'https://www.youtube.com/watch?v={youtube_ids[i]}' + "," + str(time_start[i]) + "," + str(time_end[i]))
    print(f'{len(l)} links found against this activity label')    
    return l

def clip(path,file_name,start_time,end_time):
    video = VideoFileClip(f'{path}\\{file_name}.mp4').subclip(start_time,end_time)
    frames = video.fps
    video.write_videofile(f'{path}\\clipped\\{file_name}.mp4',fps=frames)

def remove_special_characters(name):
    l = ["\\","/","*",":","|","?","<",">",'"']
    for letter in l:
        if letter in name:
            name = name.replace(letter,"")
    return name

def downloadVideo(urls,label):
    cwd = os.getcwd() 
    PATH = f'{cwd}\\{label} videos'
    for url in urls:
        try:
            youtube = pytube.YouTube(url.split(',')[1])
            video = youtube.streams.get_highest_resolution()
            print(f'Downloading {video.title} | size = {video.filesize/1000000} mb')
            video.download(filename = f'{PATH}\\{remove_special_characters(video.title)}.mp4')
            if youtube.length > 10:
                clip(PATH,remove_special_characters(video.title),int(url.split(',')[2]),int(url.split(',')[3]))
            else:
                original = f'{PATH}\\{remove_special_characters(video.title)}.mp4'
                target = f'{PATH}\\clipped\\{remove_special_characters(video.title)}.mp4'
                shutil.copyfile(original, target)
        except Exception as e: print(e)
    
if __name__ == "__main__":
    LABEL = sys.argv[1]
    urls = read_csv('train.csv',LABEL)
    if len(urls) == 0:
        sys.exit("System Exiting")
    try:
        os.mkdir(f'{LABEL} videos')
    except:
        pass
    try:
        os.mkdir(f'{LABEL} videos\\clipped')
    except:
        pass
    downloadVideo(urls,LABEL)
