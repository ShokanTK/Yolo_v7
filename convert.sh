
PRED_DIR=./runs/detect

SAVE_TXT=./baseline_pred_public.txt

python convert_predictions.py --path_to_predictions $PRED_DIR --path_to_save_txt_file $SAVE_TXT --width 1920 --height 1080
