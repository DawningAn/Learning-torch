import os

root_dir = '练手数据集/train'
target_dir = 'ants_image'
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split('_')[0]  # 即ants作为标签
out_dir = 'ants_label'
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir, out_dir, "{}.txt".format(file_name)), 'w') as f:
        f.write(label)
