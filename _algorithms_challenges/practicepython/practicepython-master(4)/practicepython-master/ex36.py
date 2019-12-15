#to plot the birthday month count onto a html file using bokeh library

from bokeh.plotting import figure, show, output_file
import ex35
from collections import Counter
#specifying the output file

x = []
y = []
monthlist = ex35.count_birthday_months()
c = Counter(monthlist)
print c
for k,v in c.items():
        print "%s : %s"%(k,v)
	x.append(int(k))
	y.append(int(v))



output_file("plot.html")


#create a figure
p = figure()
p.vbar(x=x, top=y, width=0.5)

#render / show the plot
show(p)


