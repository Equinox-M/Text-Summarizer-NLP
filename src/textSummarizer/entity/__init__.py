from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion stage.
    """
    root_dir: Path  # Root directory for storing ingested data
    source_URL: str  # URL from which data is fetched
    local_data_file: Path  # Local file path where fetched data is stored
    unzip_dir: Path  # Directory where the fetched data is extracted (if compressed)

@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration class for data validation stage.
    """
    root_dir: Path  # Root directory for storing validation results
    STATUS_FILE: str  # File containing status information
    ALL_REQUIRED_FILES: list  # List of required files for validation

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration class for data transformation stage.
    """
    root_dir: Path  # Root directory for storing transformed data
    data_file: Path  # File path of the data to be transformed
    tokenizer_name: Path  # File path of the tokenizer used for transformation

@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Configuration class for model training stage.
    """
    root_dir: Path  # Root directory for storing model training artifacts
    data_path: Path  # Path to the training data
    model_ckpt: Path  # Path to the model checkpoint
    num_train_epochs: int  # Number of training epochs
    warmup_steps: int  # Number of warmup steps
    per_device_train_batch_size: int  # Batch size per device for training
    weight_decay: float  # Weight decay parameter for training
    logging_steps: int  # Frequency of logging training metrics
    evaluation_strategy: str  # Strategy for evaluation during training
    eval_steps: int  # Frequency of evaluation during training
    save_steps: float  # Frequency of saving model checkpoints during training
    gradient_accumulation_steps: int  # Number of gradient accumulation steps

@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Configuration class for model evaluation stage.
    """
    root_dir: Path  # Root directory for storing evaluation results
    data_path: Path  # Path to the evaluation data
    model_path: Path  # Path to the trained model
    tokenizer_path: Path  # Path to the tokenizer used for evaluation
    metric_file_name: Path  # File name to store evaluation metrics
