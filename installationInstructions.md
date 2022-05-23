
## Step 1. Clone the repo
mkdir ~/repos
cd ~/repos
git clone https://github.com/hawkingbeck/ncov2019-artic-nf
cd ncov2019-artic-nf

## Step 2. Run the installation script and activate conda
source ./installationScript.sh

## Run the pipeline
export INPUT_DIR=/home/ubuntu/testData/PGIM21-R001
export OUTPUT_DIR=/home/ubuntu/testData/PGIM21-R001/output

cd ~/

nextflow run /home/ubuntu/repos/ncov2019-artic-nf/main.nf -profile conda --illumina --prefix "output" --cache=nextflowCache --directory $INPUT_DIR --outdir $OUTPUT_DIR

# Installation on VirtualBox

In some instances users may wish to install this tool chain on a VM running locally, for example a laptop. To do this VirtualBox is recommended and can be installed by following the instructions here: https://www.virtualbox.org/wiki/Downloads

The pipeline is tested on Ubuntu 18.04.6 LTS (Bionic Beaver) for which, Virtual Box installation instructions can be found here: https://www.toptechskills.com/linux-tutorials-courses/how-to-install-ubuntu-1804-bionic-virtualbox/  

