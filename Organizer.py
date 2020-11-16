import os
import shutil

path='/home/arun/Pictures'
listoffiles=os.listdir(path)


for files in listoffiles:
    name,extension=os.path.splitext(files)
    print(files)
    extension=extension[1:]
    
    if os.path.exists(path+'/'+extension):
       shutil.move(path+'/'+files,path+'/'+extension+'/'+files)
       
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+files,path+'/'+extension+'/'+files)
