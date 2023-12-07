import yaml
from sqlalchemy import create_engine, text
import pandas as pd


def load_credentials(file_path='credentials.yaml'):
    """
    Load a .yaml file into a dict

    Args:
        file_path: path to your yaml file

    Returns:
        new_dict: dict of database credentials

    """
    with open(file_path) as file:
        new_dict = yaml.safe_load(file)

    return new_dict


class RDSDatabaseConnector(): 
    def __init__(self, dict_of_creds): 
        self.dict_of_creds = dict_of_creds

    def init_sql_engine(self):
        """
        Initialize the SQLAlchemy engine

        """
        engine = create_engine('postgresql://{username}:{password}@{endpoint}:{port}/{database}'.format(username=self.dict_of_creds['RDS_USER'],
                                                                                                    password=self.dict_of_creds['RDS_PASSWORD'],
                                                                                                    endpoint=self.dict_of_creds['RDS_HOST'],
                                                                                                    port=self.dict_of_creds['RDS_PORT'],
                                                                                                    database=self.dict_of_creds['RDS_DATABASE']
                                                                                                    ))

        return engine
    
    def extract_data_from_db(self):
        """
        Extract the data from the database into a dataframe

        Returns:
            df: pandas dataframe of data from the database

        """
        sql_engine = self.init_sql_engine()
        
        table_name = 'loan_payments'

        sql = 'select * from {table_name};'.format(table_name=table_name)

        df = pd.DataFrame(sql_engine.connect().execute(text(sql)))

        return df

    def export_dataframe_to_csv(self, path='', file_name='dataframe.csv'):
        """
        Export a dataframe into a .csv file

        Args:
            path: the folder location to create the .csv file in e.g. path/to/your/folder/
                    empty string is current working dir
            file_name: the name of the .csv file to export to
        """
        df = self.extract_data_from_db()

        full_path = path + file_name

        df.to_csv(full_path, encoding='utf-8')


"""
Checking it all runs...
"""

creds = load_credentials()

rds_connector = RDSDatabaseConnector(creds)

rds_connector.export_dataframe_to_csv()



