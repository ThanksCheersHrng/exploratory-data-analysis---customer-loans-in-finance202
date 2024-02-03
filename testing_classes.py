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
#finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'], date_parser=parse_to_datetime_mo_yr)
finance_df['employment_length'] = finance_df['employment_length'].str.extract(r"([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
# print(finance_df['term'].head())
finance_df['term'] = finance_df['term'].str.extract(r"([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 

class MultipleInheritanceTestClass(im.Plotter, dc.DataFrameInfo):
    pass

df = MultipleInheritanceTestClass(finance_df)

# df.plot_column('issue_date') # Late 2009 looks very popular. 

# df.col_names()

# df.plot_column('home_ownership') # unsupported data type

df.data_types #why isn't this actually printing??? 