import os, sys
import argparse
import glob 

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--indir", required=True, type=str, help="input file")
args = parser.parse_args()

badFiles = open(args.indir+".txt", 'w')


with open(args.indir) as inputf:
    dirlist = inputf.readlines()
dirlist = [x.strip() for x in dirlist]    

counter = 0
for x in dirlist :
    fileIter = glob.iglob(os.path.join(x,'*.tar')) 
    for f in fileIter :
        print("cur file " + f)
        #retcode =  os.popen("tar --list -f %s | grep -c 'verification OK'" % f).read()
        retcode =  os.popen("cd %s && tar --list -f %s |& tee $CSCRATCH/dc2-run2.2-y4y5/%d-out " % (x,f,counter) ).read()
#        if int(retcode) != 1 :
#            print("Found bad " + f)
#            badFiles.write(f+"\n")
        counter = counter + 1
        if counter % 100 == 0 :
            print("At file: " + str(counter))

    
badFiles.close() 
