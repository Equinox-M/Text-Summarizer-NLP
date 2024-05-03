import os  # Module for interacting with the operating system
import urllib.request as request  # Module for downloading files from URLs
import zipfile  # Module for handling zip files
from src.textSummarizer.logging import logger  # Importing logger for logging messages
from src.textSummarizer.utils.common import get_size  # Importing utility function for getting file size
from src.textSummarizer.entity import DataIngestionConfig  # Importing data ingestion configuration class
from pathlib import Path  # Module for representing file paths

class DataIngestion:
    """
    Class responsible for handling data ingestion tasks.
    """
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion object with the provided configuration.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the data file from the specified URL if it does not already exist locally.
        """
        if not os.path.exists(self.config.local_data_file):
            # Download the file from the source URL
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info:\n{headers}")
        else:
            logger.info(f"{get_size(Path(self.config.local_data_file))} already exists")

    def extract_zip_file(self):
        """
        Extracts the contents of the zip file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
