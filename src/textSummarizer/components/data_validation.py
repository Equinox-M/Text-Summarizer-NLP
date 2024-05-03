import os  # Module for interacting with the operating system
from src.textSummarizer.logging import logger  # Importing logger for logging messages
from src.textSummarizer.entity import DataValidationConfig  # Importing data validation configuration class
from pathlib import Path  # Module for representing file paths

class DataValidation:
    """
    Class responsible for data validation tasks.
    """
    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation object with the provided configuration.
        """
        self.config = config

    def validate_all_files_exist(self) -> bool:
        """
        Validates if all required files exist in the specified directory.
        Returns:
            bool: True if all files exist, False otherwise.
        """
        try:
            validation_status = None  # Variable to store the validation status
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "summarizer-data", "samsum_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e
