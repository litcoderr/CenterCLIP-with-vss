
import os
import argparse
import subprocess
from tqdm import tqdm
from multiprocessing import Pool


def split(input_video_path, output_root, video_name):
    shot_path = os.path.join(output_root, video_name)
    os.mkdir(shot_path)
    try:
        # https://trac.ffmpeg.org/ticket/309
        command = ['ffmpeg',
                   '-i', input_video_path,
                   os.path.join(shot_path, "%04d.png"),
                   ]
        ffmpeg = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = ffmpeg.communicate()
        retcode = ffmpeg.poll()
        # print something above for debug
    except Exception as e:
        raise e

if __name__ == "__main__":
    dataset_path = "/media/data/MSRVTT"
    video_root = os.path.join(dataset_path, "compressed")
    output_root = os.path.join(dataset_path, "shot")
    videos = os.listdir(video_root)

    for video in videos:
        video_path = os.path.join(video_root, video)
        video_name = video.split(".")[0]
        split(video_path, output_root, video_name)