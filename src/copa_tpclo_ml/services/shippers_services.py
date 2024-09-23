from models.ShippersModel import ShippersModel
from repository import ShippersRepository

class ShippersServices():
    shippersRepository=ShippersRepository();
    def __init__(self):
         pass
         
    def get_list(self):
          return self.get_list()
    
    def get_by_id(self,id):
          return self.get_by_id(id)
    
    def create_shippers(self,ShippersModel):
        return self.create_shippers(ShippersModel)

    def update_shippers(self,ShippersModel):
        return self.update_shippers(ShippersModel)
    
    def delete_shippers(self,id):
        return self.deleteShippers(id)
        
    

 
       