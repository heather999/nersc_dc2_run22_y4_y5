import pickle, itertools
import numpy as np
import os, sys
import argparse

def checkpoints_equal(file1, file2):
    with open(file1, 'rb') as fd:
        ckpt1 = pickle.load(fd)
    with open(file2, 'rb') as fd:
        ckpt2 = pickle.load(fd)
    num_drawn1 = len(ckpt1['drawn_objects'])
    num_drawn2 = len(ckpt2['drawn_objects'])
    if ((ckpt1['drawn_objects'] == ckpt2['drawn_objects']) and
        all(np.equal(list(ckpt1['images'].values())[0],
                     list(ckpt2['images'].values())[0]).ravel())):
        return True, file1, 0
    elif num_drawn1 >= num_drawn2:
        return False, file1, num_drawn1 - num_drawn2
    return False, file2, num_drawn1 - num_drawn2



parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--indir", required=True, type=str, help="input file")
args = parser.parse_args()


with open(args.indir) as inputf:
    dirlist = inputf.readlines()
dirlist = [x.strip() for x in dirlist]    


good = 0
bad = 0
linecount = 0
first = True
for x in dirlist :
    if first:
    #    print("x: " + x)
        x1 = x
        first = False
    else:
        x2 = x
        if len(x2) <= 0:
            first = True
            continue
        if checkpoints_equal(x1, x2):
            good = good + 1
            print(x1 + ' ' + x2 + ' True\n')
        else:
            bad = bad + 1

    linecount = linecount + 1
    if linecount % 10 == 0 :
        print('pair counter: ' + str(linecount))

print('good: ' + str(good) + ' bad: ' + str(bad)+'\n')
