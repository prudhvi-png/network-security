import sys
import os
import numpy as np
import pandas as pd  
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS


from networksecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact
)
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging

from networksecurity.utils.main_utils.utils import save_numpy_array
from networksecurity.utils.main_utils.utils import save_object


class DataTransformation:
    def __init__(self,data_validtion_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validtion_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise CustomException(e,sys)
    
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path) ## With static method we can this class directly with out using object
        except Exception as e:
            raise CustomException(e,sys)

    def get_data_transformer_obj(cls)->Pipeline:
        '''
        it inistailizes a KNNImputer objet with the parameters sepecified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step

        Args:
        cls: DataTransformation

        Returns:
        A Pipeline object
        '''
        logging.info("Entered the get_data_tranformer_object method of transformation class")
        try:
            imputer:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"initialize KNNImputer wwith {DATA_TRANSFORMATION_IMPUTER_PARAMS}")

            processor:Pipeline=Pipeline([("Inputer",imputer)])
            return processor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("Entered initiate_data_transformation method")
        try:
            logging.info("Started data transformation")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            ## training dataframe
            input_feature_train_df = train_df.drop(columns=TARGET_COLUMN,axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)
            
            #testing data frame
            input_feature_test_df = test_df.drop(columns=TARGET_COLUMN,axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)

            preprocessor = self.get_data_transformer_obj()
            preprocessor_obj = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_obj.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            save_object(self.data_transformation_config.transformed_obj_file_path,preprocessor_obj)
            save_numpy_array(self.data_transformation_config.transformed_train_file_path,array=train_arr,)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,array=test_arr)

            #preperaing artifacts
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_obj_file_path,
                transfromed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e,sys)