#!/bin/bash

#PBS -j oe             # Combine output and error.
#PBS -o output/job.log # Output file.
#PBS -q default        # Queue name.
#PBS -N FeSurf         # Job name.
#PBS -l nodes=1:ppn=64 # Resources required.

MPIRUN="/opt/openmpi-intel/bin/mpirun" # For Asathor.

NPROCS=$(wc -l < ${PBS_NODEFILE})
cd $PBS_O_WORKDIR

${MPIRUN} -np ${NPROCS} lmp_mpi            \
          -in           surfin100.lmp         \
          -log          output/lammps.log  \
          -screen       none               \
          -var          RANDOM ${RANDOM} 
