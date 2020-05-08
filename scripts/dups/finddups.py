import os, sys
import argparse
import glob 

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--indir", required=True, type=str, help="input file")
args = parser.parse_args()


with open(args.indir) as inputf:
    dirlist = inputf.readlines()
dirlist = [x.strip() for x in dirlist]    

counter = 0
for x in dirlist :
    print "cur line " + x
    one, two = x.split('checkpoint-')
    print one, two
    mainname, rest = two.split('.ckpt')
    print mainname
    filename = 'checkpoint-' + mainname + '.ckpt'
    print filename
    retstr =  os.popen("find /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/grid-y4-y5 -name %s " % filename  ).read()
    print retstr 
