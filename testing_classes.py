#This is a space where I can test out the methods of my classes. 

import data_cleaning_for_EDA
import load_to_pandas

#Giving my data frame a short and sweet name to work with 
df = load_to_pandas.finance_df

df_in_class = DataFrameInfo(df) #see this is why I don't see the point- pandas already has most (if not all) of the methods we're after

types_of_data = df_in_class.data_types() 

