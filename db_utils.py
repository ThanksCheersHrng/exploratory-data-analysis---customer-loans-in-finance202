import yaml #this will allow us to read credentials.yaml as a dict
from sqlalchemy.engine.url import URL 

#import pandas



def load_credentials(file): #loads file and returns dictionary contained within #help from https://python.land/data-processing/python-yaml#Reading_and_parsing_a_YAML_file_with_Python
	with open('config.yml', 'r') as file
     new_dict = yaml.safe_load(file)
    return new_dict


class RDSDatabaseConnector: 
    def __init__(self, dict_of_creds): 
        self.dict_of_creds = dict_of_creds
        
    def method_engine(self): 
        #initialise a SQLAlechemy engine from dict_of_creds #where TF did this come from? https://docs.sqlalchemy.org/en/20/core/engines.html #https://stackoverflow.com/questions/55895457/is-it-possible-to-pass-a-dictionary-into-create-engine-function-in-sqlalchemy
        url = URL.create(**self.dict_of_creds)
        engine = create_engine(url, echo=True)

    def method_df(self): #Develop a method which extracts data from the RDS database and returns it as a Pandas DataFrame. The data is stored in a table called loan_payments. 
         
#Now create another function which saves the data to an appropriate file format to your local machine. This should speed up loading up the data when you're performing your EDA/analysis tasks. The function should save the data in .csv format, since we're dealing with tabular data.







