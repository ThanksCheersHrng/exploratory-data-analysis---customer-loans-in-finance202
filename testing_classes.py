import numpy as np
import pandas as pd 

#look into parsing dates more effectively with a custom date parser? #see notes in date_parser.txt
finance_df = pd.read_csv("dataframe.csv", parse_dates= ['issue_date', 'earliest_credit_line','last_payment_date', 'next_payment_date','last_credit_pull_date'])
finance_df['employment_length'] = finance_df['employment_length'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
# print(finance_df['term'].head())
finance_df['term'] = finance_df['term'].str.extract("([-+]?\d*\.\d+|[-+]?\d+)").astype(float)
finance_df.rename(columns = {'employment_length':'years_of_employment', 'term' : 'term_length_in_months'}, inplace = True) 

# print(finance_df['term_length_in_months'].head())
# print(type(finance_df['last_payment_date'][0]))
# print(finance_df['last_payment_date'][0])
# last_payment_date is a Timestamp dtype 
# print(finance_df['last_payment_date'].isna().sum()) #73 nice

# print(finance_df['last_credit_pull_date'].head())
# print(type(finance_df['last_credit_pull_date'][1])) #datetime64 (all the rest were timestamp)
# print(finance_df['last_credit_pull_date'].isna().sum()) #7 



class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.table = self.data_frame.value_counts()

    def count_cells_in_df_matrix(self):
        element_count = self.data_frame.size
        print(element_count)

    def data_types(self): 
        data_types = self.data_frame.dtypes
        print(data_types)

    def col_names(self): 
        col_names = self.data_frame.columns 
        print(col_names)

    def stats(self): 
        print(self.data_frame.describe())
         
    def tabulate_and_export(self, column_name, output_csv_path):
        # Check if the specified column exists in the DataFrame
        if column_name not in self.data_frame.columns:
            raise ValueError(f"Column '{column_name}' not found in DataFrame.")
        # Use value_counts to tabulate the values in the specified column
        value_counts_table = self.data_frame[column_name].value_counts()
        # Convert the value_counts result to a DataFrame for better formatting
        value_counts_df = pd.DataFrame({column_name: value_counts_table.index, 'Count': value_counts_table.values})
        # Export the DataFrame to a CSV file
        value_counts_df.to_csv(output_csv_path, index=False)
        print(f"Table exported to {output_csv_path}")

    def count_null(self): 
        print(self.data_frame.isna().sum()) 
    
    def perc_null(self): 
        print(self.data_frame.isna().mean()*100)
    
    def print_shape(self): 
        print(self.data_frame.shape)
    
    def count_distinct_and_export(self, column_name, output_csv_path):
        # Check if the specified column exists in the DataFrame
        if column_name not in self.data_frame.columns:
            raise ValueError(f"Column '{column_name}' not found in DataFrame.")
        # Use value_counts to tabulate the values in the specified column
        distinct_counts_table = self.data_frame[column_name].count_distinct()
        # Convert the value_counts result to a DataFrame for better formatting
        distinct_counts_df = pd.DataFrame({column_name: distinct_counts_table.index, 'Count': distinct_counts_table.values})
        # Export the DataFrame to a CSV file
        distinct_counts_df.to_csv(output_csv_path, index=False)
        print(f"Table exported to {output_csv_path}")

    def count_distinct(self): #this is a mess of a display, default to use the method above.
        print(self.data_frame.value_counts()) 
    
    def corr_matrix(self): 
        # if dtype('column') is timestamp or datetime64:
          #  self.data_frame['column'] = self.data_frame['column'].dt.month # Not sure if month or year is better- number of months would be best, but perhaps these four columns aren't worth the trouble! 
        print(self.data_frame.corr(numeric_only=True)) #now suddently it works?? I don't recall cleaning my data any more than it was before when this was tripping all over the shop!! 
        #it's such a massive column, I'd like to narrow it down to spit out any correlations with an absolute value greater than 65%. 

df = DataFrameInfo(finance_df)

df.corr_matrix()