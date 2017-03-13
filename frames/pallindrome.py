import os
import shutil

files = os.listdir()
for f in files:
    if f.endswith('.jpg'):
        if 'CMB' in f:
            shutil.copyfile(f, f.replace('CMB', 'CMF'))
        if 'CMC' in f:
            shutil.copyfile(f, f.replace('CMC', 'CME'))
