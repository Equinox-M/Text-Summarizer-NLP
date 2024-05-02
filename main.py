from src.textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started >>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed >>>>>")

except Exception as e:
    logger.exception(e)
    raise e
