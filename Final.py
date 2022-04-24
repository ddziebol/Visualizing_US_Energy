# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:16:55 2022
@author: Destiny, Mark
"""
import time
import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import layout, column, gridplot, row
from bokeh.models import CustomJS, ColumnDataSource, CDSView, DateRangeSlider, Select, BoxSelectTool, HoverTool, \
    CrosshairTool, VArea, Patch, Patches, BoxZoomTool, Div, HArea, IndexFilter
from bokeh.transform import linear_cmap, LinearColorMapper
from bokeh.palettes import Spectral6, GnBu, Viridis256
# -----clean and format the data

raw_data = pd.read_csv("US_Energy.csv", delimiter=",", na_values=('--'))

cleaned_data = raw_data.drop([13, 15, 17, 19], axis=0)
cleaned_data = cleaned_data.drop(['remove', 'units', 'source key', 'category'], axis=1)

cleaned_data = cleaned_data.transpose()

new_header = cleaned_data.iloc[0]  # grab the first row for the header
cleaned_data = cleaned_data[1:]  # take the data less the header row
cleaned_data.columns = new_header

for (columnName, columnData) in cleaned_data.iteritems():
    cleaned_data["Change in " + columnName] = pd.to_numeric(cleaned_data[columnName]).pct_change()

# -----designate and format X and Y

columns = sorted(cleaned_data.columns[:18])
columns_change = sorted(cleaned_data.columns[18:])

cleaned_data['active_axis'] = cleaned_data['U.S. Crude Oil Production'] #This gives all graphs same starting values
cleaned_data['Month'] = pd.to_datetime(cleaned_data.index, format="%b-%y")

source = ColumnDataSource(data=cleaned_data)  # Plot2 -> 3
source2 = ColumnDataSource(data=cleaned_data)  # Plot3 -> 4
source3 = ColumnDataSource(data=cleaned_data)  # Plot1 -> 2
source4 = ColumnDataSource(data=cleaned_data)  # Plot1 -> 1
view = CDSView(source=source)  # Plot2
view2 = CDSView(source=source2)  # Plot3
view3 = CDSView(source=source3)  # Plot1
view4 = CDSView(source=source3)  # Plot1

x = pd.to_datetime(cleaned_data.index, format="%b-%y").to_pydatetime()

Default1 = "U.S. Crude Oil Production"
Default2 = "U.S. Coal Consumption"
source.data['active_axis'] = source.data[Default1]  # sets appropriate defaults for plot1
source2.data['active_axis'] = source.data[Default2]
source3.data['active_axis'] = source.data["Change in "+Default1]  # sets appropriate defaults for plot1
source4.data['active_axis'] = source.data["Change in "+Default2]

#example views for varea segments:

#-----Prepare tools for plots:
hover = HoverTool(
    mode="vline",
    tooltips=[
        ('Date', '@index'),
        ('y', '@active_axis'),
    ],
)
linked_crosshair = CrosshairTool(dimensions="height")

box_selector = BoxSelectTool()
box_zoom = BoxZoomTool()
#removed box_selector from list
tools_to_show = ['box_zoom', hover, linked_crosshair,  'pan,save', 'reset']
toolbar_options=dict(logo='gray')


#Linear_cmap for color?
#mapper = linear_cmap(field_name='y', palette=Spectral6, low=0, high=10)

# ----plot configuration:


plot1 = figure(x_axis_type="datetime", width=900, height=400, tools=tools_to_show, title="Percent Change", title_location='left')

plot1.line(x='Month', y='active_axis', line_width=1, line_alpha=0.5, source=source3, view=view3, color='orange')

plot1.line(x='Month', y='active_axis', line_width=1, line_alpha=0.5, source=source4, view=view4, color='blue')

view5 = CDSView(source=source3, filters=[IndexFilter([0,1,2,3,4,5])])
view6 = CDSView(source=source3, filters=[IndexFilter([5,6,7,8,9,10,11])])

glyph = VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in "+Default2, fill_alpha = 0.5, fill_color = 'purple') #works
glyph2 = VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in "+Default2, fill_alpha = 0.5, fill_color = 'gray')

plot1.add_glyph(source3, glyph, view = view5) #works
plot1.add_glyph(source3, glyph2, view = view6)

#plot1.hbar(y = 0, right = max(source.data['Month']), left = min(source.data['Month']), height = 1, fill_alpha = .1) #Works - colors graph one color for range of month. Does pick up hover tool.









plot2 = figure(x_axis_type="datetime", width=900, height=200, tools=tools_to_show, title=Default1, title_location='left')

plot2.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source, view=view, color='orange')

plot3 = figure(x_axis_type="datetime", width=900, height=200, tools=tools_to_show, title=Default2, title_location='left')

plot3.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source2, view=view2,  color='blue')

plot1.x_range = plot2.x_range = plot3.x_range  # Links x range of graphs when manipulated by zoom or pan

# ----- Create Slider and Selector objects
slider = DateRangeSlider(title="Date Range: ", start=min(x), end=max(x), step=1, value=(min(x), max(x)))

axesSelect = Select(title="Y-Axis:", value=Default1, options=columns, background='orange')

axesSelect2 = Select(title="Y-Axis2:", value=Default2, options=columns, background='#848FF0')


# ------link slider to graph
slider.js_link("value", plot2.x_range, "start", attr_selector=0)
slider.js_link("value", plot2.x_range, "end", attr_selector=1)

# ------Use JS to change 'active axis' to match selector value
axesSelect.js_on_change('value', CustomJS(args=dict(source=source, axesSelect=axesSelect), code="""
  source.data['active_axis'] = source.data[axesSelect.value]
  source.change.emit()
  """))

axesSelect.js_on_change('value', CustomJS(args=dict(source=source3, axesSelect=axesSelect), code="""
  source.data['active_axis'] = source.data["Change in " + axesSelect.value]
  source.change.emit()
  """))


axesSelect2.js_on_change('value', CustomJS(args=dict(source=source2, axesSelect=axesSelect2), code="""
  source.data['active_axis'] = source.data[axesSelect.value]
  source.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source=source4, axesSelect=axesSelect2), code="""
  source.data['active_axis'] = source.data["Change in " + axesSelect.value]
  source.change.emit()
  """))

### Update VArea

axesSelect.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph,glyph2 = glyph2, axesSelect=axesSelect), code="""
  glyph.y1.field = "Change in " + axesSelect.value;
  glyph2.y1.field = "Change in " + axesSelect.value;
  source.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph, glyph2 = glyph2, axesSelect=axesSelect2), code="""
  glyph.y2.field = "Change in " + axesSelect.value;
  glyph2.y2.field = "Change in " + axesSelect.value;
  source.change.emit()
  """))

axesSelect.js_link('value', plot2.title, 'text')

axesSelect2.js_link('value', plot3.title, 'text')

# ----plot slider
show(layout(row(Div(text="<h1>U.S. Energy Comparison. Select and Compare:</h1>"), sizing_mode='stretch_width'), [slider, axesSelect, axesSelect2], gridplot([[plot1], [plot2], [plot3]], toolbar_options=dict(logo='grey'))))
# while True:
#     time.sleep(1)
#     print("Y1: ", glyph.y1)
#     print("Y2: ", glyph.y2)
print(source.data['Month'][0:5])