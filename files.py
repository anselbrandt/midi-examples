import os

root = "midi"
dirs = [os.path.join(root, dir) for dir in os.listdir(root) if os.path.isdir(os.path.join(root,dir))]
files = [os.path.join(dir, file) for dir in dirs for file in os.listdir(dir) if os.path.isfile(os.path.join(dir,file))]

for file in files:
    print(file)