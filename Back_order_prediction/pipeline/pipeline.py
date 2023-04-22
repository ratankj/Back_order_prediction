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

from Back_order_prediction.components.data_ingestion import DataIngestion
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


# pipeline

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys) from e