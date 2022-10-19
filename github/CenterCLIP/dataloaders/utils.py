import av
import copy, math

def find_max(data, threshold=0.05):
    num_frames = len(data)
    min_f, max_f = [], []
    
    max_f.append((0, 0))
    last = 'min'
    tmp_min, tmp_max = (0, 0), (0, data[0])

    for i, d in enumerate(data):
        if last == 'min':
            if tmp_max[1] < d:
                tmp_max = (i, d)
            else:
                if tmp_max[1] - d > threshold:
                    max_f.append(tmp_max)
                    tmp_min = (i, d)
                    last = 'max'

        elif last == 'max':
            if tmp_min[1] > d:
                tmp_min = (i, d)
            else:
                if d - tmp_min[1] > threshold:
                    min_f.append(tmp_min)
                    tmp_max = (i, d)
                    last = 'min'
    max_f.append((len(data), 0))

    return max_f

def frames_per_direct_seg(max_f, seg=12):
    frac = []
    nseg = []
    for i in range(1, len(max_f)):
        ratio = (max_f[i][0] - max_f[i - 1][0]) / max_f[-1][0] * seg
        nseg.append(math.floor(ratio))
        frac.append((-(ratio - math.floor(ratio)), i - 1))
        seg -= math.floor(ratio)
    frac.sort()
    i = 0
    while (seg):
        nseg[frac[i][1]] += 1
        i += 1
        seg -= 1
        if i == len(nseg):
            i = 0
    return nseg

def frames_per_indirect_seg(max_f, seg=12):
    segcnt = len(max_f) - 1
    nframe = [0] * segcnt
    i = 0
    while seg > 0 :
        if nframe[i] < max_f[i + 1][0] - max_f[i][0]:
            nframe[i] += 1
            seg -= 1
        i += 1
        if i == segcnt:
            i = 0
    return nframe

def get_boundary_frame(video_path, max_f, save_path):
    container = av.open(video_path)
    video_stream = container.streams.video[0]
    num_frames, fps = video_stream.frames, float(video_stream.average_rate)

    idx, frames = [], []
    max_f = max_f[1:-1]
    for i, frame in enumerate(container.decode(video=0)):
        for j in max_f:
            if j[0] == i:   
                idx.append(i)
                frames.append(frame)
                
                # save
                frame.to_image().save(f'{save_path}_{i}.jpg')
    breakpoint()
    return idx, frames

def get_video_data(video_path, start_time=None, end_time=None, random_shift=None):
    # pyav decode -- container and streams
    random_shift = True if random_shift is None else random_shift

    assert os.path.exists(video_path), "{} does not exist".format(video_path)
    container = av.open(video_path)

    video_stream = container.streams.video[0]
    num_frames, fps = video_stream.frames, float(video_stream.average_rate)

    print(f'num_frames fps {num_frames} {fps}')

import os
import pickle

if __name__ == "__main__":
    vid = 'video8671'
    save_path = '/home/estela19/workspace/vlret/result/video8671/vss'
    with open('/home/estela19/workspace/vlret/dataset/msrvtt/msrvtt_boundary_prob.pkl', 'rb') as f:
        data = pickle.load(f)
    v = data['video8671']
    max_f = find_max(v)
    # print(len(v))
    # print(max_f)
    # seg = frames_per_indirect_seg(max_f)
    # print(seg)

    # idx, frames = get_boundary_frame('/home/estela19/workspace/vlret/dataset/msrvtt/MSRVTT/videos/all/video8671.mp4', max_f, save_path)
    # print(idx)
    # print(frames)
    get_video_data('/home/estela19/workspace/vlret/dataset/msrvtt/MSRVTT/videos/all/video8671.mp4')