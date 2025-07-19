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


'''
Data Ingestion related constant start with DATA_INGESTION var Name

'''

DATA_INGESTION_COLLECTION_NAME:str = "networkdata"  ## Collection name in database
DATA_INGESTION_DATABASE_NAME:str = "prudhviredrouth143" ## My data base name
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATIO:float=0.2