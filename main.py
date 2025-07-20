from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        logging.info("Enter the try block")
        trainingpipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainingpipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise CustomException(e,sys)