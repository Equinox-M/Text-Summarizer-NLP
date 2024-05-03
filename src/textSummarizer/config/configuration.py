from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """
        Initialize ConfigurationManager with file paths for config and params.

        Args:
            config_filepath (str): Path to the configuration YAML file.
            params_filepath (str): Path to the parameters YAML file.
        """
        # Read YAML files and create directories
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieve data ingestion configuration.

        Returns:
            DataIngestionConfig: Configuration for data ingestion stage.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        # Create DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieve data validation configuration.

        Returns:
            DataValidationConfig: Configuration for data validation stage.
        """
        config = self.config.data_validation
        create_directories([config.root_dir])

        # Create DataValidationConfig object
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Retrieve data transformation configuration.

        Returns:
            DataTransformationConfig: Configuration for data transformation stage.
        """
        config = self.config.data_transformation
        create_directories([config.root_dir])

        # Create DataTransformationConfig object
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_file=config.data_file,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        """
        Retrieve model training configuration.

        Returns:
            ModelTrainingConfig: Configuration for model training stage.
        """
        config = self.config.model_training
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        # Create ModelTrainingConfig object
        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.evaluation_strategy,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )

        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Retrieve model evaluation configuration.

        Returns:
            ModelEvaluationConfig: Configuration for model evaluation stage.
        """
        config = self.config.model_evaluation
        create_directories([config.root_dir])

        # Create ModelEvaluationConfig object
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name
        )

        return model_evaluation_config
