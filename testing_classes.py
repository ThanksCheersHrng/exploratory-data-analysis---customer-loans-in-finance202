import numpy as np
import pandas as pd 

#look into parsing dates more effectively with a custom date parser? #see notes in date_parser.txt
finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'])
finance_df['employment_length'] = finance_df['employment_length'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
# print(finance_df['term'].head())
finance_df['term'] = finance_df['term'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 




df = DataFrameInfo(finance_df)