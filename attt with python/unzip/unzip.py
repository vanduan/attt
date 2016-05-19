import zipfile
import os
import sys
count = 0
path = "/path"
folder = ''
while 1:
    pathnew = path +'/'+ folder
    for file in os.listdir(pathnew):
        if file != 'unzip.py':
            try:
                print 'extracting file: ', file
                zip = zipfile.ZipFile(pathnew+'/'+file,'r')
                folder = 'unzip'+str(count)
                zip.extractall(folder)
                zip.close()
                count += 1
            except:
                print 'done =>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
                print 'flag in',folder
                sys.exit()
                