# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:16:55 2022

@author: Mark
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:44:27 2022
@author: Mark, Destiny
"""

import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import layout, column, gridplot
from bokeh.models import CustomJS, ColumnDataSource, CDSView, DateRangeSlider, Select, BoxSelectTool, HoverTool

# -----clean and format the data

raw_data = pd.read_csv("US_Energy.csv", delimiter=",",na_values=('--'))

cleaned_data = raw_data.drop([13,15,17,19],axis=0)
cleaned_data = cleaned_data.drop(['remove', 'units', 'source key', 'category'], axis=1)

cleaned_data = cleaned_data.transpose()

new_header = cleaned_data.iloc[0]  # grab the first row for the header
cleaned_data = cleaned_data[1:]  # take the data less the header row
cleaned_data.columns = new_header

for (columnName, columnData) in cleaned_data.iteritems():
        cleaned_data["Change in "+columnName] = pd.to_numeric(cleaned_data[columnName]).pct_change()

# -----designate and format X and Y

columns = sorted(cleaned_data.columns[:18])
columns_change = sorted(cleaned_data.columns[18:])

cleaned_data['active_axis'] = cleaned_data['U.S. Crude Oil Production']
cleaned_data['Month'] = pd.to_datetime(cleaned_data.index, format="%b-%y")

source = ColumnDataSource(data=cleaned_data)
source2 = ColumnDataSource(data=cleaned_data)
view = CDSView(source=source)
view2 = CDSView(source=source2)

x = pd.to_datetime(cleaned_data.index, format="%b-%y").to_pydatetime()
#y = cleaned_data['U.S. Crude Oil Production']

# ----basic plots

hover = HoverTool(
    mode = "vline",
    tooltips = [
        ('Date', '@index'),
        ('y', '@active_axis'),
    ],
)

tools_to_show = [hover, 'box_zoom','pan,save','reset','wheel_zoom']

plot1 = figure(x_axis_type="datetime", width=900, height=400, tools = tools_to_show)

plot1.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source, view=view)
plot1.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source2, view=view2)

plot1.add_tools(BoxSelectTool())

plot2 = figure(x_axis_type="datetime", width=900, height=200, tools = tools_to_show)

plot2.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source, view=view)

plot2.add_tools(BoxSelectTool())


plot3 = figure(x_axis_type="datetime", width=900, height=200, tools = tools_to_show)

plot3.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source2, view=view2)

plot3.add_tools((BoxSelectTool()))

plot1.x_range = plot2.x_range = plot3.x_range  # Links x range of graphs when manipulated by zoom or pan

# ----- Create Slider and Selector objects
slider = DateRangeSlider(title="Date Range: ", start=min(x), end=max(x), step=1, value=(min(x), max(x)))

axesSelect = Select(title="Y-Axis:", value="U.S. Crude Oil Production", options=columns)

axesSelect2 = Select(title="Y-Axis2:", value="U.S. Crude Oil Production", options=columns)

# ------link slider to graph
slider.js_link("value", plot2.x_range, "start", attr_selector=0)
slider.js_link("value", plot2.x_range, "end", attr_selector=1)

# ------Use JS to change 'active axis' to match selector value
axesSelect.js_on_change('value', CustomJS(args=dict(source=source, axesSelect=axesSelect), code="""
  source.data['active_axis'] = source.data[axesSelect.value]
  source.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source=source2, axesSelect=axesSelect2), code="""
  source.data['active_axis'] = source.data[axesSelect.value]
  source.change.emit()
  """))

# ----plot slider
show(layout([slider, axesSelect, axesSelect2], gridplot([[plot1], [plot2], [plot3]])))