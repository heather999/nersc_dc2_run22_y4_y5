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
    fileIter = glob.iglob(os.path.join(x,'*/*.tar')) 
    for f in fileIter :
        print("cur file " + f)
        #retcode =  os.popen("tar --list -f %s | grep -c 'verification OK'" % f).read()
        retcode =  os.popen("cd %s && tar xf %s |& tee $CSCRATCH/dc2-run2.2-y4y5/%s-%d-out " % (x,f,args.indir,counter) ).read()
        counter = counter + 1
        if counter % 100 == 0 :
            print("At file: " + str(counter))

    
