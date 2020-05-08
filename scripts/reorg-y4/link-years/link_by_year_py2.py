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
    print "cur visit " + x
    retcode =  os.popen("ln -s /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/extract-y4-y5/%s /global/cfs/cdirs/lsst/production/DC2_ImSim/temp/Run2.2i/sim/y5-wfd/%s" % (x, x) ).read()
    
