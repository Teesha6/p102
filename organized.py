import os
import shutil

from = "C:/Users/teesh/Downloads"
to = "C:/Users/teesh/Downloads/F2 pdf"
list = os.listdir(from)
for file in list:
    name, ext = os.path.splitext(file)
    if ext == '':
        continue
    if ext in ['.pdf']:
        p1 = from + '/' + file
        p2 = to + '/' + "pdf"
        p3 = to + '/' + "pdf" + '/' + file
        if os.path.exists(p2):
            print("moving" + file + "...")
            shutil.move(p1,p3)
        else:
            os.mkdirs(p2)
            print("moving" + file + "...")
            shutil.move(p1,p3)
