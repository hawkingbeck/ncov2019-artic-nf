
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