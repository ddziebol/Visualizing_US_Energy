
glyph = VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in U.S. Coal Production", fill_alpha = 0.5) #renders but does not update.

r = plot1.add_glyph(source3, glyph)

glyph.y2 = "Change in "+Default2 #Illistrates ability to change y out of funciton.



#Did not change anything, rarea stayed the same on select:
axesSelect.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph, axesSelect=axesSelect), code="""
  r.glyph.y1 = "Change in " + axesSelect.value
  r.glyph.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph, axesSelect=axesSelect2), code="""
  r.glyph.y2 = "Change in " + axesSelect.value
  r.glyph.change.emit()
  """))

#woudl erase each area one at a time on select (loose values of whichever one you click):
axesSelect.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph, axesSelect=axesSelect), code="""
  glyph.y1 = "Change in " + axesSelect.value
  source.change.emit()
  """))

axesSelect2.js_on_change('value', CustomJS(args=dict(source = source3, glyph = glyph, axesSelect=axesSelect2), code="""
  glyph.y2 = "Change in " + axesSelect.value
  source.change.emit()
  """))

#mimics the above effect:
glyph1 = VArea(x = 'Month', y1 = "Change in "+Default1, fill_alpha = 0.5) #renders but does not update.
glyph2 = VArea(x = 'Month', y2 = "Change in "+Default2, fill_alpha = 0.5)
r1 = plot1.add_glyph(source3, glyph1)
r2 = plot1.add_glyph(source4, glyph2)