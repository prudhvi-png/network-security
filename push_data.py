import os 
import sys 
import json

from dotenv import load_dotenv
import certifi

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca = certifi.where()

import pandas as pd    
import numpy as np
import pymongo
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging

'''Pushing the data into database as list of json values'''

class NetworkDataExtrack():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())## converting the records into list of json
            return records
        except Exception as e:
            raise CustomException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collcetion = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collcetion = self.database[self.collcetion]
            self.collcetion.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH = "network_data\phisingData.csv"
    DATABASE = "prudhviredrouth143"
    collection = "networkdata"
    network_obj = NetworkDataExtrack()
    records = network_obj.csv_to_json_converter(FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)