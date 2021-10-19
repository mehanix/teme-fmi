'''
 Am folosit image_dataset_from_directory la modelul CNN
 care imi cere o structura specifica a datasetului pentru a functiona corect.
 Acesta este scriptul cu care mi-am generat acea structura.
 El trebuie rulat pentru a functiona CNN-ul.
 '''
import os, shutil

os.mkdir("/kaggle/working/train")

os.mkdir("/kaggle/working/train/0")
os.mkdir("/kaggle/working/train/1")
os.mkdir("/kaggle/working/train/2")
os.mkdir("/kaggle/working/validation/")
os.mkdir("/kaggle/working/validation/0")
os.mkdir("/kaggle/working/validation/1")
os.mkdir("/kaggle/working/validation/2")
os.mkdir("/kaggle/working/test_data/")
os.mkdir("/kaggle/working/test_data/test")

with open("/kaggle/input/ai-unibuc-23-31-2021/train.txt") as f:
    lines = f.readlines()
    for l in lines:
        fn,i = l.strip().split(",")
        shutil.copy(f"/kaggle/input/ai-unibuc-23-31-2021/train/{fn}",f"/kaggle/working/train/{i}/{fn}")

with open("/kaggle/input/ai-unibuc-23-31-2021/validation.txt") as f:
    lines = f.readlines()
    for l in lines:
        fn,i = l.strip().split(",")
        shutil.copy(f"/kaggle/input/ai-unibuc-23-31-2021/validation/{fn}",f"/kaggle/working/validation/{i}/{fn}")


with open("/kaggle/input/ai-unibuc-23-31-2021/test.txt") as f:
    lines = f.readlines()
    for l in lines:
        fn = l.strip()
        shutil.copy(f"/kaggle/input/ai-unibuc-23-31-2021/test/{fn}",f"/kaggle/working/test_data/test/{fn}")
    
print("done!")
