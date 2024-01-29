# This is a space where I can test out the methods of my classes. 
import numpy as np
import pandas as pd

# to do: import data_cleaning_for_EDA once finalised
# from data_cleaning_for_EDA import DataFrameInfo 

#import load_to_pandas for access to the db. 
finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'])
finance_df['employment_length'] = finance_df['employment_length'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df['term'] = finance_df['term'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 


#temporary direct copy/paste instead of import- why is name 'DataFrameInfo' not defined??? 
#Now I get this error instead: AttributeError: 'DataFrameInfo' object has no attribute 'dtypes' 

class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def data_types(self): 
        data_types = pd.dtype(self.data_frame)
        print(data_types)

    def col_names(self): 
        print(pd.columns(self.data_frame))


df = DataFrameInfo(finance_df)
df.data_types()
df.col_names()

""" 
#Giving my data frame a short and sweet name to work with 
load_to_pandas 

df = finance_df

# df = load_to_pandas.finance_df() # brackets needed to call a function

df_in_class = DataFrameInfo(df) 

types_of_data = df_in_class.data_types() 

print(types_of_data) 

#As I suspected, it's not 'seeing' pd actions inside the new class, even when the new class has imported pd! 

# data_types = self.dtypes
                 ^^^^^^^^^^^
# AttributeError: 'DataFrameInfo' object has no attribute 'dtypes'
"""