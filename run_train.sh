python -m torch.distributed.launch --nproc_per_node 2 --master_port 9526 \
            train_aux.py --workers 10 --device 0,1 --sync-bn \
            --batch-size 20 --data ./data/vl_hpuck_003_2202.yaml \
            --img 1280 1280 --cfg ./cfg/training/yolov7-w6.yaml  --epochs 100 \
            --weights ./yolov7-w6.pt --name baseline --hyp ./data/hyp_vl_0029.scratch.p6.yaml