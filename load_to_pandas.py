""" 
In this task, prompt reads 
'create a function which will load the data from your local machine into a Pandas DataFrame.' 
Unless 'create a function' just means 'write a line of code,' but doesn't actually mean 
'create a function,' this prompt sounds like over-engineering... 
surely I could just use pd.read_csv, a function that already exists?
"""
import numpy as np
import pandas as pd

# class DataImportAndClean(): 

# finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'])

column_tabulated_df = pd.read_csv("open_accounts_tabulated.csv")

# print(last_payment_amount_tabulated_df.head())

s = column_tabulated_df['Count']

#print(type(s)) # confirms this is a Series, so, should be able to: 

print(s.sum()) #right, this says that there are 54231 non-NA values in the last_payment_amount column of finance_df 

# print(last_payment_amount_tabulated_df['Count'].sum)

# print(finance_df.shape) # (54231, 44), so 44 columns (variables) for 1 row of variable names and 54,230 loans (entries/rows)
# finance_df.info() # from this we learn the datatype for each variable, and how many non-null entries there are for each variable. 
                    # Notably there are plenty of variables that have some null variables, e.g. months since first payment (could be zero if loan less than a month old) or next payment date (could be null if loan paid). 
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 54231 entries, 0 to 54230
Data columns (total 44 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   Unnamed: 0                   54231 non-null  int64
 1   id                           54231 non-null  int64
 2   member_id                    54231 non-null  int64
 3   loan_amount                  54231 non-null  int64
 4   funded_amount                51224 non-null  float64
 5   funded_amount_inv            54231 non-null  float64
 6   term                         49459 non-null  object
 7   int_rate                     49062 non-null  float64
 8   instalment                   54231 non-null  float64
 9   grade                        54231 non-null  object
 10  sub_grade                    54231 non-null  object
 11  employment_length            52113 non-null  object
 12  home_ownership               54231 non-null  object
 13  annual_inc                   54231 non-null  float64
 14  verification_status          54231 non-null  object
 15  issue_date                   54231 non-null  object
 16  loan_status                  54231 non-null  object
 17  payment_plan                 54231 non-null  object
 18  purpose                      54231 non-null  object
 19  dti                          54231 non-null  float64
 20  delinq_2yrs                  54231 non-null  int64
 21  earliest_credit_line         54231 non-null  object
 22  inq_last_6mths               54231 non-null  int64
 23  mths_since_last_delinq       23229 non-null  float64
 24  mths_since_last_record       6181 non-null   float64
 25  open_accounts                54231 non-null  int64
 26  total_accounts               54231 non-null  int64
 27  out_prncp                    54231 non-null  float64
 28  out_prncp_inv                54231 non-null  float64
 29  total_payment                54231 non-null  float64
 30  total_payment_inv            54231 non-null  float64
 31  total_rec_prncp              54231 non-null  float64
 32  total_rec_int                54231 non-null  float64
 33  total_rec_late_fee           54231 non-null  float64
 34  recoveries                   54231 non-null  float64
 35  collection_recovery_fee      54231 non-null  float64
 36  last_payment_date            54158 non-null  object
 37  last_payment_amount          54231 non-null  float64
 38  next_payment_date            21623 non-null  object
 39  last_credit_pull_date        54224 non-null  object
 40  collections_12_mths_ex_med   54180 non-null  float64
 41  mths_since_last_major_derog  7499 non-null   float64
 42  policy_code                  54231 non-null  int64
 43  application_type             54231 non-null  object
dtypes: float64(20), int64(9), object(15)
memory usage: 18.2+ MB
"""

#first_five = finance_df.head(5) 
# print(first_five) # returns the first five entires for a sample so we can see how they look

# Noticed id sems to start with 3 and member_id seems to start with 4, so checked: 
# print(finance_df['id'].min(), finance_df['id'].max(), finance_df['member_id'].min(), finance_df['member_id'].max())
# 55521 38676116 70694 41461848 so the pattern doesn't persist- id numbers don't have a quickly recognisable format.

# What type of applications could there be? 
# print(set(finance_df['application_type'])) #{'INDIVIDUAL'} so all loans are of the same type

# What is the range of loan amounts? 
# print(finance_df['loan_amount'].min(), finance_df['loan_amount'].max()) # 500 35000, so a range of 34500

# print(set(finance_df['term'])) #I used this to check the contents of every column 

'''
Milestone3:Task1: are there any excess symbols in the data? 
Why, yes! employment_length and term columns can be summarised as floats. 
'''


    # finance_df['employment_length'] = finance_df['employment_length'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)


# print(finance_df['employment_length'])
# print(finance_df['employment_length'].dtype) 

     # finance_df['term'] = finance_df['term'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)

     # finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 


# finance_df.info() 

