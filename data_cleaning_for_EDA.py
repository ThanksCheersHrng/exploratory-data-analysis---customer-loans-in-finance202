# create DataTransform class for column conversions 

class DataTransform():
    def __init__(self) -> None:
        pass


# create class to get info from DataFrame

import numpy as np
import pandas as pd

class DataFrameInfo():
    def __init__(self, data_frame):
        self.data_frame = data_frame
    def data_types(self): 
        data_types = self.dtypes
        print(data_types)
    def col_names(self): 
        print(self.columns)
    def stats(self) -> None: 
        pass
    def count_null(self) -> None: 
        pass
    def perc_null(self) -> None: 
        pass 
    def print_shape(self) -> None: 
        pass
    def count_distinct(self) -> None: 
        pass
    def cor_coef(self) -> None: 
        pass 
    

