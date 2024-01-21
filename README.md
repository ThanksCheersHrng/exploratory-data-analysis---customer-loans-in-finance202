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
	2.1. As AiCore is (pedagogically) handing the reins over to the students moreso at this stage, but still sets out a set of instructions to follow. Despite my lack of experience with AWS, I can imagine there are slower, less "slick", but ultimately simpler ways to extract the dataframe.csv, but in trying to stick to AiCore's instructions I got all in a muddle. In short, I found 'setting the stage' for this one-button click style of download very difficult, and enlisted the help of a programmer friend to tidy up my code in db_utils.py. 
	2.2. Though this is considered part of 'milestone 3,' that is, part of EDA in the AiCore prompts, I can't help but consider Data Cleaning as a prerequisite to EDA, and not part of it itself. Thus, I'm calling this section 2.2, not 3.1.  
		2.2 Data cleaning involved converting columns to more appropriate data types (e.g. to number) and removing excess symbols, among other things. While I have historically performed data cleaning tasks through libraries like pandas directly, then saved the improved databases with their own name (a habit I developed using R), AiCore instructed to make column conversions by setting up a DataTransform class; since I would later import the .py file in which this class existed to an .ipynb file, I opted to create a separate and obviously named data_cleaning_for_EDA.py file for this task; however, it was in examining the columns in load_to_pandas.py closely that I realised the only columns I was likely to have issues with were the dates being listed as 'object' dtypes anyway, so I decided to just add the parse_dates argument in the original pd.read_csv() statement instead.... then, while combing the column titles for potential columns that would need a change to date format, I idenitified that employment_length was unnecessarily stringy; I could identify potential correlations if that was in int64 form, and the same can be said for term. So I parsed dates in load_to_pandas.py (see the non-parsed thing in earlier version control commits), and I changed those two columns 'term' and 'employment_length' in the same file as well, instead of using classes (seems overcomplicated) in data_cleaning_for_EDA.py at all. 
		
	3. Task 2 Prompt: Create a class to get information from the DataFrame. I initially set up a class with -> None: pass as the empty framework. Again I question the use of setting up an entire class when I already have the dataset available for exploration. However, reading the suggested 'useful utility methods,' I feel more motivated to create some of these methods. I thought adding a cor_coef method might come in handy- one that would calculate the correlation between every column and output a matrix; based on prior experience with dimensionality reduction methods, I know this particular method may prove too computationally expensive to produce in pracitse. 

	4. 
### What I've learned: 
	1. 
	2. As I converted employment_length, I was reminded that nan can't be forced to int, but it can be forced to float. 
	3. As I started actually developing a class of methods ("DataFrameInfo()"), I rediscovered trouble with defining classes that had been a stumbling block in the first milestone (defining classes to read off of AWS). At this stage, rewatching AiCore's video on Object Oriented Programming and listening veeeeery carefully at around 8 minutes, I caught a detail that clarifies my confusion (at least in part, we shall see...). Essentially, the __init__ method is only necessary if you need to add information when *initialising* an instance of the class. In other words, if I don't have to input the column names myself, if instead I can just call the method col_names and they're already built into the object (data frames come with pandas.columns method), then I don't have to consider col_names to be an attribute. If I have no such information that I need to personally input on setting up the instance of the class, I don't need the __init__ section of my class-defining code! God, I hope I have that right. --- LOL! (not really laughing out loud, more of a glower at screen, but laughing a little on the inside) If I want my class method outputs to vary according to some *initial* input, then I do still need to initialise the instance with the pd.DataFrame that it recieves. 
	4. 

## Installation instructions 
To install the available data from pull this repo. To see only the pretty final products, i.e. only the analysis and visualisation, you can download the pdf/png/jpg... whatever I manage to save as here as a bonus. 

## Usage instructions 
Run it in your preferred python module. I used VSCode. 

## License information 
This project is the result of the hard work and dedication of the people behind AiCore. All credit goes to AiCore for how the data was sourced and the project structure. As per their instructions, I am submitting my work as a student here on github, an open source platform; this implies that anyone can use my code to further their own learning.
