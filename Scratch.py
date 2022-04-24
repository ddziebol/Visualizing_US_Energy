# import math
#
# from bokeh.models import ColumnDataSource, CustomJSTransform
# from bokeh.plotting import figure, show
# from bokeh.transform import transform
#
# N = 100
# ds = ColumnDataSource(dict(x=[i / 10 for i in range(N)],
#                            y=[math.sin(i / 10) for i in range(N)]))
# p = figure()
# p.line('x', 'y', source=ds, line_width=3)
# # p.varea(x='x', y1=transform('y', CustomJSTransform(v_func="return xs.map(x => x > 0 ? x : 0)")),
# #         y2=0, source=ds, color='green', fill_alpha=0.5)
# # p.varea(x='x', y1=transform('y', CustomJSTransform(v_func="return xs.map(x => x < 0 ? x : 0)")),
# #         y2=0, source=ds, color='red', fill_alpha=0.5)
#
# p.varea(x='x', y1=transform('y', CustomJSTransform(v_func="return xs.map(x => x > 0 ? x : 0)")),
#         y2=0, source=ds, color='green', fill_alpha=0.5)
# p.varea(x='x', y1=transform('y', CustomJSTransform(v_func="return xs.map(x => x < 0 ? x : 0)")),
#          y2=0, source=ds, color='red', fill_alpha=0.5)
#
# show(p)

print(int(6/2))

glyph.y1.field = "Change in " + axesSelect.value;
glyph.fill_color = 'blue';
glyph2.y1.field = "Change in " + axesSelect.value;
glyph2.fill_color = 'red';

glyph.y2.field = "Change in " + axesSelect.value;
glyph2.y2.field = "Change in " + axesSelect.value;
source.change.emit()

#Works
# view5 = CDSView(source=source3, filters=[IndexFilter([0,1])], name = str(1))
# view6 = CDSView(source=source3, filters=[IndexFilter([1,2])], name = str(2))
#
# glyph = VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in "+Default2, fill_alpha = 0.5, fill_color = palette[1])
# glyph2 = VArea(x = 'Month', y1 = "Change in "+Default1, y2 = "Change in "+Default2, fill_alpha = 0.5, fill_color = palette[2])
#
# plot1.add_glyph(source3, glyph, view = view5)
# plot1.add_glyph(source3, glyph2, view = view6)

# views = [view5, view6]
# glyphs = [glyph, glyph2]
#
# for i in range(len(views)):
#     plot1.add_glyph(source3, glyphs[i], view = views[i])

#Testing