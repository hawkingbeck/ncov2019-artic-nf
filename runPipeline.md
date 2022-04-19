# Run Pipeline Example

For test data, run the below
````
export INPUT_DIR=/home/ubuntu/testData/PGIM21-R001
export OUTPUT_DIR=/home/ubuntu/testData/PGIM21-R001/output
nextflow run ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR

nextflow run connor-lab/ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR
nextflow run hawkingbeck/ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR
````