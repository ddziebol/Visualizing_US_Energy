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