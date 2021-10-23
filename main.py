import pandas as pd
import cv2
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import statistics
import random
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('medium_data.csv')

population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    mean_list=data
    fig=ff.create_distplot([data], ["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()

first_std_deviation_start, first_std_deviation_end=population_mean-std_deviation, population_mean+std_deviation
second_std_deviation_start, second_std_deviation_end=population_mean-(2*std_deviation), population_mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end=population_mean-(3*std_deviation), population_mean+(3*std_deviation)
print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

fig=ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode="lines", name="Standard Deviation Start 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.17], mode="lines", name="Standard Deviation End 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.17], mode="lines", name="Standard Deviation Start 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode="lines", name="Standard Deviation End 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0,0.17], mode="lines", name="Standard Deviation Start 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0,0.17], mode="lines", name="Standard Deviation End 3"))
fig.show()