import os
import shutil


os.chdir('FilesToSort')
ext_to_dir = {}
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue
    extension = filename.split('.')[-1]
    if extension not in ext_to_dir:
        new_dir = input(f'What category would you like to sort {extension} files into? ')
        if new_dir not in ext_to_dir.values():
            os.mkdir(new_dir)
        ext_to_dir[extension] = new_dir
    shutil.move(filename, ext_to_dir[extension] + '/' + filename)
