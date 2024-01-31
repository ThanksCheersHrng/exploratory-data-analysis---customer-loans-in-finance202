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
        means = self.data_frame.mean() #addition unsupported for float and str, so force float and ignore str?  
        # meds = self.data_frame.median
        # mode = self.data_frame.mode
        # table = [[columns, means, medians, modes], [self.col_names, means, meds, mode]]
        print(means)
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
# df.stats()


# Can I really not perform a mean calculation on a float64 type? Test this on last_payment_amount and next_payment_date (a datetime64[ns] type)

# last_pay = df['last_payment_amount'] # DataFrameInfo object is not subscriptable!? But I want that pandas functionality; surely I should just be using pandas rn instead of creating a bloody class. 
last_pay = finance_df['last_payment_amount']
# print(last_pay.dtype) # confirms this is still float64 even when outside DataFrameInfo class
# print(last_pay.mean) # demonstrates that pd.Series.mean CAN calculate mean for a float64 object 

next_pay_date = finance_df['next_payment_date'] 
# print(next_pay_date.mean) # baller, it worked. 

mini_df = pd.concat({"last pay" : last_pay , 
                     "next date" : next_pay_date}, axis = 1)

# print(mini_df)
# print(mini_df.mean()) # works out beautifully. 


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