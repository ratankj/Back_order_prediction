import yaml,sys
import numpy as np
import os, sys
import numpy as np
import dill
import pandas as pd
from Back_order_prediction.constant import *
from Back_order_prediction.exception import CustomException


def write_yaml_file(file_path:str,data:dict=None):
    """
    Create yaml file 
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise CustomException(e,sys)


def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys) from e
    
    #yaml.safe_load() method takes a file object, reads its contents, and then deserializes them into a Python object.


def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CustomException(e, sys) from e


def save_object(file_path: str, obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) from e





def load_data(file_path:str , schema_file_path:str)->pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        dataframe=pd.read_csv(file_path)

        error_message = ""
        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])

            else:
                error_message= f"{error_message} columns [{column}] is not in the schema"

        if len(error_message)>0:
            raise Exception(error_message)
        
        return dataframe

    except Exception as e:
        raise CustomException(e,sys) from e

