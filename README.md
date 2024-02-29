# YOLOv7

Official repository - [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://github.com/WongKinYiu/yolov7)


## prepare experiment

Load project

``` shell
git clone git@git.visionlabs.ru:s.tazhimbetov/yolo_v7.git

cd yolo_v7

wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt

```

Create env

``` shell
conda create -n yolo_v7 python=3.9

conda activate yolo_v7

bash prepare_env.sh

```


Create prepared data folder

``` shell

mkdir prepared_data

cd prepared_data

cp path_to_dataset.zip ./

unzip dataset.zip

cp path_testset_open.zip ./

unzip testset_open.zip

cp train_part.cache ../data/
cp train_part.txt ../data/

cp val_part.cache ../data/
cp val_part.txt ../data/

cd ..

```

## Training

Reproducing of baseline. The baseline was trained on a subset of dataset.

``` shell
bash run_train.sh
```

## predict and convert predictions for submission
``` shell
bash run_test_public.sh

bash convert.sh
```