from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataTransformationConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
import sys

if __name__ == "__main__":
    try:
        logging.info("Enter the try block")
        trainingpipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainingpipeline_config)
        data_validation_config = DataValidationConfig(trainingpipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)
        data_validation = DataValidation(dataingestionartifact,data_validation_config=data_validation_config)
        logging.info("Initaite data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed!!")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipeline_config)
        logging.info("Data transformatio started")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed!!")

    except Exception as e:
        raise CustomException(e,sys)