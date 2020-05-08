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
    print "cur dir " + x + "\n"
    fileIter = glob.iglob(os.path.join(x,'*/fits/agn_ckpts/*.ckpt'))
    for f in fileIter :
       one, two, three, head, trunc_visit, raft = f.split('-')
       visit = trunc_visit.zfill(8)
       g,c,d,l,p,I,R,s,e,t,h,a,b,filename=f.split('/')
       print "file: " + f + " visit: " + visit + " filename: " + filename + "\n"
       retcode =  os.popen("mkdir -p /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/extract-y4-y5/%s/agn_ckpts && ln -s %s /global/cfs/cdirs/lsst/production/DC2_ImSim/Run2.2i/sim/extract-y4-y5/%s/agn_ckpts/%s " % (visit,f,visit,filename) ).read()
    
