#Imputing Methods : Two Classes 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def __getitem__(self, key): 
        return self.data_frame[key]
    
    def table(self, column_name):
        column_table = self.data_frame[column_name].value_counts().reset_index()
        column_table.columns = ['Value', 'Count']
        column_table = column_table.sort_values(by='Value')
        print(column_table)

    def plot_column(self, column_name, transformer=None): 
        # Check if the column exists in the DataFrame
        if column_name not in self.data_frame.columns:
            print(f"Column '{column_name}' not found in the DataFrame.")
            return

        # Get the data type of the column
        column_dtype = self.data_frame[column_name].dtype

        # Plot based on data type
        if pd.api.types.is_numeric_dtype(column_dtype): 
            self._plot_numeric_column(column_name, transformer=transformer) 
        elif pd.api.types.is_categorical_dtype(column_dtype):
            self._plot_categorical_column(column_name)
        elif pd.api.types.is_datetime64_any_dtype(column_dtype):
            self._plot_datetime_column(column_name)
        else:
            print(f"Unsupported data type for column '{column_name}'.")

    def _plot_numeric_column(self, column_name, transformer=None): 
        if transformer is None: 
            transformer = lambda x: x
        transformed_data = transformer(self.data_frame[column_name])
        plt.figure(figsize=(8, 6))
        sns.histplot(transformed_data, kde=True, color='teal')
        plt.title(f'Distribution of {column_name}')
        plt.xlabel(column_name)
        plt.show()

    def _plot_categorical_column(self, column_name):
        plt.figure(figsize=(8, 6))
        sns.countplot(x=column_name, data=self.data_frame)
        plt.title(f'Count of each category in {column_name}')
        plt.show()

    #add a method for datetime data that treats it like numeric. 
    def _plot_datetime_column(self, column_name):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data_frame[column_name], kde=True, color='violet')
        plt.title(f'Distribution of {column_name}')
        plt.show()


    def boxplot_with_outliers(self, column_name):
        if column_name not in self.data_frame.columns:
            print(f"Column '{column_name}' not found in the DataFrame.")
            return
        # Can't create a boxplot of categorical data since it's not generally ordinal and I haven't made a distinction. 
        column_dtype = self.data_frame[column_name].dtype
        if pd.api.types.is_numeric_dtype(column_dtype) or pd.api.types.is_datetime64_any_dtype(column_dtype):
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=column_name, data=self.data_frame, showfliers=True) # will show outliers
            plt.title(f'Box plot with outliers for {column_name}')
            plt.show()
        else:
            print(f"Column '{column_name}' is not of numerical or datetime type, skipping box plot.")



# I used ChatGPT to improve the following class, turning my for > if structure in drop_weak_columns into a boolean indexing style function, introducing more flexibility by treating the threshold as a parameter, and turning getitem into a method to improve consistency and encapsulation. 
class DataFrameTransform:
    def __init__(self, data_frame): 
        self.data_frame = data_frame
    
    def __getitem__(self, key): 
        return self.data_frame[key]

    def _get_weak_columns(self, threshold):
        return self.data_frame.columns[self.data_frame.isna().mean() > threshold]

    def drop_weak_columns(self, threshold=0.25):
        weak_columns = self._get_weak_columns(threshold)
        self.data_frame = self.data_frame.drop(columns=weak_columns)
        return self.data_frame
    
    def impute_null_values(self):
        null_columns = self._get_weak_columns(0)  # Adjusted to handle any columns with null values
        for column in null_columns:
            replace_with_this = self.data_frame[column].median()
            self.data_frame[column].fillna(replace_with_this, inplace=True)
    
    def skew_transform(self, skewed_columns, transformations):
        if len(skewed_columns) != len(transformations):
            raise ValueError("Length of skewed_columns and transformations must be the same.")
        
        for column, transform_func in zip(skewed_columns, transformations):
            if column not in self.data_frame.columns:
                print(f"Column '{column}' not found in the DataFrame.")
                continue
            if not callable(transform_func):
                print(f"Transformation for column '{column}' is not a function.")
                continue
            
            try:
                self.data_frame[column] = transform_func(self.data_frame[column])
                print(f"Transformation applied to column '{column}'.")
            except Exception as e:
                print(f"Error applying transformation to column '{column}': {e}")


    def remove_outlier_rows(self, column_with_outlier, threshold): 
        self.data_frame = self.data_frame.loc[self.data_frame[column_with_outlier] <= threshold]
        return self.data_frame
    
    def drop_any_column(self, column_to_drop):
        self.data_frame.drop(columns=[column_to_drop], inplace=True)
        return self.data_frame
    
    def _get_high_corr_pairs(self, threshold, corr_matrix): # private method, as this is a sub-task for another internal method (goodbye_high_corr_cols...)
        high_corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > threshold:
                    high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j]))
        return high_corr_pairs

    def _remove_columns_with_high_skewness(self, numeric_df, high_corr_pairs): # private method, as this is a sub-task for another internal method (goodbye_high_corr_cols...)
        while high_corr_pairs:
            col1, col2 = high_corr_pairs[0]

            skewness_col1 = numeric_df[col1].skew()
            skewness_col2 = numeric_df[col2].skew()

            column_to_drop = col1 if abs(skewness_col1) > abs(skewness_col2) else col2

            self.data_frame.drop(columns=[column_to_drop], inplace=True)

            high_corr_pairs = [(x, y) for x, y in high_corr_pairs if x != column_to_drop and y != column_to_drop]

    def goodbye_high_corr_cols(self, threshold=0.7, columns_to_keep=None):
        numeric_columns = self.data_frame.select_dtypes(include=['number']).columns
        numeric_df = self.data_frame[numeric_columns]

        corr_matrix = numeric_df.corr()

        high_corr_pairs = self._get_high_corr_pairs(threshold, corr_matrix)

        # Remove columns with high skewness except those in columns_to_keep
        if columns_to_keep:
            high_corr_pairs = [(col1, col2) for col1, col2 in high_corr_pairs if col1 not in columns_to_keep and col2 not in columns_to_keep]

        self._remove_columns_with_high_skewness(numeric_df, high_corr_pairs)

        return self.data_frame