import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show
import numpy as np

# Change print setting:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Notes on dataset:
##Data starts on the fifth column
## Source key in column 4
## date columns start at column 6

#Data Cleaning pulled from Mark's DateRangeSlider
raw_data = pd.read_csv("US_Energy.csv",delimiter=",")
cleaned_data = raw_data.drop(['remove','units','source key','category'], axis=1)
cleaned_data = cleaned_data.transpose()
new_header = cleaned_data.iloc[0] #grab the first row for the header
cleaned_data = cleaned_data[1:] #take the data less the header row
cleaned_data.columns = new_header
df = cleaned_data
x = pd.to_datetime(cleaned_data.index, format="%b-%y").to_pydatetime()
y = df['U.S. Heating Degree Days'] #Try out heating days

##First test plot
# p = figure(plot_height=400, plot_width=800, x_axis_type="datetime")
# p.line(x, y)
# show(p)
