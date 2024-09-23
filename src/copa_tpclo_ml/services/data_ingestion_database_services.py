import pyodbc
import pandas as pd
class DataIngestionDataBaseServices:
       def __init__(self):
              pass
       


def read_sql_data(self):
       data_base_connection_config =self.jsonConfigurationManager.get('data_ingestion').get('source_dir')
       conn = pyodbc.connect(data_base_connection_config.sqlserver)
       query='SELECT [Description]  FROM [Categories]'
       df=pd.read_sql(query,conn)
       return df