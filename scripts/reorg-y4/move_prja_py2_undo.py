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
       retcode =  os.popen("unlink /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/extract-y4-y5/%s/agn_ckpts/%s && ln -s %s /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/extract-y4-y5/%s/agn_ckpts/%s " % (visit,filename,f,visit,filename) ).read()
    
