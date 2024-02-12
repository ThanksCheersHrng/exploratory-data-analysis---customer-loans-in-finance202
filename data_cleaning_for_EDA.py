# create class to get info from DataFrame

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt 
import seaborn as sns
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
        # return(data_types_listed)

    def col_names(self): #advised by ChatGPT when couldn't call col_names as an iterable/list-- it kept coming back as None type. 
        if isinstance(self.data_frame, pd.DataFrame):  # Check if self.data_frame is a DataFrame
            col_names = self.data_frame.columns.tolist()  # Convert columns to a list if self.data_frame is a DataFrame
            return col_names #must now remember to call print() if I just want to see the col_names. 
        else:
            print("Error: 'data_frame' is not a valid DataFrame object.")
            return None
        
    def stats(self): 
        print(self.data_frame.describe())
        # return(self.data_frame.describe())
         
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
    
    def _get_high_correlation_pairs(self, threshold):  # internal method in service of high_corr_matrix
        original_corr_matrix = self.data_frame.corr(numeric_only=True)

        high_corr_indices = np.where((original_corr_matrix.abs() > threshold) & (original_corr_matrix < 1.0))
        high_corr_pairs = [(original_corr_matrix.index[i], original_corr_matrix.columns[j]) for i, j in zip(*high_corr_indices) if i != j]

        return high_corr_pairs

    def _plot_high_corr_scatterplots(self, high_corr_pairs): # internal method in service of high_corr_matrix
        for idx, (column1, column2) in enumerate(high_corr_pairs):
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=self.data_frame, x=column1, y=column2, color='teal')
            plt.title(f"{column1} vs {column2}")
            plt.savefig(f"high_corr_scatterplot_{column1}_vs_{column2}.png")
            plt.close()

    def _filter_high_abs_corr_matrix(self, high_corr_pairs): # internal method in service of high_corr_matrix
        high_abs_corr_matrix = self.data_frame.corr(numeric_only=True).loc[[pair for pair in high_corr_pairs]]
        high_abs_corr_matrix = high_abs_corr_matrix.dropna(axis=1, how='all').dropna(axis=0, how='all')
        return high_abs_corr_matrix

    def high_corr_matrix(self, threshold=0.65): # name changed from corr_matrix to high_corr_matrix- note the code in ongoing_workspace won't match any more. 
        high_corr_pairs = self._get_high_correlation_pairs(threshold)
        self._plot_high_corr_scatterplots(high_corr_pairs)

        high_abs_corr_matrix = self._filter_high_abs_corr_matrix(high_corr_pairs)
        print(f"\nCorrelation Matrix with Correlations > {threshold} or < -{threshold}:")
        print(high_abs_corr_matrix)
    

    def high_skew_columns(self, threshold = 1.2): 
        skewed_columns = [] 
        for column in self.data_frame.columns: 
            if pd.api.types.is_numeric_dtype(self.data_frame[column]):
                skewness = self.data_frame[column].skew()
                if abs(skewness) > threshold: 
                    skewed_columns.append(column)
        return skewed_columns # return becuase I might want to use this later, so remember to print it. 

