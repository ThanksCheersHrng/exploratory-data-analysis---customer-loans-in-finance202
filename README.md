# AiCore Project:
## Exploratory Data Analysis - Customer Loans in Finance 
### exploratory-data-analysis---customer-loans-in-finance202

This repo is for another Ai Core Project titled "Exploratory Data 
Analysis - Customer Loands in Finance." I've been looking forward to 
seeing what examples of finance questions they put together, hoping that 
eventually these projects will build towards some DL project looking for 
market trends (as an example). Some serious maths!

Let's see where this project takes us, shall we?

## This repo should contain: 
- credentials.yaml which contains the credentials for accessing AWS (this is in the .gitignore)

- .gitignore, which sets items git should ignore when committing (this means if you pull my repo, you should not get all of the information listed here)

- this README.md file 

- db_utils.py which contains code to extract data from the project's database 

	As of 2023.12.02.21.39, this contains a class (as the task dictates should be created) with dummy parameters and methods to remind me how classes work, so that when I'm asked to populate the code with something meaningful, I can remember how.

	As of 2023.25.12, this contains all the necessary code to use the credentials to download the information from AWS, then convert that data into a csv for use in exploratory data analysis. 

	As of 2023.30.12.16.00, I'm still finding it difficult to run db_utils.py to completion; I have pip installed sqlalchemy and pandas *in the VScode terminal,* which seems to successfully convince the code that they're there, but then, even though the code is only X lines long, I get the following ModuleNotFoundError: No module named 'psycopg2'. It is referencing File "C:...\AppData\Roaming\Python\Python311\site-packages\sqlalchemy\dialects\postgresql\psycopg2.py", line 690, in import_dbapi. By the directory, it looks as though this file gets read when trying to apply the sqlalchemy module.  

	As of 2023.12.30.16.10, did a pip install psycopg2, then ran db_utils.py once more and HAAALELUJA, got dataframe.csv in my environment! Now I can start the real project! 

- load_to_pandas.py which reads dataframe.csv as a pandas dataframe called finance_df, and applies basic pandas functions to become familiar with the data. 

## Project Decription 
### Aims: 
	1. Set up the environment
	2. Extract loan data from the cloud (this was a giant pain.)
	3. Perform Exploratory Data Analysis 
	4. Produce full analysis and visualisation of loan data. 
### Methods: 
	1. I did this in VS code. It turns out a few things needed to be re-installed within VS code in order for db_utils.py to "see" them all in concert. 
	2. As AiCore is (pedagogically) handing the reins over to the students moreso at this stage, but still sets out a set of instructions to follow. Despite my lack of experience with AWS, I can imagine there are slower, less "slick", but ultimately simpler ways to extract the dataframe.csv, but in trying to stick to AiCore's instructions I got all in a muddle. In short, I found 'setting the stage' for this one-button click style of download very difficult, and enlisted the help of a programmer friend to tidy up my code in db_utils.py. 
	3. 
	4. 
### What I've learned: 
	1. 
	2. 
	3. 
	4. 

## Installation instructions 
To install the available data from pull this repo. To see only the pretty final products, i.e. only the analysis and visualisation, you can download the pdf/png/jpg... whatever I manage to save as here as a bonus. 

## Usage instructions 
Run it in your preferred python module. I used VSCode. 

## License information 
This project is the result of the hard work and dedication of the people behind AiCore. All credit goes to AiCore for how the data was sourced and the project structure. As per their instructions, I am submitting my work as a student here on github, an open source platform; this implies that anyone can use my code to further their own learning.
