#
#Copy file from
#
# %userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
#
#to
# C:\Users\trina\OneDrive\Desktop\WallPapers
#
from  shutil import copyfile
import os

SourceFolder = "C:\\Users\\trina\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
DistFolder = "C:\\Users\\trina\\OneDrive\\Desktop\\WallPapers"

for name in os.listdir(SourceFolder):
    #Find the file size, we will copy the file if size > 100,000
    src =  SourceFolder + "\\" + name
    statinfo = os.stat(src)
    if statinfo.st_size > 100000:
        dst = DistFolder + "\\" + name + ".jpg"
        #print(statinfo.st_size)
        print(dst)
        #move the file to DistFolder.
        copyfile(src, dst)
