import pyodbc
import pandas as pd
from config import JsonConfigurationManager
from models.ShippersModel import ShippersModel

class ShippersRepository():
    def __init__(self):
           config_manager = JsonConfigurationManager('..\..\config\config.json')
           connStr = config_manager.get('data_base_connection').get('sqlserver')
           self.conn = pyodbc.connect(connStr)
           self.conn.autocommit=True
           self.cur = self.conn.cursor()

    def get_list(self):
          query='select  * from Shippers'
          df=pd.read_sql(query,self.conn)
          return df
    
    def get_by_id(self,id):
          query='select  * from Shippers where ShipperID='+id
          df=pd.read_sql(query,self.conn)
          return df
    
    def create_shippers(self,ShippersModel):
        query=f"INSERT INTO Shippers(CompanyName,Phone)VALUES('{ShippersModel.CompanyName}','{ShippersModel.Phone}')"
        self.cur.execute(query)
        if self.cur.rowcount>0:
             return {"message":"Shippers information Save Successfully.","statuscode":201};
        else:
             return {"message":"Faill to save Shippers information.","statuscode":202};

    def update_shippers(self,ShippersModel):
        query=f"UPDATE Shippers SET CompanyName='{ShippersModel.CompanyName}' , Phone='{ShippersModel.Phone}' WHERE ShipperID={ShippersModel.ShipperID}"
        self.cur.execute(query)
        if self.cur.rowcount>0:
             return {"message":"Shippers information Updated Successfully.","statuscode":204}
        else:
             return {"message":"Nothing to Update Shippers information.","statuscode":202}
    
    def delete_shippers(self,id):
        self.cur.execute(f"DELETE FROM Shippers WHERE ShipperID={id}")
        if self.cur.rowcount>0:
             return  {"message":"Shippers information Deleted Successfully.","statuscode":201}
        else:
             return {"message":"Nothing Deleted Shippers information.","statuscode":202}    
        
    

 
       