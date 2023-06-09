from collections import namedtuple
from datetime import datetime
import uuid

from Back_order_prediction.config.configuration import Configuration
from Back_order_prediction.logger import logging
from Back_order_prediction.exception import CustomException
from threading import Thread
from typing import List

from multiprocessing import Process
from Back_order_prediction.entity.artifact_entity import DataIngestionArtifact
from Back_order_prediction.entity.artifact_entity import DataValidationArtifact , DataTransformationArtifact
from Back_order_prediction.components.data_ingestion import DataIngestion
from Back_order_prediction.components.data_validation import DataValidation
from Back_order_prediction.components.data_transformation import DataTransformation

import os, sys
from datetime import datetime
import pandas as pd


class Pipeline():
    def __init__(self,config:Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e,sys) from e
        


# data ingestion 

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys) from e


# data validataion


    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CustomException(e, sys) from e


# data transformation

    def start_data_transformation(self,
                                  data_ingestion_artifact:DataIngestionArtifact,
                                  data_validation_artifact:DataValidationArtifact)->DataTransformationArtifact:
        try:
            data_transformation= DataTransformation(
                data_transformation_config= self.config.get_data_transforamtion_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )

            return data_transformation.initiate_data_transformation()


        except Exception as e:
            raise CustomException(e, sys) from e


# pipeline

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                                                          data_validation_artifact=data_validation_artifact)

        except Exception as e:
            raise CustomException(e, sys) from e