import os
from datetime import datetime

def get_currect_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


CURRENT_TIME_STAMP =  get_currect_time_stamp()


# TO GET CURRENT WORKING DIRECTORY
ROOT_DIR = os.getcwd()

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)



# DATA INGESTION REALATED VARIABLE

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATASET_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_INGESTED_DIR_NAME_KEY ="ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY ="ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY="ingested_test_dir"


# DATA PIPELINE REALTED VARIABLE
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPLELINE_NAME_KEY="pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
