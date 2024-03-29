# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:16:55 2022
@author: Destiny, Mark
"""
import time
import pandas as pd
import colorcet as cc
import numpy as np
import datetime as dt
from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.themes import built_in_themes
from bokeh.layouts import layout, column, gridplot, row
from bokeh.models import CustomJS, ColumnDataSource, CDSView, DateRangeSlider, Select, BoxSelectTool, HoverTool, \
    CrosshairTool, VArea, Patch, Patches, BoxZoomTool, Div, HArea, IndexFilter, ColorBar, Span, Label, RadioButtonGroup
from bokeh.transform import linear_cmap, LinearColorMapper
from bokeh.palettes import Spectral6, GnBu, mpl, brewer, all_palettes, Viridis256, Cividis256, Turbo256, Viridis, Cividis, cividis, viridis, inferno, linear_palette

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
cleaned_data['formattedMonth'] = cleaned_data['Month'].dt.strftime('%B %Y')
cleaned_data['Cor'] = '' #Empty column to be filled with correlaiton values in JS callbacks.

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
Default2 = "U.S. Liquid Fuels Consumption"
source.data['active_axis'] = source.data[Default1]  # sets appropriate defaults for plot1
source2.data['active_axis'] = source.data[Default2]
source3.data['active_axis'] = source.data["Change in "+Default1]  # sets appropriate defaults for plot1
source4.data['active_axis'] = source.data["Change in "+Default2]

#example views for varea segments:

#-----Prepare tools for plots:
hover = HoverTool(
    mode="vline",
    tooltips=[
        ('Date', '@formattedMonth'),
        ('y', '@active_axis{0.000 a}'),
        ('Correlation', '@Cor')
    ],
)
linked_crosshair = CrosshairTool(dimensions="height")

box_selector = BoxSelectTool()
box_zoom = BoxZoomTool()
#removed box_selector from list
tools_to_show = ['box_zoom', box_selector, hover, linked_crosshair,  'pan,save', 'reset']
toolbar_options=dict(logo='gray')

# ----plot + line configuration:
width = 1500
height1 = 400
height2 = 200

#curdoc().theme = 'dark_minimal'

plot1 = figure(x_axis_type="datetime", width=width, height=height1, tools=tools_to_show, title="Percent Change", title_location='left')

<<<<<<< HEAD
plot1.line(x='Month', y='active_axis', line_width=1, line_alpha=1, source=source3, view=view3, color='orange')
=======
plot1.line(x='Month', y='active_axis', line_width=1, line_alpha=1.0, source=source3, view=view3, color='orange')
>>>>>>> origin/main

plot1.line(x='Month', y='active_axis', line_width=1, line_alpha=0.5, source=source4, view=view4, color='blue')

#plot1.background_fill_color = '#F1E8E8'


plot2 = figure(x_axis_type="datetime", width=width, height=height2, tools=tools_to_show, title=Default1, title_location='left')

plot2.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source, view=view, color='orange')

plot3 = figure(x_axis_type="datetime", width=width, height=height2, tools=tools_to_show, title=Default2, title_location='left')

plot3.line(x='Month', y='active_axis', line_width=3, line_alpha=0.5, source=source2, view=view2,  color='blue')

plot1.x_range = plot2.x_range = plot3.x_range  # Links x range of graphs when manipulated by zoom or pan

#-------Spans and lables for dates
SCovid19 = Span(location = source.data['Month'][363], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
LCovid19 = Label(x =source.data['Month'][363], y = 0.1, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Start of Covid-19 in U.S.", text_alpha = 1, text_font_style = 'bold',text_color='white')

S2008 = Span(location = source.data['Month'][215], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
L2008 = Label(x =source.data['Month'][215], y = 0.1, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Start of 2008 U.S. financial crisis", text_alpha = 1,  text_font_style = 'bold',text_color='white')

SUkrane = Span(location = source.data['Month'][385], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
LUkrane = Label(x =source.data['Month'][385], y = 0.14, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Start of 2022 war \nin Ukraine", text_alpha = 1,  text_font_style = 'bold',text_color='white')

SJP = Span(location = source.data['Month'][42], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
LJP = Label(x =source.data['Month'][42], y = 0.1, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Jurassic Park Released", text_alpha = 1,  text_font_style = 'bold',text_color='white')

S911 = Span(location = source.data['Month'][141], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
L911 = Label(x =source.data['Month'][141], y = 0.13, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "9/11 Attacks", text_alpha = 1,  text_font_style = 'bold',text_color='white')

SDotCom = Span(location = source.data['Month'][123], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
LDotCom = Label(x =source.data['Month'][123], y = 0.1, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Beginning of Dot Com crash", text_alpha = 1,  text_font_style = 'bold',text_color='white')

SParis = Span(location = source.data['Month'][311], dimension='height', line_dash = 'dashed', line_width = 2, line_color = '#E00B9E', line_alpha = 1)
LParis = Label(x =source.data['Month'][311], y = 0.1, x_offset = 2, y_offset = 2, text_font_size = '10pt', text = "Start of Paris Accord", text_alpha = 1,  text_font_style = 'bold',text_color='white')

EventSpans = [SCovid19, S2008, SUkrane, SJP, S911, SDotCom, SParis]
EventLabels = [LCovid19, L2008, LUkrane, LJP, L911, LDotCom, LParis]

for i in range(len(EventSpans)):
    plot1.add_layout(EventSpans[i])

for i in range(len(EventLabels)):
    plot1.add_layout(EventLabels[i])

# ------Fill between lines creation and initial application:
length = len(source.data['Month'])

#Palatte selection and add colorbar:

selectPalette = cc.gwv

palette = linear_palette(selectPalette, 200)

paletteInstance2 = LinearColorMapper(selectPalette, low = -1, high = 1)

colorbar = ColorBar(color_mapper = paletteInstance2, label_standoff = 12, location = (0,0), title = "Correlation")
plot1.add_layout(colorbar, 'right')


#Make list of all views, one for each month:
views = []
for i in range(length-1):
    views.append(CDSView(source=source3, filters = [IndexFilter([i, i+1])]))

#Make glyphs with colormap:
glyphs = []
for i in range(length-1):
    glyphs.append(VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in "+Default2, fill_alpha = 0.7, fill_color = palette[int((i * 200) / length)]))

#Apply glyphs and views:
for i in range(length-1):
    plot1.add_glyph(source3, glyphs[i], view = views[i])


# ----- Create Slider and Selector objects
slider = DateRangeSlider(title="Date Range: ", start=min(x), end=max(x), step=1, value=(min(x), max(x)))

axesSelect = Select(title="Select First Time Series:", value=Default1, options=columns, background='orange')

axesSelect2 = Select(title="Select Second Time Series:", value=Default2, options=columns, background='#848FF0')

radio_button_group = RadioButtonGroup(labels = ['Show Events', 'Hide Labels', 'Hide All'], active = 0, background ="#6AD8DB", sizing_mode = "stretch_both")

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

# ------Use JS to change 'active axis' to match selector value and update color for all varea glyphs
axesSelect.js_on_change('value', CustomJS(args=dict(source = source3, source2 = source4, glyphs = glyphs, palette = palette, axesSelect=axesSelect), code="""
  var xlist = [];
  var ylist = [];
  var fullx = source.data['active_axis'].filter(Boolean); //remove nan 
  var fully = source2.data['active_axis'].filter(Boolean); //remove nan
    
  console.log("Length of first source: ")
  console.log(fullx.length)
  console.log("second source: ")
  console.log(fully.length)
  
  const average = (array) => array.reduce((a, b) => a + b) / array.length;
  var n = fullx.length;
  if (fullx.length != fully.length){  //change n to equal length of shortest no nan data 
    console.log("If Entered")
    if (fullx.length < fully.length){
        n = fullx.length;}
    if (fullx.length > fully.length){
        n = fully.length;}
  }
  for (var i = 0; i < n; i++){ //for every value of the shorter data set
      if (i < 3){
        xlist = source.data['active_axis'].slice(-i-3); //in reverse order
        ylist = source2.data['active_axis'].slice(-i-3);
        }
      if (i>3){
        xlist = source.data['active_axis'].slice(-i-3, -i+3);
        ylist = source2.data['active_axis'].slice(-i-3, -i+3);
        }
      const nn = xlist.length
      
      const xmean = average(xlist);
      const ymean = average(ylist);
      
      var xnorm = xlist.map(x => x-xmean);
      var ynorm = ylist.map(x => x-ymean);
      
      const xnormsum = xnorm.reduce((partialSum, a) => partialSum + a, 0);
      const ynormsum = ynorm.reduce((partialSum, a) => partialSum + a, 0);
      
      var xnormsq = xnorm.map(x=> Math.pow(x,2));
      var ynormsq = ynorm.map(x=> Math.pow(x,2));
      
      const xnormsqsum = xnormsq.reduce((partialSum, a) => partialSum + a, 0);
      const ynromsqsum = ynormsq.reduce((partialSum, a) => partialSum + a, 0);
      
      const cornom = xnorm.reduce(function(r,a,i){return r+a*ynorm[i]},0);
      const cordenom = Math.sqrt(xnormsqsum * ynromsqsum);
      const cor = cornom/cordenom
         
      source.data['Cor'][glyphs.length - 1 - i] = cor
      source2.data['Cor'][glyphs.length - 1 - i] = cor
      glyphs[glyphs.length - 1 - i].fill_color = palette[parseInt(((cor + 1) * 200) / 2)]
      
      console.log(cor, "month: ", source.data["Month"][glyphs.length - 1 - i], "Cor: ",source.data['Cor'][glyphs.length - 1 - i], );
  }
  for (var i = 0; i < glyphs.length; i++){
      glyphs[i].y1.field = "Change in " + axesSelect.value;
  };
  source.change.emit()
  source2.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source = source3, source2 = source4, glyphs = glyphs, palette = palette, axesSelect=axesSelect2), code="""
  var xlist = [];
  var ylist = [];
  var fullx = source.data['active_axis'].filter(Boolean); //remove nan 
  var fully = source2.data['active_axis'].filter(Boolean); //remove nan
  
  console.log("Length of first source: ")
  console.log(fullx.length)
  console.log("second source: ")
  console.log(fully.length)
  
  const average = (array) => array.reduce((a, b) => a + b) / array.length;
  var n = fullx.length;
  if (fullx.length != fully.length){  //change n to equal length of shortest no nan data 
    console.log("If Entered")
    if (fullx.length < fully.length){
        n = fullx.length;}
    if (fullx.length > fully.length){
        n = fully.length;}
  }
  for (var i = 0; i < n; i++){ //for every value of the shorter data set
      if (i < 3){
        xlist = source.data['active_axis'].slice(-i-3); //in reverse order
        ylist = source2.data['active_axis'].slice(-i-3);
        }
      if (i>3){
        xlist = source.data['active_axis'].slice(-i-3, -i+3);
        ylist = source2.data['active_axis'].slice(-i-3, -i+3);
        }
      const nn = xlist.length
      
      const xmean = average(xlist);
      const ymean = average(ylist);
      
      var xnorm = xlist.map(x => x-xmean);
      var ynorm = ylist.map(x => x-ymean);
      
      const xnormsum = xnorm.reduce((partialSum, a) => partialSum + a, 0);
      const ynormsum = ynorm.reduce((partialSum, a) => partialSum + a, 0);
      
      var xnormsq = xnorm.map(x=> Math.pow(x,2));
      var ynormsq = ynorm.map(x=> Math.pow(x,2));
      
      const xnormsqsum = xnormsq.reduce((partialSum, a) => partialSum + a, 0);
      const ynromsqsum = ynormsq.reduce((partialSum, a) => partialSum + a, 0);
      
      const cornom = xnorm.reduce(function(r,a,i){return r+a*ynorm[i]},0);
      const cordenom = Math.sqrt(xnormsqsum * ynromsqsum);
      const cor = cornom/cordenom
      
      console.log(cor, " Index: ", i, "Length of Glyphs: ", glyphs.length, "Pallet: ", parseInt(((cor + 1) * 200) / 2));
      source.data['Cor'][glyphs.length - 1 - i] = cor
      source2.data['Cor'][glyphs.length - 1 - i] = cor
      glyphs[glyphs.length - 1 - i].fill_color = palette[parseInt(((cor + 1) * 200) / 2)]
  }
  for (var i = 0; i < glyphs.length; i++){
      glyphs[i].y2.field = "Change in " + axesSelect.value;
      //glyphs[i].fill_color = palette[Math.floor(Math.random()*101)]
  }
  source.change.emit()
  source2.change.emit()
  """))

# ------Use JS to change visibility of events to match radiobutton selection

radio_button_group.js_on_click(CustomJS(args=dict(source = source3, EventSpans = EventSpans, EventLabels = EventLabels), code="""
    if (this.active == 0){
        console.log("First Button")
        for (var i = 0; i < EventSpans.length; i++){
            EventSpans[i].line_alpha = 1};
        for (var i = 0; i < EventLabels.length; i++){
            EventLabels[i].text_alpha = 1};  
  
    };
    if (this.active == 1){
        console.log("Second Button")
        for (var i = 0; i < EventSpans.length; i++){
            EventSpans[i].line_alpha = 1};
        for (var i = 0; i < EventLabels.length; i++){
            EventLabels[i].text_alpha = 0}; 
    };
    if (this.active ==2){
        console.log("Third Button")
        for (var i = 0; i < EventSpans.length; i++){
            EventSpans[i].line_alpha = 0};
        for (var i = 0; i < EventLabels.length; i++){
            EventLabels[i].text_alpha = 0};
    };
    source.change.emit();
"""))

### Update Names of graphs
axesSelect.js_link('value', plot2.title, 'text')
axesSelect2.js_link('value', plot3.title, 'text')

#

# ----plot slider
curdoc().theme = 'dark_minimal'
show(layout(row(Div(text="<b>U.S. Energy Trends:</b>", style={'font-size':'200%'},margin=(0,5,0,5)), 
                Div(text="<i><b>Select, Zoom, Explore</b></i>", style={'font-size':'150%'},margin=(7,5,0,5))), 
            [axesSelect, axesSelect2,slider, radio_button_group], gridplot([[plot1], [plot2], [plot3]], toolbar_options=dict(logo='grey'))))
