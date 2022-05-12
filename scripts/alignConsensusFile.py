import argparse
import os
import subprocess
import sys
import shutil
import pandas as pd
import argparse
import numpy as np
import json
from datetime import datetime
from decimal import Decimal
import difflib
# from Bio import SeqIO
# import pysam

def alignFasta(refFastaFilePath, consensusFilepath, alignedFastaFilepath, trimStart, trimEnd):
  ##############################################
  # Step 1. Run Minimap
  ##############################################
  mappedFastapath = f"{consensusFilepath}.mapped"
  subprocess.run(
    "minimap2 -t minimap2_threads -a -x asm5 {} {} > {}".format(
        refFastaFilePath, consensusFilepath, mappedFastapath
      ),
      check=True,
      shell=True,
      stdout=subprocess.DEVNULL, 
      stderr=subprocess.STDOUT
   )
  ##############################################
  # Step 2. 
  ##############################################
  # samfile = pysam.AlignmentFile(mappedSamFastaFilePath, 'r')
  # reference = SeqIO.read(refFastaFilePath, 'fasta')

  goFastaCommand = f"gofasta sam toMultiAlign --samfile {mappedFastapath} --trim --pad --trimstart {trimStart} --trimend {trimEnd} -o {alignedFastaFilepath}"
  subprocess.run(
    goFastaCommand,
    check=True,
    shell=True,
    stdout=subprocess.DEVNULL, 
    stderr=subprocess.STDOUT
  )

  os.remove(mappedFastapath)



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Align the fasta file')
  parser.add_argument('--consensusFastaFilePath', dest='consensusFastaFilePath', type=str, help='input consensus fasta file path')
  parser.add_argument('--alignedFastaFilepath', dest='alignedFastaFilepath', help='output file for the aligned fasta')
  args = parser.parse_args()
  alignFasta("/home/ubuntu/resources/MN908947.fa", args.consensusFastaFilePath, args.alignedFastaFilepath, 265, 29674)

