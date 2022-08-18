from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://localhost:51990')
        self.database = self.client['AAC']                          
        #self.client = MongoClient('mongodb://%s:%s@localhost:51190/?authMechanism=DEAFULT&authSource=AAC' % accuser, cs340job))
        #self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary    
            return True                      
        else:
            raise Exception("Nothing to save, because data parameter is empty")
                                  
                                  
       # Create method to implement the R in CRUD. 
    def read_all(self,data):
        cursor =self.database.animals.find(data, {'_id':False} ) #return a cursor pointer to list results(docs)
        return cursor
        
                                                  
    def read(self,data):
        if data is not None:
            
            return self.database.animals.find(data) #returns only one doc as a python dictionary
        else:
            print('Nothing to read, because data parmameter is empty')
            return False
        
        #create method to update
    def update(self,data,updateData):   
            
        if data is not None:
            result= self.database.animals.update_one(data,{'$set':updateData})#update and set data
            
        else :
            updateException="Not found" #if not found error message
            return updateException
                
            
          
        
        #Create delete method
    def delete(self,data):
        if data is not None:
            self.database.animals.remove_one(data) #delets data
            return True
        else:

            deleteException = "Nothing to delete" #if no data returns error message
            return deleteException
        
                 
                                 