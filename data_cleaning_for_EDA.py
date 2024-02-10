# create class to get info from DataFrame

import numpy as np
import pandas as pd
import os
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
    
    def corr_matrix(self, threshold=0.65):
        original_corr_matrix = self.data_frame.corr(numeric_only=True)
        print(original_corr_matrix)

        # Filter for correlations above the threshold
        high_corr_indices = np.where((original_corr_matrix.abs() > threshold) & (original_corr_matrix < 1.0))
        # Return a matrix of just the pairs that are highly correlated
        high_corr_pairs = [(original_corr_matrix.index[i], original_corr_matrix.columns[j]) for i, j in zip(*high_corr_indices) if i != j]

        # Loop through to make sure every pair gets plotted
        for idx, (column1, column2) in enumerate(high_corr_pairs):
            # Create a new figure for each scatterplot
            plt.figure(figsize=(8, 6))
    
            sns.scatterplot(data=self.data_frame, x=column1, y=column2)
            plt.title(f"{column1} vs {column2}")
    
            # Save scatterplot to PNG file
            plt.savefig(f"high_corr_scatterplot_{column1}_vs_{column2}.png")
            plt.close()  # Close the current plot to release memory


        # Filter the original correlation matrix for absolute correlations above the threshold
        high_abs_corr_matrix = original_corr_matrix.loc[high_corr_pairs]
        # Use high_corr_pairs to filter the original matrix
        high_abs_corr_matrix = high_abs_corr_matrix.dropna(axis=1, how='all').dropna(axis=0, how='all')

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

