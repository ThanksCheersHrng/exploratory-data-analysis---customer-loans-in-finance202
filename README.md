# exploratory-data-analysis---customer-loans-in-finance202


This repo is for another Ai Core Project titled "Exploratory Data 
Analysis - Customer Loands in Finance." I've been looking forward to 
seeing what examples of finance questions they put together, hoping that 
eventually the projects will build towards some DL project looking for 
market trends (as an example). Some serious maths!

Let's see where this project takes us, shall we?

# This repo should contain: 
- credentials.yaml which contains the credentials for accessing AWS

- .gitignore, which sets items git should ignore when committing 

- this README.md file 

- db_utils.py which contains code to extract data from the project's database 

	As of 2023.12.02.21.39, this contains a class (as the task dictates should be created) with dummy parameters and methods to remind me how classes work, so that when I'm asked to populate the code with something meaningful, I can remember how.

	As of 2023.25.12, this contains all the necessary code to use the credentials to download the information from AWS, then convert that data into a csv for use in exploratory data analysis. 

	As of 2023.30.12.16.00, I'm still finding it difficult to run db_utils.py to completion; I have pip installed sqlalchemy and pandas *in the VScode terminal,* which seems to successfully convince the code that they're there, but then, even though the code is only X lines long, I get the following ModuleNotFoundError: No module named 'psycopg2'. It is referencing File "C:...\AppData\Roaming\Python\Python311\site-packages\sqlalchemy\dialects\postgresql\psycopg2.py", line 690, in import_dbapi. By the directory, it looks as though this file gets read when trying to apply the sqlalchemy module.  

	As of 2023.12.30.16.10, did a pip install psycopg2, then ran db_utils.py once more and HAAALELUJA, got dataframe.csv in my environment! Now I can start the real project! 

