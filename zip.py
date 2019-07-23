#! /usr/bin/env python
#coding=utf-8
import os,zipfile

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
                print filelist   
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
#         
        arcname = tar[len(dirname):]
        print arcname,"+++"
        print tar
#         zf.write(tar,arcname)
#         zf.write(tar)
    zf.close()
def zip_dir2(srcPath,dstname):
    zipHandle=zipfile.ZipFile(dstname,'w',zipfile.ZIP_DEFLATED)
    if os.path.isfile(srcPath):
        zipHandle.write(srcPath)
        zipHandle.close()
    else:
        for dirpath,dirs,files in os.walk(srcPath):
            for filename in files:
                zipHandle.write(os.path.join(dirpath,filename)) #必须拼接完整文件名，这样保持目录层级
                print filename+" zip succeeded",dirpath,filename
    #         for dir in dirs:
    #             zipHandle.write(os.path.join(dirpath,dir))
    
        zipHandle.close
if __name__ == '__main__':
    zip_dir(r'E:\jira',r'E:\zip.zip')
