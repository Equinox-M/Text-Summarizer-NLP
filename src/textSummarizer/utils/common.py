import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any

# @ensure_annotated is basically to enforce the type indicated by annotations when passing an argument that is not what was indicated to the function   
@ensure_annotation
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object
    Args:
        path_to_yaml (Path): path to the yaml file
    Raises:
        ValueError: if the yaml file is empty
        e: empty yaml file
    Returns:
        ConfigBox: a ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotation
def create_directories(path_to_directories: list, verbose=True):
    """ Create list of directories

    Args:
        path_to_directories (list): list path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults to false
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotation
def get_size(path: Path) -> str:
    """ Get the size of a file

    Args:
        path (Path): path to the file
    Returns:
        str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"