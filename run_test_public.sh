OPENSET=./prepared_data/testset_open

for dirname in ${OPENSET}/*; do

basedir=$(basename -- $dirname)

python detect.py --weights ./runs/train/baseline/weights/epoch_099.pt \
                --source $dirname --img-size 1280 \
                --conf-thres 0.0 --device 1 --name $basedir --save-conf --save-txt

done
