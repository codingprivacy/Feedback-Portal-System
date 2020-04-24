__author__ = 'Anindita'

from bokeh.io import show, output_file,export_png
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import FactorRange

#output_file("bars.html")

def call_bar_graph():
        Y_value=[]
        list_val=[['1','1','1','1','0','1','1','1'],['1','0','0','1','0','1','0','1','0'],['0','1','0','1','1','1','0','0','0'],['0','0','0','1','1','0','0','1','0'],['0','0','1','1','0','1','0','1','1']]


        for i in range(len(list_val[0])):
            sum=0
            for j in range(len(list_val)):
                  sum=int(list_val[j][i])+sum
            Y_value.append(sum)


        val_summ_1=(Y_value[1]+Y_value[2])/2
        val_summ_2=(Y_value[3]+Y_value[4])/2
        val_summ_3=(Y_value[5]+Y_value[6])/2
        Y_value_new=[]


        Y_value_new.append(Y_value[0])
        Y_value_new.extend([val_summ_1])
        Y_value_new.extend([val_summ_2])
        Y_value_new.extend([val_summ_3])
        Y_value_new.extend([Y_value[7]])


        #Y_value=[0,0,0,0,0]
        value = ['Punctualtiy', 'Knowledge', 'Commmunication Skills', 'Interaction','Evaluation']
        p1 = figure(x_range=value, plot_height=400,plot_width=700,x_axis_label="Characteristics",y_axis_label="Number of Students", title="Characteristic Graph",toolbar_location=None, tools="")
        p1.vbar(x=value, top=Y_value_new, width=0.9,color="#00b9bc")

        p1.xgrid.grid_line_color = None
        p1.y_range.start = 0

        p1.y_range.end=len(list_val)


        #html_bar=file_html(p,CDN,"my Plot")
        return p1


def call_year_graph():
        #output_file("mixed.html")
        no_reviews=20
        factors = [
            ("2001", "Odd Sem"), ("2001", "Even sem"),
            ("2002", "Odd sem"), ("2002", "Even sem"),
            ("2003", "Odd sem"), ("2003", "Even sem"),
            ("2004", "Odd sem"), ("2004", "Even sem"),

        ]

        p2 = figure(x_range=FactorRange(*factors), plot_height=400,plot_width=700,
                   toolbar_location=None, tools="",title="Life Time Graph",x_axis_label="Time Line",y_axis_label="Number of Students")

        x = [ 10, 16, 9, 8, 12, 14, 14, 16 ]
        p2.vbar(x=factors, top=x, width=0.9,color="red",alpha=0.5)

        p2.line(x=["2001", "2002", "2003", "2004"], y=[12, 9, 13, 14], color="black", line_width=3)


        p2.y_range.start = 0
        p2.y_range.end= no_reviews
        p2.x_range.range_padding = 0.1
        p2.xaxis.major_label_orientation = 1
        p2.xgrid.grid_line_color = None

        #html_year=file_html(p,CDN,"my Plot")
        return p2