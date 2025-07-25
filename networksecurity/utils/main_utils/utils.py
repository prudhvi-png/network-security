import yaml
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys) from e
    

def write_yml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    except Exception as e:
        raise CustomException(e,sys)
    
def save_numpy_array(file_path:str,array:np.array):
    '''
    save numpy array data to file
    file_path:str location of the file to save
    array: np.array data to save
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj,array)
        logging.info("Saved the array")
    except Exception as e:
        raise CustomException(e,sys) from e
    
def save_object(file_path:str,obj)->None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise CustomException(e,sys) from e