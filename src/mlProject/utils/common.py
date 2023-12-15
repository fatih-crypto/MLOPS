import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations

def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Yaml dosyasini yüklemeyi sağlar
    
    
    """
    
    
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"{path_to_yaml} loaded succsesful")
            return ConfigBox
    except BoxValueError :
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 
    

@ensure_annotations

def create_directories(path_to_directories:list,verbose = True):
    
    """Path oluşturur"""
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")



@ensure_annotations

def save_json(path: Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at:{path}")


@ensure_annotations

def load_json(path:Path) -> ConfigBox:
    with opne(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully {path}")

@ensure_annotations

def save_bin(data: Any,path:Path):
    """Saved binary file
    
    Args: data(Any): path table saved as bin 

    path: path to bin file
    """
    joblib.dump( value = data, filename  = path)
    logger.info(f"bin saved at {path}")
@ensure_annotations
def load_bin(path:Path) -> Any:
    """Load binary data
    
    args: path to bin file
    returns: Any object stored file

    """
    data = joblib.load(path)
    logger.info(f"binary_file loaded from {path}")
    return data
@ensure_annotations
def get_size(path:Path) ->str:
    size_in_kb = round(os.path.getsize(path/1024))
    return (f"near {size_in_kb} kb")






