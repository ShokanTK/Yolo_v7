import os
import argparse

def bags_stat(res_path, info_file):
    #num_frames = len(os.listdir(res_path.replace('mining_res', 'mining_data').replace('labels/', '')))
    num_frames = len(os.listdir(res_path.replace('/netapp/a.sergeeva/BAGS/bag/mining_res/', '/ssd/a.sergeeva/BAGS/DIT_1000_cams/').replace('labels/', '')))
    files = sorted(os.listdir(res_path))
    sum_bbox = 0
    num_frames_with_box = len(files)
    for file in files:
        with open(res_path + file, 'r') as f:
            data = f.read()
        sum_bbox += len(data.split('\n'))

    info_str = f'\n\
        {res_path}\n\
        Num frames: {num_frames}\n\
        Num frames with box: {num_frames_with_box}\n\
        Num bboxes: {sum_bbox}\n\
        Bboxes per frame mean: {sum_bbox // num_frames}\n\
        ---------------------------------------------------\n'
    print(info_str)
    with open(info_file, 'a') as f:
        f.write(info_str)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--res_path', help='labels')
    parser.add_argument('--info_file', help='save')  # file/folder, 0 for webcam
  
    opt = parser.parse_args()
    bags_stat(opt.res_path, opt.info_file)