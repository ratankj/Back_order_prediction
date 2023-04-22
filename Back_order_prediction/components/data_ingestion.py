import os,sys
from six.moves import urllib  
from Back_order_prediction.logger import logging
from Back_order_prediction.exception import CustomException

from Back_order_prediction.constant import *

from Back_order_prediction.utils.utils import read_yaml_file

from Back_order_prediction.entity.config_entity import DataIngestionConfig

from Back_order_prediction.entity.artifact_entity import DataIngestionArtifact

from Back_order_prediction.config.configuration import Configuration

from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split





class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig): # from entity/config_entity
        try:
            logging.info(f"{'>>'*30}Data Ingestion log started.{'<<'*30} \n\n")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys) from e
        


    def download_data(self) ->str:

            try:
                download_url = self.data_ingestion_config.dataset_download_url  #download data
               
                raw_data_dir=self.data_ingestion_config.raw_data_dir
               

                 # if not available then make a folder raw_data_dir  and is available then exis_ok =TRUE
                os.makedirs(raw_data_dir,exist_ok=True) 

                #after download the dataset we hae to call the base name
                # 'https://example.com/files/back_order.csv' -- the base name is -  back_order.csv

                back_order_file_name=os.path.basename(download_url)

                raw_file_path=os.path.join(raw_data_dir,back_order_file_name)

                logging.info(f"Downloading file from :[{download_url}] into :[{raw_file_path}]")
                

                #here the file located at download_url will be downloaded and saved to raw_file_path
                #it is a Python function that is used to download a file from a URL and save it to a local file path.
                urllib.request.urlretrieve(download_url, raw_file_path)
                
                logging.info(
                    f"File :[{raw_file_path}] has been downloaded successfully.")
                
                
                return raw_file_path

            except Exception as e:
                raise CustomException(e,sys) from e  
            


    def split_data_as_train_test(self) -> DataIngestionArtifact:


            try:
                raw_data_dir=self.data_ingestion_config.raw_data_dir

                #s a Python function that returns a list of all the files and directories in the directory specified by raw_data_dir.
                file_name = os.listdir(raw_data_dir)[0]

                back_order_file_path = os.path.join(raw_data_dir,file_name)

                logging.info(f"Reading csv file: [{back_order_file_path}]")

                # when we run data_ingestion it will store with date time
                today_date = date.today()
                current_year=today_date.year

                back_order_dataframe = pd.read_csv(back_order_file_path)

                # dropping sku column
                back_order_dataframe.drop(["sku"],axis=1,inplace=True) 

                #replace yes with 1 and no with 0 in went_on_backorder column
                back_order_dataframe["went_on_backorder"] = np.where(back_order_dataframe["went_on_backorder"] == 'Yes', 1,0)

                logging.info(f"splitting data into train and test data")

                train_set = None
                test_set = None

                # train test split
                train_set,test_set = train_test_split(back_order_dataframe,test_size = 0.3,random_state=42)

                train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)

                test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

                logging.info(f"Training file path : [{train_file_path}]")
                logging.info(f"Testing file path : [{test_file_path}]")
# 
# *****************************%%%%%%%%%%%%%%%%%%%%**********************************************************

                if train_set is not None:
                    os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                    logging.info(f"Exporting training dataset to file: [{train_file_path}]")
                    train_set.to_csv(train_file_path, index=False)


                if test_set is not None:
                    os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok= True)
                    logging.info(f"Exporting training dataset to file: [{test_file_path}]")
                    test_set.to_csv(test_file_path,index =False)


                data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,
                                                          test_file_path=test_file_path,
                                                          is_ingested=True,
                                                          message=f"data ingestion completed successfully"
                                                          )
                logging.info(f"Data Ingestion Artifact:[{data_ingestion_artifact}]")
                return data_ingestion_artifact

            except Exception as e:
                raise CustomException(e,sys) from e
        


    def initiate_data_ingestion(self):
        try:
            raw_file_path = self.download_data()
            return self.split_data_as_train_test()


        except Exception as e:
            raise CustomException(e,sys) from e
        
        




