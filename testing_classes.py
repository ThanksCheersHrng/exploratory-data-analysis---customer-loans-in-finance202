#This is a space where I can test out the methods of my classes. 
import numpy as np
import pandas as pd

#import data_cleaning_for_EDA
import load_to_pandas

#temporary direct copy/paste instead of import- why is name 'DataFrameInfo' not defined??? 
#Now I get this error instead: AttributeError: 'DataFrameInfo' object has no attribute 'dtypes' 

class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame
    def data_types(self): 
        data_types = self.dtypes
        print(data_types)
    def col_names(self): 
        print(self.columns)

#Giving my data frame a short and sweet name to work with 
df = load_to_pandas.finance_df

df_in_class = DataFrameInfo(df) #see this is why I don't see the point of creating classes in this project- all these layers of instantiation take so much time and brainspace! I've been at this for hours, just trying to get DataFrameInfo to work and spit out the data types of each column- pandas already has most (if not all) of the methods we're after

types_of_data = df_in_class.data_types() 

