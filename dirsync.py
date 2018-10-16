from shutil import copytree, copy2
import os
sourcerootfolder =  input("Source folder: /home/emrah/Documents/1:")
destinationrootfolder =  input("Source folder: /home/emrah/Pictures/Wallpapers/2:")
for root, dirs, files in os.walk(sourcerootfolder, topdown=True):
    for dname in sorted(dirs):
        fullsourcepath=os.path.join(root, dname)
        print (fullsourcepath)
        relativedestpath=destinationrootfolder+fullsourcepath.replace(sourcerootfolder,"")
        print (relativedestpath)
        if os.path.exists(relativedestpath):
            print ("directory already exist")
        else:
            print ("copying the directory")
            copytree(os.path.join(root, dname), relativedestpath, symlinks=False, ignore=None)
    for fname in sorted(files):
        fullsourcefpath=os.path.join(root, fname)
        print (fname)
        relativedestpath2=destinationrootfolder+fullsourcefpath.replace(sourcerootfolder,"")
        print (relativedestpath2)
        if os.path.exists(relativedestpath2):
            print ("file already exist")
        else:
            print ("copying the file")
            destnewfile=destinationrootfolder+"/"+fname
            copy2(os.path.join(root, fname), relativedestpath2)
