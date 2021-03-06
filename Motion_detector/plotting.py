from motion_detec import df
from  bokeh.plotting import figure, show, output_file

p=figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_width', title="Motion graph")
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1
q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")
output_file("graph.html")
show(p)