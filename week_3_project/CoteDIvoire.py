# Load the pandas libraries with alias 'pd'
import pandas as pd

#Read data from file 'D:\veronica_moringa\project_dsp\week_3_project\Telcom_dataset_1.csv'
#(which is in the same directory that my python project is based)
# Control delimiters, rows, column names with read_csv

data = pd.read_csv('D:\veronica_moringa\project_dsp\week_3_project\Telcom_dataset_1.csv')

# Preview the first five lines of the loaded data

data.head()
