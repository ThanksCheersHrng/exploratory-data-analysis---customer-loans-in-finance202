#Imputing Methods : Two Classes 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def __getitem__(self, key): 
        return self.data_frame[key]

    def plot_column(self, column_name, transformer=None): # explicitly take transformer as an argument in function call 
        # Check if the column exists in the DataFrame
        if column_name not in self.data_frame.columns:
            print(f"Column '{column_name}' not found in the DataFrame.")
            return

        # Get the data type of the column
        column_dtype = self.data_frame[column_name].dtype

        # Plot based on data type
        if pd.api.types.is_numeric_dtype(column_dtype): 
            self._plot_numeric_column(column_name, transformer=transformer) # make transformer an explicit attribute on return
        elif pd.api.types.is_categorical_dtype(column_dtype):
            self._plot_categorical_column(column_name)
        elif pd.api.types.is_datetime64_any_dtype(column_dtype):
            self._plot_datetime_column(column_name)
        else:
            print(f"Unsupported data type for column '{column_name}'.")

    def _plot_numeric_column(self, column_name, transformer = None): # default identity (i.e. no) transformation
        if transformer is None: 
            transformer = lambda x: x  # setting up the default as the identity transformation using lambda. 
        transformed_data = transformer(self.data_frame[column_name])
        plt.figure(figsize=(8, 6))
        sns.histplot(transformed_data, kde=True)
        plt.title(f'Distribution of {column_name}')
        plt.show()

    def _plot_categorical_column(self, column_name):
        plt.figure(figsize=(8, 6))
        sns.countplot(x=column_name, data=self.data_frame)
        plt.title(f'Count of each category in {column_name}')
        plt.show()

    #add a method for datetime data that treats it like numeric. 
    def _plot_datetime_column(self, column_name):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data_frame[column_name], kde=True)
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

    def drop_weak_columns(self, threshold=0.25):  # still has a default parameter of 0.25 so I shouldn't have to change implementation code. 
        weak_columns = self.data_frame.columns[self.data_frame.isna().mean() > threshold]
        self.data_frame = self.data_frame.drop(columns=weak_columns)
        return self.data_frame
    
    def impute_null_values(self):
        null_columns = self.data_frame.columns[self.data_frame.isna().mean() > 0]
        # .fillna method works on Series, so individual breakdown:
        for column in null_columns:
            replace_with_this = self.data_frame[column].median()
            self.data_frame[column].fillna(replace_with_this, inplace = True)
            # I later found out .fillna CAN work on a data frame as well. 
    
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
                
"""             
    def skew_transform(self, skewed_columns, transformations): # the error methods suggested by chatGPT here will help identify which item in which list is causing errors, should any occur. 
        # check that each skewed column has its own transformaiton specified: 
        if len(skewed_columns) != len(transformations):
            raise ValueError("Lengths of skewed_columns and transformations should be the same.")
        for column, trans_func in zip(skewed_columns, transformations): #cool zip = iterator function! 
           if column not in self.data_frame.columns: 
               print(f"Make sure '{column}' is in the data frame.") 
               continue
           if not callable(trans_func): 
               print(f"Check that the transformation {trans_func} is a function.")
        try: 
            self.data_frame[column] = trans_func(self.data_frame[column])
            print(f"transformation '{trans_func}' has been applied to the column, '{column}'.")
        except Exception as e: 
            print(f"Error while applying transformation '{trans_func}' to column '{column}: {e}'")
        pass 
"""