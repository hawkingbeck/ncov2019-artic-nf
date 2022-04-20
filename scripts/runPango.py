import os
import subprocess
from subprocess import call
import sys
import shutil
import pandas as pd
import argparse
from argparse import ArgumentParser
import numpy as np
from datetime import datetime
from decimal import Decimal

def main(fasta_filename, results_filename):

  usherOutputFilePath = f"{os.path.splitext(results_filename)[0]}_usher.csv"
  pLearnOutputFilePath = f"{os.path.splitext(results_filename)[0]}_pLearn.csv"
  command = f"pangolin --verbose --usher {fasta_filename} --outfile {usherOutputFilePath}"

  call(command, shell=True)

  usherLineageDf = pd.read_csv(usherOutputFilePath)

  command = f"pangolin --verbose {fasta_filename} --outfile {pLearnOutputFilePath}"
  
  call(command, shell=True)
    
  pLearnLineageDf = pd.read_csv(pLearnOutputFilePath)

  resultDict = {
    'alignedFile': os.path.basename(fasta_filename),
    'alignedFilePath': fasta_filename,
    'lineage': list(pLearnLineageDf['lineage'])[0], 
    'usherLineage': list(usherLineageDf['lineage'])[0],
    'conflict': list(pLearnLineageDf['conflict'])[0], 
    'ambiguity_score': list(pLearnLineageDf['ambiguity_score'])[0],
    'version': list(pLearnLineageDf['version'])[0],
    'pangolin_version': list(pLearnLineageDf['pangolin_version'])[0],
    'pangoLEARN_version': list(pLearnLineageDf['pangoLEARN_version'])[0],
    'pango_version': list(pLearnLineageDf['pango_version'])[0],
    'note': list(pLearnLineageDf['note'])[0],
    'scorpio_call': list(pLearnLineageDf['scorpio_call'])[0],
    'scorpio_support': list(pLearnLineageDf['scorpio_support'])[0],
    'scorpio_conflict': list(pLearnLineageDf['scorpio_conflict'])[0]
    }

  resultsDf = pd.DataFrame(resultDict, index=[0])
  resultsDf.to_csv(results_filename, index=False)

  os.remove(usherOutputFilePath)
  os.remove(pLearnOutputFilePath)
  
if __name__ == "__main__":
    parser = ArgumentParser(description='Genotype an aligned sequence on specified variants of interest')
    parser.add_argument('--fasta_filename', help="Single sample fasta, wuhan aligned")
    parser.add_argument('--results_filename', help="filename to store the results into")

    args = parser.parse_args()

    main(args.fasta_filename, args.results_filename)
