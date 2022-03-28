# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:09:40 2022

@author: Mark
"""

import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import layout
from bokeh.models import DateRangeSlider

#-----clean and format the data

raw_data = pd.read_csv("US_Energy.csv",delimiter=",")

cleaned_data = raw_data.drop(['remove','units','source key','category'], axis=1)

cleaned_data = cleaned_data.transpose()


new_header = cleaned_data.iloc[0] #grab the first row for the header
cleaned_data = cleaned_data[1:] #take the data less the header row
cleaned_data.columns = new_header

#-----designate and format X and Y

x = pd.to_datetime(cleaned_data.index,format="%b-%y").to_pydatetime()
y = cleaned_data['U.S. Crude Oil Production']

#----basic plot

plot = figure(title = "U.S Crude Oil Production", x_axis_type="datetime")
  
plot.line(x=x, y=y, line_width=3, line_alpha=0.5)

plot.xaxis.axis_label = "Date"
plot.yaxis.axis_label = "Production in Millions of Barrels Per Day"
  
#----- Create Slider object
slider = DateRangeSlider(title="Date Range: ", start=min(x), end=max(x),step=1,value=(min(x),max(x)))
  
#------link slider to graph
slider.js_link("value",plot.x_range,"start",attr_selector=0)
slider.js_link("value",plot.x_range,"end",attr_selector=1)

#----plot slider
show(layout([slider, plot]))