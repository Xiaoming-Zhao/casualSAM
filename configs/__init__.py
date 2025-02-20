# %%
from pathlib import Path
from os.path import join
project_path = str(Path(__file__).absolute().parents[1])
if False:
    depth_pretrain_path = join(
        project_path, 'pretrained_depth_ckpt/best_depth_Ours_Bilinear_inc_3_net_G.pth')
    sintel_data_pattern = './{{mode}}/{track_name}'
    sintel_seg_pattern = './moving_seg/{track_name}'
    sintel_data_root = ''
else:
    depth_pretrain_path = None
    sintel_data_pattern = None
    sintel_seg_pattern = None
    sintel_data_root = None
midas_pretrain_path = join(project_path, 'pretrained_depth_ckpt/midas_cpkt.pt')
# fill this line with your DAVIS path. Note that images should be under davis_path/JPEGImages/{track_name}/*.jpg
davis_path = "/mnt/mydata/datasets/DAVIS"
assert davis_path is not None


# %%
