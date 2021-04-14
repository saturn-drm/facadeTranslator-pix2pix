import os
import sys
from PIL import Image

# Usage: python reversePic.py [infolder] [outfolder]
infolder = sys.argv[1]
outfolder = sys.argv[2]
left_emu = (0, 0, 256, 256)
right_emu = (256, 0, 512, 256)

# make place for all the subfolders, e.g. train, test, val
def createOutFolders(inpath, outpath):
    for subdir in os.scandir(inpath):
        if subdir.is_dir():
            outsubdir = os.path.join(outpath, subdir.name)
            if not os.path.exists(outsubdir):
                os.makedirs(outsubdir)

# reverse the image
def reverseIMG(inname, left_emu, right_emu):
    im = Image.open(inname)
    left_img = im.crop(left_emu)
    right_img = im.crop(right_emu)
    target = Image.new('RGB', (512, 256))
    target.paste(right_img, left_emu)
    target.paste(left_img, right_emu)
    target.save(inname2outname(inname, outfolder))

# get the list of input image names, e.g. west/test/1.jpg
def getInputNameList(inpath):
    innames = []
    for root, subfolders, files in os.walk(inpath):
        for f in files:
            if not f == '.DS_Store':
                innames.append(os.path.join(root, f))
    return innames

# create the output image name correspondingly, e.g. west2/test/1.jpg
def inname2outname(inname, outpath):
    subdir = os.path.basename(os.path.dirname(inname))
    return os.path.join(outpath, os.path.join(subdir, os.path.basename(inname)))

if __name__ == '__main__':
    createOutFolders(infolder, outfolder)
    inputnames = getInputNameList(infolder)
    for inputname in inputnames:
        reverseIMG(inputname, left_emu, right_emu)