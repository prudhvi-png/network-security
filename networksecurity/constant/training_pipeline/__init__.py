import os
import sys
import numpy as np
import pandas as ps  


'''
defining common constant variable for training pipeline

'''
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "networksecurity"
ARTIFACT_DIR:str = 'Artifacts'
FILE_NAME:str = 'phishingData.csv'

TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str = 'test.csv'
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessor.pkl"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yml")


'''
Data Ingestion related constant start with DATA_INGESTION var Name

'''

DATA_INGESTION_COLLECTION_NAME:str = "networkdata"  ## Collection name in database
DATA_INGESTION_DATABASE_NAME:str = "prudhviredrouth143" ## My data base name
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATIO:float=0.2


'''Data validation related constant start with DATA_VALIDATION VAR NAME'''

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yml"

'''Data transformation related constant start with DATA_TRANSFORMATION VAR NAME'''

DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"


## Knn Imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values" : np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}