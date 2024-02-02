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
        self.table = self.data_frame.value_counts()

    def count_elements(self):
        element_count = self.data_frame.size
        print(element_count)

    def data_types(self): 
        data_types = self.data_frame.dtypes
        print(data_types)

    def col_names(self): 
        header = self.data_frame.columns 
    
    def stats(self): 
        means = self.data_frame.mean(numeric_only=True) #addition unsupported for float and str, so force float and ignore str?  
        meds = self.data_frame.median(numeric_only=True)
        mode = self.data_frame.mode(axis=1, dropna=True)
        # print(mode) # still returns a whole bunch of 0.0, NaN, NaT, despite dropna=True # as I supsected, mode has no issue with str. 
        
        #### One possible way to display it all: 
        # to_display = {"means": means, "medians": meds}
        # display_df = pd.concat(to_display, axis = 1) 
        # print(display_df)

        #### Another possible way to display it all: 
        # table = [[columns, means, medians, modes], [self.col_names, means, meds, mode]]
        # print(tabulate(table))

    def tabulate_non_null_values(self): #I'm struggling to believe over 97% of the entries in every column are NA's.  
        print(self.table)
        # self.table = pd.DataFrame(self.table)
        # self.table.to_csv('Table_of_non_null_values.csv', sep = " ") #it was too big to be legible in vs code so I thought to export to csv # just got a bunch of ones; clearly not identifying the right 'sep'

    def count_null(self): 
        # approach number 1
        # createa a count of this somehow: 
            # (self.data_frame.isna)  # this is boolean same-sized df showing places of NA elts (so like, count if =True)
        # approach number 2
        all_count = self.data_frame.size # n. elts in array
        non_null_count = self.data_frame.count() # n. non-null elts
        null_count = all_count - non_null_count
        print(null_count)
    
    def perc_null(self): 
        numerator = self.data_frame.size - self.data_frame.count()
        denominator = self.data_frame.size
        print(100*numerator/denominator)
    
    def print_shape(self): 
        print(self.data_frame.shape)
    
    def count_distinct(self):
        # print(self.data_frame.) 
        pass
    
    def cor_coef(self): 
        pass 

df = DataFrameInfo(finance_df)
# the applicatons of each method below get commented out as I confirm they work 
# df.data_types()
# df.col_names()
# df.stats()
# df.print_shape() # (54231, 44)
# df.count_null() #that works. They're all in the 2 milliion's, but different values 
# df.perc_null() # they all come out to around 98%, which is bonkers, but fits with the null count. 
# df.count_elements() # 2386164
# df.tabulate_non_null_values() #it works but it's a mess to look at. # I'm losing time! 



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