
## Step 1. Clone the repo
mkdir ~/repos
cd ~/repos
git clone https://github.com/hawkingbeck/ncov2019-artic-nf
cd ncov2019-artic-nf


## Step 1. Install prerequsistes

sudo apt-get -y update
sudo apt-get -y install gcc
sudo apt-get -y install make
sudo apt-get -y install libbz2-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install libncurses5-dev
sudo apt-get -y install libncursesw5-dev
sudo apt-get -y install liblzma-dev

## Step 2. Install Anacaonda

mkdir ~/downloads
cd ~/downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/Miniconda3
source ~/.profile

## Step 3. Install Pangolin Conda Environment

https://github.com/cov-lineages/pangolin 
mkdir ~/repos
cd ~/repos
git clone https://github.com/cov-lineages/pangolin 
cd pangolin
conda env create -f environment.yml
conda activate pangolin
pip install .

## Step 4. Install Minimap2
conda activate pangolin
cd ~/
mkdir repos
cd repos
git clone https://github.com/lh3/minimap2
cd minimap2
make

## Step 5. Install Nextflow
conda config --add channels bioconda
conda install nextflow=21.10.6

## Clone Nextflow pipeline repo
cd ~/repos
git clone https://github.com/hawkingbeck/ncov2019-artic-nf
cd ncov2019-artic-nf

## Step 7. Install basespace
<!-- mkdir ~/bin
wget "https://launch.basespace.illumina.com/CLI/latest/amd64-linux/bs" -O $HOME/bin/bs
chmod u+x $HOME/bin/bs
bs --help -->

# Step 6. Copy Resources
mkdir ~/resources
cp ~/repos/ncov2019-artic-nf/scripts/MN908947.fa ~/resources/

## Run the pipeline
mkdir ~/nextflowCache
export INPUT_DIR=/home/ubuntu/testData/PGIM21-R001
export OUTPUT_DIR=/home/ubuntu/testData/PGIM21-R001/output

cd ~/

nextflow run /home/ubuntu/repos/ncov2019-artic-nf/main.nf -profile conda --illumina --prefix "output" --cache=nextflowCache --directory $INPUT_DIR --outdir $OUTPUT_DIR 


<!-- cd ~/downloads
sudo apt-get update
sudo apt install default-jre
v21.10.6
https://github.com/nextflow-io/nextflow
git clone https://github.com/nextflow-io/nextflow.git --branch v21.10.6
wget -qO- https://get.nextflow.io | bash
chmod +x nextflow
sudo mv nextflow /usr/bin/
sudo chown -hR ubuntu /usr/bin/nextflow -->


<!-- ## Step 4. Install SamTools
sudo apt-get update
sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install libbz2-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libncurses5-dev 
sudo apt-get install libncursesw5-dev
sudo apt-get install liblzma-dev -->

<!-- ### Install htslib
cd /usr/bin
sudo wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
sudo tar -vxjf htslib-1.9.tar.bz2
sudo rm htslib-1.9.tar.bz2
cd htslib-1.9
sudo make -->

<!-- ### Install sam tools
cd ..
sudo wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
sudo tar -vxjf samtools-1.9.tar.bz2
sudo rm samtools-1.9.tar.bz2
cd samtools-1.9
sudo make -->

<!-- ### Install BCF Tools
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
source ~/.profile -->

<!-- ## Install Trim-galore
conda install -c bioconda trim-galore -->
<!-- cd ~/repos
git clone https://github.com/FelixKrueger/TrimGalore.git --branch 0.6.5
cd TrimGalore
sudo mkdir /usr/bin/TrimGalore
sudo cp trim_galore /usr/bin/TrimGalore
export PATH="$PATH:/usr/bin/TrimGalore"
source ~/.profile -->

<!-- ## Install docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker -->

