import os, sys
from os import listdir, getcwd
from os.path import join
import imagesize

infiles = sys.argv[1:]
indir = '/disk1/DeepFashion/BBOX2017/'

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for infile in infiles:
    if not os.path.exists(indir + 'labels/' + infile):
        os.makedirs(indir + 'labels/' + infile)
    list_file = open(infile + '_train.txt', 'w')
    f = open(indir + 'Annotations/' + infile + '.txt', 'r')
    i = 0
    for line in f:
        i += 1
        if i < 3: continue
        items = line.split()
        imgfile = '%s/JPEGImages/%s/%s' % (indir, infile, items[0])
        list_file.write('%s\n'% imgfile)
        w, h = imagesize.get(imgfile)
        out_file = open('%s/labels/%s/%s.txt' % (indir, infile, items[0][0:-4].replace('/', '_')), 'a')
        b = (float(items[2]), float(items[4]), float(items[3]), float(items[5]))
        bb = convert((w, h), b)
        out_file.write(items[1] + " " + " ".join([str(a) for a in bb]) + '\n')
        out_file.close()
    list_file.close()

