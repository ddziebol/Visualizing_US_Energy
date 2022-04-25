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
# console.log(source.data['active_axis'][i])

var
fullx = [];
var
fully = [];
fullx = source.data['active_axis'].filter(function(n)
{
return n | | n === 0;
});
fully = source2.data['active_axis']
console.log([0]])
const
n = source.data['active_axis'].length;
if (source.data['active_axis'].length != source2.data['active_axis'].length)
{
    console.log("If Entered")
    if (source.data['active_axis'].length < source2.data['active_axis'].length)
n = source.data['active_axis'].length;
if (source.data['active_axis'].length > source2.data['active_axis'].length)
n = source2.data['active_axis'].length;
}

if (i < 3){

}
if (i < 3){
xlist = source.data['active_axis'].slice(-i-3);
ylist = source2.data['active_axis'].slice(-i-3);
}

var xminmean = xlist.map(element = > element - xmean);


var xsqr = xlist.map(function(x){return Math.pow(x, 2)});
const xsqrsum = xsqr.reduce((partialSum, a) = > partialSum + a, 0);
var ysqr = ylist.map(function(x){return Math.pow(x, 2)});
const ysqrsum = ysqr.reduce((partialSum, a) = > partialSum + a, 0);

var xyminmean = xminmean.reduce(function(r,a,i){return r+a*yminmean[i]},0); // list of xminmean * yminmean, elementwise

const
xsum = xlist.reduce((partialSum, a) = > partialSum + a, 0);
const
xmean = xsum / nn;
let
xminmean = xlist.map(function(x)
{
return x - xmean});

const
ysum = ylist.reduce((partialSum, a) = > partialSum + a, 0);
const
ymean = ysum / nn;
let
yminmean = ylist.map(function(x)
{
return x - ymean});

let xyminmean = xminmean.map(function(r, a, i)
{
return r + a * yminmean[i]});

const xyminmeansum = xyminmean.reduce((partialSum, a) = > partialSum + a, 0);

var xminmeansqr = xminmean.map(function(x)
{return Math.pow(x, 2)});
const xminmeansqrsum = xminmeansqr.reduce((partialSum, a) = > partialSum + a, 0);

var yminmeansqr = yminmean.map(function(x)
{
return Math.pow(x, 2)});
const yminmeansqrsum = yminmeansqr.reduce((partialSum, a) = > partialSum + a, 0);

const cornom = xyminmeansum;
const cordenom = Math.sqrt(xminmeansqrsum * yminmeansqrsum);
const cor = cornom / cordenom;

var
xnorm = xlist.map(function(value)
{
return value - xmean;});
var
xnorm = ylist.map(function(value)
{
return value - ymean;});

//glyphs[i].fill_color = palette[Math.floor(Math.random()*101)]