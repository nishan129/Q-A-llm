import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname")

list_files = [
    "src/__init__.py",
    "src/run_local.py",
    "src/helper.py",
    "model/instruction.txt",
    "requirements.txt",
    "setup.py",
    "main.py"
]

for file_path in list_files:
    filePath = Path(file_path)
    filedir, filename = os.path.split(filePath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file : {filename}")
        
    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, 'w') as f:
            pass
        
        logging.info(f"Creating empty file : {filePath}")
        
    else:
        logging.info(f"{filename} file is already exists")