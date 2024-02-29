import sys
import argparse
import os.path as osp
from glob import glob

import numpy as np
from tqdm import tqdm


def convert_bboxes_from_yolo_to_x1y1x2y2(bbox, w, h):
 
    probs = bbox[:, -1]
    bbox_new = bbox[:, 1:-1].copy()
    
    if len(bbox_new) > 0:
        bbox_new[:, :2] = bbox_new[:, :2] - bbox_new[:, 2:] * 0.5
        bbox_new[:, 2:] = bbox_new[:, 2:] + bbox_new[:, :2]
        bbox_new *= np.array([h, w])[[1, 0, 1, 0]]
 
    return bbox_new, probs


def bboxes2txt(f_id, bboxes, im_name):
    f_id.write('%s\n%d\n' % (im_name, len(bboxes) if bboxes is not None else 0))
    if bboxes is None or len(bboxes) == 0:
        return
    rects = np.hstack([bboxes[:, :2], bboxes[:, 2:4] - bboxes[:, :2] + 1, bboxes[:, 4].reshape(-1, 1)]) # x1, y1, h, w
    for rect in rects:
        f_id.write('%.2f %.2f %.2f %.2f %f\n' % tuple(rect))
    f_id.flush()


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_predictions', type=str, default='')
    parser.add_argument('--path_to_save_txt_file', type=str, default='')
    parser.add_argument('--width', type=int, default=1920)
    parser.add_argument('--height', type=int, default=1080)

    return parser.parse_args(argv)




def main(args):

    dir_temp = args.path_to_predictions + '/*/labels/*'
    filenames = sorted(glob(dir_temp))

    with open(args.path_to_save_txt_file, 'w') as file:
        for fname in tqdm(filenames, total=len(filenames)):
            
            bbox_yolo = np.loadtxt(fname)

            if len(bbox_yolo.shape) == 1:
                bbox_yolo = bbox_yolo[np.newaxis]

            bbox_pred, score = convert_bboxes_from_yolo_to_x1y1x2y2(bbox_yolo, args.width, args.height)
            bboxes_st = np.hstack([bbox_pred, score[np.newaxis].T])

            str_splits = fname.split('/')

            outname = osp.join(str_splits[-3], str_splits[-1])
            outname = outname[:-3] + 'jpeg'
            bboxes2txt(file, bboxes_st, outname)
    


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
