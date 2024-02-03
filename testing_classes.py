import numpy as np
import pandas as pd  
import data_cleaning_for_EDA as dc 
import matplotlib.pyplot as plt
import seaborn as sns
import imputing_methods as im

# I keep getting date parsing warnings when I least expect them so I'm going to try specifying a single format now. 
# Apart from the columns I turn into floats below, all the other date-type columns in finance_df appear to be Month-Year in shape:
def parse_to_datetime_mo_yr(date_str):
    return pd.to_datetime(date_str, format='%m-%Y', errors='coerce')

# Reading in the csv and parsing dates. 
finance_df = pd.read_csv(
    "dataframe.csv",
    parse_dates=['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date'],
    date_format='%m-%Y',
    converters={'issue_date': parse_to_datetime_mo_yr, 
                'earliest_credit_line': parse_to_datetime_mo_yr,
                'last_payment_date': parse_to_datetime_mo_yr,
                'next_payment_date': parse_to_datetime_mo_yr,
                'last_credit_pull_date': parse_to_datetime_mo_yr}
)
# Cleaning up lengths of time that could be treated as floats. 
finance_df['employment_length'] = finance_df['employment_length'].str.extract(r"([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df['term'] = finance_df['term'].str.extract(r"([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 
# Cleaning up object type columns- all of which are suitable for category (I checked).
columns_to_cat = ['grade', 'sub_grade', 'verification_status', 'home_ownership', 'loan_status', 'payment_plan', 'purpose', 'application_type']
finance_df[columns_to_cat] = finance_df[columns_to_cat].astype('category')

class MultipleInheritanceTestClass(im.Plotter, dc.DataFrameInfo):
    pass

df = MultipleInheritanceTestClass(finance_df)

# deciding which (if any) columns have too many NULLs: 

df.print_shape()
df.perc_null()


# df.plot_column('issue_date') # Late 2009 looks very popular. 

# df.col_names()

# df.plot_column('home_ownership') # unsupported data type

# df.data_types() 