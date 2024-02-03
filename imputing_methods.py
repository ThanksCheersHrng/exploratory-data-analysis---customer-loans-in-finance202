#Imputing Methods : Two Classes 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def plot_column(self, column_name):
        # Check if the column exists in the DataFrame
        if column_name not in self.data_frame.columns:
            print(f"Column '{column_name}' not found in the DataFrame.")
            return

        # Get the data type of the column
        column_dtype = self.data_frame[column_name].dtype

        # Plot based on data type
        if pd.api.types.is_numeric_dtype(column_dtype):
            self._plot_numeric_column(column_name)
        elif pd.api.types.is_categorical_dtype(column_dtype):
            self._plot_categorical_column(column_name)
        elif pd.api.types.is_datetime64_any_dtype(column_dtype):
            self._plot_datetime_column(column_name)
        else:
            print(f"Unsupported data type for column '{column_name}'.")

    def _plot_numeric_column(self, column_name):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data_frame[column_name], kde=True)
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


