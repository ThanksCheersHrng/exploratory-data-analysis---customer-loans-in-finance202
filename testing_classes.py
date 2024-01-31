# This is a space where I can test out the methods of my classes. 
import numpy as np
import pandas as pd
# from tabulate import table

# to do: import data_cleaning_for_EDA once finalised
# from data_cleaning_for_EDA import DataFrameInfo 

#import load_to_pandas for access to the db. 
finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'])
finance_df['employment_length'] = finance_df['employment_length'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df['term'] = finance_df['term'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 


class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def data_types(self): 
        data_types = self.data_frame.dtypes
        print(data_types)

    def col_names(self): 
        header = self.data_frame.columns 
    
    def stats(self) -> None: 
        means = self.data_frame.mean(numeric_only=True) #addition unsupported for float and str, so force float and ignore str?  
        meds = self.data_frame.median(numeric_only=True)
        # mode = self.data_frame.mode
        # table = [[columns, means, medians, modes], [self.col_names, means, meds, mode]]
        # to_display = {"means": means, "medians": meds}
        # display_df = pd.concat(to_display, axis = 1) 
        # print(display_df)
        print(meds)
        # print(tabulate(table))


    def count_null(self) -> None: 
        pass
    
    def perc_null(self) -> None: 
        pass 
    
    def print_shape(self) -> None: 
        pass
    
    def count_distinct(self) -> None: 
        pass
    
    def cor_coef(self) -> None: 
        pass 

df = DataFrameInfo(finance_df)
# the applicatons of each method below get commented out as I confirm they work 
# df.data_types()
# df.col_names()
df.stats()


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