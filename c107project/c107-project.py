import plotly.express as px
import numpy as np 
import csv 

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee-in-ml"]))
            hours_of_sleep.append(float(row["sleep-in-hours"]))
    return{"x": cups_of_coffee, "y": hours_of_sleep } 

def findCorrelation(datasource):
    correlaton = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups of Coffee Vs Hours of Sleep ", correlaton[0,1])

def setup():
    data_path = "data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()


