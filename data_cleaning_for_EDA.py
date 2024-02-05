# create class to get info from DataFrame

import numpy as np
import pandas as pd
class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.table = self.data_frame.value_counts()

    def __getitem__(self, key): #this will only allow me to work with one coulmn at a time. 
        return self.data_frame[key]

    def count_cells_in_df_matrix(self):
        element_count = self.data_frame.size
        print(element_count)

    def data_types(self): 
        data_types_listed = self.data_frame.dtypes
        print(data_types_listed)

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
        original_corr_matrix = self.data_frame.corr(numeric_only=True)
        print("Full Numeric Correlation Matrix:")
        print(self.data_frame.corr(numeric_only=True)) 
        #it's such a massive column, I'd like to narrow it down to spit out any correlations with an absolute value greater than 65%. 
        threshold = 0.65
        high_abs_corr_matrix = original_corr_matrix[(original_corr_matrix.abs() > threshold) & (original_corr_matrix < 1.0)] # this will also remove self-correlations. 
        high_abs_corr_matrix = high_abs_corr_matrix.dropna(axis=1, how='all').dropna(axis=0, how='all')
        
        print(f"\nCorrelation Matrix with Correlations > {threshold} or < -{threshold}:")
        print(high_abs_corr_matrix)

