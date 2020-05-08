#!/bin/sh

export STACKCVMFS=/cvmfs/sw.lsst.eu/linux-x86_64
export LSST_STACK_VERSION=w_2019_42

module unload python
module swap PrgEnv-intel PrgEnv-gnu
module swap gcc gcc/6.3.0
module rm craype-network-aries
module rm cray-libsci
module unload craype
export CC=gcc

#source $STACKCVMFS/$LSST_STACK_VERSION/loadLSST.bash


# Use the /cvmfs distrubtion from IN2P3
LSST_DISTRIB=$STACKCVMFS/lsst_distrib/$LSST_STACK_VERSION
LSST_SIMS=$STACKCVMFS/lsst_sims/sims_$LSST_STACK_VERSION

EUPS_DIR="${LSST_DISTRIB}/eups/current"
source "${LSST_DISTRIB}/loadLSST.bash"

# Tell eups to also use the packages in lsst_sims on top of lsst_distrib
EUPS_PATH=$EUPS_PATH:"${LSST_SIMS}/stack/current"

#setup lsst_distrib
#setup -r $LOCALDIR/obs_lsst -j
#setup -r $LOCALDIR/pipe_tasks -j

echo Now setup any necessary stack packages such as: setup -t w_2019_19 lsst_distrib or setup -t sims_w_2019_19 lsst_sims

export OMP_NUM_THREADS=1

