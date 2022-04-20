# Run Pipeline Example

For test data, run the below
````
export INPUT_DIR=/home/ubuntu/testData/PGIM21-R001
export OUTPUT_DIR=/home/ubuntu/testData/PGIM21-R001/output

nextflow run main.nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR

nextflow run ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR
nextflow run connor-lab/ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR
nextflow run hawkingbeck/ncov2019-artic-nf -profile conda --cache /home/ubuntu/articCondaEnv --illumina --prefix "output" --directory $INPUT_DIR --outdir $OUTPUT_DIR
````


INEI100603_S15_L001
INEI099528_S7_L001