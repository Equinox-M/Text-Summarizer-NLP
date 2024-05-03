import os  # Module for interacting with the operating system
from src.textSummarizer.logging import logger  # Importing logger for logging messages
from transformers import AutoTokenizer  # Importing AutoTokenizer for tokenization
from datasets import load_dataset, load_from_disk  # Importing functions for loading datasets
from src.textSummarizer.entity import DataTransformationConfig  # Importing data transformation configuration class
from pathlib import Path  # Module for representing file paths

class DataTransformation:
    """
    Class responsible for data transformation tasks.
    """
    def __init__(self, config: DataTransformationConfig):
        """
        Initializes the DataTransformation object with the provided configuration.
        """
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)  # Initializing the tokenizer

    def convert_examples_to_features(self, example_batch):
        """
        Converts examples to features suitable for model input.
        Args:
            example_batch (dict): Batch of examples containing 'dialogue' and 'summary' keys.
        Returns:
            dict: Dictionary containing input_ids, attention_mask, and labels.
        """
        # Tokenize input dialogue
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        # Tokenize target summary
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
            
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        """
        Converts the dataset to PyTorch format and saves it to disk.
        """
        # Load dataset
        dataset_samsum = load_from_disk(self.config.data_file)
        
        # Map examples to features and save to disk
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
