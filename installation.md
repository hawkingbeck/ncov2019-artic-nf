## Step 1. Install Anacaonda

mkdir downloads
cd downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh


## Step 2. Install Pangolin Conda Environment

https://github.com/cov-lineages/pangolin 

git clone https://github.com/cov-lineages/pangolin 
cd pangolin
conda env create -f environment.yml
conda activate pangolin
pip install .


## Step 3. Install Nextflow
cd ..
sudo apt-get update
sudo apt install default-jre
wget -qO- https://get.nextflow.io | bash
chmod +x nextflow
sudo mv nextflow /usr/bin/


## Step 4. Install SamTools
sudo apt-get update
sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install libbz2-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libncurses5-dev 
sudo apt-get install libncursesw5-dev
sudo apt-get install liblzma-dev

### Install htslib
cd /usr/bin
sudo wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
sudo tar -vxjf htslib-1.9.tar.bz2
sudo rm htslib-1.9.tar.bz2
cd htslib-1.9
sudo make

### Install sam tools
cd ..
sudo wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
sudo tar -vxjf samtools-1.9.tar.bz2
sudo rm samtools-1.9.tar.bz2
cd samtools-1.9
sudo make

### Install BCF Tools
cd ..
sudo wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
sudo tar -vxjf bcftools-1.9.tar.bz2
sudo rm bcftools-1.9.tar.bz2
cd bcftools-1.9
sudo make

## Add items to path and reload profile to enable
cd ~/
export PATH="$PATH:/usr/bin/bcftools-1.9"
export PATH="$PATH:/usr/bin/samtools-1.9"
export PATH="$PATH:/usr/bin/htslib-1.9"
source ~/.profile

## Clone Nextflow pipeline repo
cd ~/
mkdir repos
cd repos
git clone https://github.com/hawkingbeck/ncov2019-artic-nf