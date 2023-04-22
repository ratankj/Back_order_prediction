from Back_order_prediction.exception import CustomException
from Back_order_prediction.logger import logging
from Back_order_prediction.config.configuration import Configuration
from Back_order_prediction.components.data_ingestion import DataIngestion
import os
from Back_order_prediction.pipeline.pipeline import Pipeline


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
            logging.error(f"{e}")
            print(e)


if __name__ == "__main__":
     main()



