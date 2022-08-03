import random
import os
import shutil
# cli --input demo --output demo_sample --size 100 --seed 1
dir_name = 'demo' # input
files = os.listdir(dir_name)
size = 2
# random.seed(1) 
sample = random.sample(range(0, len(files)), size)
print(sample)
dest_name = 'demo_sample'
for idx in sample:
    os.makedirs(dest_name, exist_ok=True)
    shutil.copy(os.path.join(dir_name, files[idx]), os.path.join(dest_name, files[idx]))