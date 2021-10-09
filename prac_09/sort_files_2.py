import os
import shutil


os.chdir('FilesToSort')
new_dirs = []
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue
    extension = filename.split('.')[-1]
    if extension not in new_dirs:
        os.mkdir(extension)
        new_dirs.append(extension)
    shutil.move(filename, extension + '/' + filename)
