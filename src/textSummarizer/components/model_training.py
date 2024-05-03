from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
from src.textSummarizer.entity import ModelTrainingConfig
import os

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        """
        Initializes the ModelTraining object with the provided configuration.
        """
        self.config = config

    def train(self):
        """
        Performs model training.
        """
        # Determine device for training
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        
        # Prepare data collator
        data_collector = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load training data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Define training arguments
        training_args = TrainingArguments(
            output_dir=self.config.root_dir, 
            num_train_epochs=1, 
            warmup_steps=500,
            per_device_train_batch_size=1, 
            per_device_eval_batch_size=1,
            weight_decay=0.01, 
            logging_steps=100,
            evaluation_strategy='steps', 
            eval_steps=1000, 
            save_steps=5000,
            gradient_accumulation_steps=1
        ) 

        # Initialize Trainer object
        trainer = Trainer(model=model_pegasus, 
                          args=training_args,
                          tokenizer=tokenizer, 
                          data_collator=data_collector,
                          train_dataset=dataset_samsum_pt["test"], 
                          eval_dataset=dataset_samsum_pt["validation"])
        
        # Train the model
        trainer.train()

        # Save trained model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
