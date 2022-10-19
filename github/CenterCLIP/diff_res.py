import pandas as pd
import csv

if __name__=='__main__':
	video = [23, 32, 73, 79, 153, 166, 220, 235, 281, 286, 393, 412, 413, 420, 435, 437, 462, 482, 506, 567, 593, 655, 660, 687, 725, 740, 830, 880, 935, 958]
	misret= [959, 549, 549, 440, 331, 215, 105, 635, 154, 33, 606, 14, 969, 674, 210, 962, 651, 425, 251, 137, 346, 972, 270, 250, 783, 209, 554, 28, 410, 886]
	data = pd.read_csv('/home/estela19/workspace/vlret/dataset/msrvtt/msrvtt_data/MSRVTT_JSFUSION_test.csv')

	res = {}
	res['video_id'], res['ours'], res['centerclip'] = [], [], []

	print('video_id,ours,centerclip')
	for i, j in zip(video, misret):
		vid = data['video_id'].values[i-2]
		ours = data['sentence'].values[i-2]
		centerclip = data['sentence'].values[j-2]
		print(f'{vid},{ours},{centerclip}')
		# res['video_id'].append(data['video_id'].values[i])
		# res['ours'].append(data['sentence'].values[i])
		# res['centerclip'].append(data['sentence'].values[j])

	# with open('/home/estela19/workspace/vlret/res.csv', 'w') as f:
	# 	w = csv.writer(f)
	# 	w.writerow(res.keys())
	# 	w.writerow(res.values())