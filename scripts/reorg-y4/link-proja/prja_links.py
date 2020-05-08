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
    print "cur dir " + x
    fileIter = glob.iglob(os.path.join(x,'*/agn_ckpts/*.ckpt'))
    for f in fileIter :
       print "file: " + f
       a,b,c,d,e,g,h,i,j,k,visit,m,filename=f.split('/')
       print visit
       print filename
       retcode =  os.popen("mkdir -p /global/cfs/cdirs/lsst/production/DC2_ImSim/temp/Run2.2i/sim/y4-wfd-test/%s/agn_ckpts && ln -s %s /global/cfs/cdirs/lsst/production/DC2_ImSim/temp/Run2.2i/sim/y4-wfd/%s/agn_ckpts/%s " % (visit, f,visit,filename) ).read()
    
