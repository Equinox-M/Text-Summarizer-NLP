from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_4_model_training import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_5_model_evaluation import DataEvaluationTrainingPipeline

# Define stage names for logging
STAGE_NAME = 'Data Ingestion Stage'
try:
    # Data Ingestion Stage
    logger.info(f">>>>> Stage {STAGE_NAME} Started >>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed >>>>>")

except Exception as e:
    # Log exception if any and raise
    logger.exception(e)
    raise e

# Data Validation Stage
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

# Data Transformation Stage
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

# Model Training Stage
STAGE_NAME = "Model Training stage"
try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Model Evaluation Stage
STAGE_NAME = "Model Evaluation stage"
try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = DataEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
