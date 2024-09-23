import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "copa_tpclo_ml"

list_of_files = [
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion_componentes.py",
    f"src/{project_name}/components/data_ingestion_facade_componentes.py",
    f"src/{project_name}/components/data_visualization_componentes.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration_manager.py",

    f"src/{project_name}/constants/__init__.py",

    f"src/{project_name}/exceptionhandler/__init__.py",
    f"src/{project_name}/exceptionhandler/custom_exception.py",
    
    f"src/{project_name}/logging/__init__.py",
   
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/text_data_output_model.py",

    f"src/{project_name}/pipeline/__init__.py",

    f"src/{project_name}/repository/__init__.py",
    f"src/{project_name}/repository/inmemory_repository.py",
    f"src/{project_name}/repository/Irepository.py",
    f"src/{project_name}/repository/shippers_repository.py",

    f"src/{project_name}/services/__init__.py",
    f"src/{project_name}/services/csv_loader.py",
    f"src/{project_name}/services/data_ingestion_api_services.py",
    f"src/{project_name}/services/data_ingestion_database_services.py",
    f"src/{project_name}/services/data_ingestion_file_factory_services.py",
    f"src/{project_name}/services/shippers_services.py",
    f"src/{project_name}/services/text_file_loader.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/cleanup_csv_data.py",
    f"src/{project_name}/utils/cleanup_table_data.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/helper.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/processing_text_data.py",

    "config/config.yaml",
    "config/config.ini",
    "config/config.json",
    "test/__init__.py",
    "app.py",
    "main.py",
    "resources_setup.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/Experiment.ipynb",
    "artifacts/data.csv",
    "artifacts/data_ingestion/data.csv",
    "artifacts/archive/data.csv",
    "logs",
    "plot"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")

