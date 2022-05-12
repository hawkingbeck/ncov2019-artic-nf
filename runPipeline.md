# Run Pipeline Example

For test data, run the below
````
export INPUT_DIR=/home/ubuntu/testData/PGIM21-R001
export OUTPUT_DIR=/home/ubuntu/testData/PGIM21-R001/output

nextflow run main.nf -profile conda --cache ~/nextflowCache  --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR 


nextflow run main.nf --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR -profile conda

https://github.com/hawkingbeck/ncov2019-artic-nf
````