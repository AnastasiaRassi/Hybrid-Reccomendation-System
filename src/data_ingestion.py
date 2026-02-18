import os
import pandas as pd
import boto3
from dotenv import load_dotenv
from loguru import logger
from utils.custom_exception import CustomException
from utils.general_utils import load_config
from config.paths_config import *

load_dotenv()

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info("Data Ingestion Started....")

    def download_csv_from_s3(self):
        try:
            s3 = boto3.client("s3")

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR, file_name)

                if file_name == "animelist.csv":

                    obj = s3.get_object(Bucket=self.bucket_name, Key=file_name)
                    data = pd.read_csv(obj['Body'], nrows=5_000_000)
                    data.to_csv(file_path, index=False)
                    logger.info("Large file detected. Only downloading 5M rows.")

                else:
                    s3.download_file(self.bucket_name, file_name, file_path)
                    logger.info(f"Downloaded file: {file_name}")

        except Exception as e:
            logger.error("Error while downloading data from S3")
            raise CustomException("Failed to download data", e)

    def run(self):
        try:
            logger.info("Starting Data Ingestion Process....")
            self.download_csv_from_s3()
            logger.info("Data Ingestion Completed...")
        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
        finally:
            logger.info("Data Ingestion DONE...")


if __name__ == "__main__":
    config = load_config(CONFIG_PATH)
    obj = DataIngestion(config)
    obj.run()
