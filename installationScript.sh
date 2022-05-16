#!/bin/sh

# Install required libraries
sudo apt-get -y update
sudo apt-get -y install gcc
sudo apt-get -y install make
sudo apt-get -y install libbz2-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install libncurses5-dev
sudo apt-get -y install libncursesw5-dev
sudo apt-get -y install liblzma-dev

# Install Miniconda
mkdir ~/downloads
cd ~/downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/Miniconda3
eval "$(/home/ubuntu/Miniconda3/bin/conda shell.bash hook)"
conda init

# Install Pangolin
cd ~/repos
git clone https://github.com/cov-lineages/pangolin 
cd pangolin
conda env create -f environment.yml
conda activate pangolin
pip install .

# Install minimap 2
conda activate pangolin
cd ~/repos
git clone https://github.com/lh3/minimap2
cd minimap2
make

# Install Nextflow
conda activate pangolin
conda config --add channels bioconda
conda install -y nextflow=21.10.6

# Copy the resources
sudo mkdir ~/resources
sudo cp ~/repos/ncov2019-artic-nf/scripts/MN908947.fa ~/resources/

sudo mkdir ~/nextflowCache

