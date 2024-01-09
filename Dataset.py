import pandas as pd 
import numpy as np 
import json 
from datetime import datetime, timedelta 
import s3fs 

def run_etl():

    #load the data
    data =  pd.read_csv(r"C:\Users\ankur\Documents\boston_store_customers.csv")

    #ETL steps
    data.dropna()
    data.drop_duplicates()

    #convert to csv and save in the project folder
    path = r"C:\\Users\\ankur\Documents\Airflow_Project\\"
    data.to_csv(path+"local_modified_data.csv")