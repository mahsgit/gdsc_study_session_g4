'''Create a Python script that identifies and collects files 
(both created and modified) in the last 24 hours from the current directory.
Update these files in some way and move them to a folder named "last_24hours."'''
import os
import shutil
import time

def move_files_to_folder(files):
    folder_name = 'the last 24hours'
    os.makedirs(folder_name, exist_ok=True)
    for file in files:
        shutil.move(file, os.path.join(folder_name, os.path.basename(file)))

files = os.listdir()
recent_files = [file for file in files if os.path.isfile(file) and time.time() - os.path.getmtime(file) < 24 * 60 * 60]

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for file in recent_files:
    with open(file, 'a') as file_obj:
        file_obj.write('\nUpdated at ' + timestamp)
move_files_to_folder(recent_files)
