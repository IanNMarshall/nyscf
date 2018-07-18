import geopandas as gp
import pandas as pd
import numpy as np
import plotly.offline as py
import json
import sys, os
import colorlover as cl
import math
import array
from shapely.ops import cascaded_union


def read_county_shp():
	#print(sys.path)
	#sys.path.append('/nyscfapp1/helpers/')
	df = gp.read_file("/home/upstate_beast/Desktop/projects/nyscf/nyscfapp/nyscfapp1/helpers/cb_2017_us_county_500k.shp")
	#df.tail() #show last few rows
	df = df[df['STATEFP'] == '36'] #ONLY NY
	df['FIPS'] = df['STATEFP'] + df['COUNTYFP']
	#df['FIPS'] = pd.to_numeric(df['FIPS'])
	#print("hello")
	return df

def merge_dfs(df, df2):
	"""Takes 2 data frames: df from county shape file and df2 resulting from query to Dc1 table Group by FIPS"""
	#df2 = pd.read_csv('A00188_FIPS.csv') #Test on county data - ultimately change this to an input
	#add special FIPS cases 1. Out of State, 2. Bad Fips Lookup (zip no FIPS) 3. Unknown Loc. (no fips no)
	#OTHR3 = df2[df2['FIPS'].str.contains('?', na=True)]['AMT'].sum()
	#print(df2[df2['FIPS'].isna])
	OTHR3 = 0
	OTHR3 = OTHR3 + df2[df2.isna().FIPS]['AMT'].sum()#will split this out to other2 at some pnt
	#OTHR2 = df2[df2['FIPS']=='?????']['AMT'].sum()
	OTHR2 = 0 #placeholder until input gives ZIP
	OTHR1 = df2[df2['FIPS'].str.contains('^(?!36)', na=False)]['AMT'].sum() - OTHR2 - OTHR3
	d = {'FIPS': ['OTHR1', 'OTHR2', 'OTHR3'], 
		 'AMT': [OTHR1, OTHR2, OTHR3], 
		 'NAME': ['Other State', 'Bad FIPS Lookup', 'Unknown Location']}
	df_other = pd.DataFrame(data=d)
	df3 = pd.merge(df, df2, on='FIPS', how='left') #left merge we will remove all rows we don't want
	df3 = df3.append(df_other, ignore_index=True, sort=False) #append spec. cases to end of DF add back in FIPS = OTHR*
	df3['AMT'] = pd.to_numeric(df3['AMT'], downcast='float') #Downcast when running agains DB input
	df3['AMT'].fillna(0.00, inplace=True)
	df3_ma = max(df3['AMT'])
	df3['amt2max'] = round(df3['AMT']/df3_ma + .005, 2)
	#rgb(128,0,128) #purple

	return df3



def set_plot_data(df4, filer_FIPS="UNKNW"):
	purp = cl.scales['9']['seq']['Purples']
	purp2 = [[0, purp[0]], [1,purp[-1]]] # should fix this, color bar hack
	
	#more colors by interpolating, look into this later
	#purp = cl.interp( purp, 48 )[32:48]
	#color_match = zip(purp, r)
	
	#fig layout (mostly margins, etc. most options go in data)
	layout_ny = dict(
    hovermode = 'closest',
    xaxis = dict(
        autorange = False,
        range = [-80, -72], 
        showgrid = False,
        zeroline = False,
        fixedrange = False
    ),
    yaxis = dict(
        autorange = False,
        range = [40, 46], 
        showgrid = False,
        zeroline = False,
        fixedrange = False
    ),
    margin = dict(
        t=20,
        b=20,
        r=20,
        l=20
    ),
    width = 800,
    height = 600,
    dragmode = 'select',
	)

	#fig data contains format Polygon objects into x and y coord arrays and append shape dicts.
	plot_data4 = []

	#loop through df contain FIPS, AMT, and Shape info
	for index,row in df4.iterrows():
		if ('OTHR' in row['FIPS']): #special cases
			if row['FIPS'] == 'OTHR1':
				x = array.array('d', [-78.0, -78.5, -78.5, -78.0, -78.0])
				y = array.array('d', [45.0, 45.0, 45.5, 45.5, 45.0])
				c_x = array.array('d', [-78.25])
				c_y = array.array('d', [45.25])

			elif row['FIPS'] == 'OTHR2':
				x = array.array('d', [-78.6, -79.1, -79.1, -78.6, -78.6])
				y = array.array('d', [45.0, 45.0, 45.5, 45.5, 45.0])
				c_x = array.array('d', [-78.85])
				c_y = array.array('d', [45.25])

			elif row['FIPS'] == 'OTHR3':
				x = array.array('d', [-79.2, -79.7, -79.7, -79.2, -79.2])
				y = array.array('d', [45.0, 45.0, 45.5, 45.5, 45.0])
				c_x = array.array('d', [-79.45])
				c_y = array.array('d', [45.25])
		else: #normal polygon
			if df4['geometry'][index].type == 'Polygon':
			    x,y = row.geometry.exterior.xy
			    c_x,c_y = row.geometry.centroid.xy
			elif df4['geometry'][index].type == 'MultiPolygon':
				#create list of float arrays for x and y polygons. we will loop through later
			    x = [poly.exterior.xy[0] for poly in df4['geometry'][index]]
			    y = [poly.exterior.xy[1] for poly in df4['geometry'][index]]
			    #merge multiPolygon obj with cascaded_union for centroid calc.
			    polygons = [poly for poly in df4['geometry'][index]]
			    u_polygons = cascaded_union(polygons)
			    c_x,c_y = u_polygons.centroid.xy

			else: #something is broken
				print('stop')
	    #fc = str(int(128*row['amt2max']))
	    #fc_rgb = 'rgb(' + fc + ', ' + '0, ' + fc + ')'
		fc = 'rgba(128, 0, 128, ' + str(row['amt2max']) + ')'
	    #print (len(purp))
	    #print (index, int(math.floor(row['amt2max']*(len(purp)-1))))
		fc1 = purp[int(math.floor(row['amt2max']*(len(purp)-1)))]
		#highlight filers county if we have it
		if (row['FIPS']==filer_FIPS):
			line_color = 'red'
			line_w = 2
			mark_color = 'red'
			h_text = "Filer's Home County: " + row['NAME'] + ' | Amt: ' + str(row['AMT'])
		else: 
			line_color = 'black'
			line_w = 1
			h_text = 'County: ' + row['NAME'] + ' | Amt: ' + str(row['AMT'])
			mark_color = 'white'

		#special case
		if ('OTHR' in row['FIPS']):
			county_outline = dict(
			    type = 'scatter',
			    showlegend = False,
			    legendgroup = "shapes",
			    line = dict(color=line_color, width=line_w),
			    mode = "lines", #added since default for lt 20 coords gives line and marker
			    x=x,
			    y=y,
			    fill='toself',
			    fillcolor = fc1,
			    hoverinfo='none',
			)
			plot_data4.append(county_outline)



		elif df4['geometry'][index].type == 'Polygon':
			county_outline = dict(
			    type = 'scatter',
			    showlegend = False,
			    legendgroup = "shapes",
			    line = dict(color=line_color, width=line_w),
			    mode = "lines", #added since default for lt 20 coords gives line and marker
			    x=x,
			    y=y,
			    fill='toself',
			    fillcolor = fc1,
			    hoverinfo='none',
			)
			plot_data4.append(county_outline)
		#multipolygon county, loop coordinate arrays
		else:
			for i in range(len(x)):
				county_outline = dict(
				    type = 'scatter',
				    showlegend = False,
				    selectedpoints = [],
				    legendgroup = "shapes",
				    line = dict(color=line_color, width=line_w),
				    mode = "lines",
				    x=x[i],
				    y=y[i],
				    fill='toself',
				    fillcolor = fc1,
				    hoverinfo='none',
				)
				plot_data4.append(county_outline)
		hover_point = dict(
		        type = 'scatter',
		        showlegend = False,
		        legendgroup = "centroids",
		        name = row.NAME,
		        #text = 'County: ' + row['NAME'] + ' | Amt: ' + str(row['AMT']) + " | fc: " + fc1 + " lev: " + str(int(math.floor(row['amt2max']*(len(purp)-1)))),
		        text = h_text,
		        marker = dict(size=2, color=mark_color),
		        x=c_x,
		        y=c_y,
		        fill='toself',
		)
		plot_data4.append(hover_point)
		#print(row['NAME'])
		#print(county_outline['x'],  county_outline['y'])

	
	#colorbar
	max_rnd = 10**(math.floor(math.log(max(df4['AMT']), 10)) - 2) #since we have eighths should do minus 2
	cb_ticktext = [max_rnd*(math.ceil(t*max(df4['AMT']/8)/max_rnd)) for t in range(9)]
	cb_tickvals = [t/8 for t in range(9)]
	plot_data4.append( dict(
		y = df4.amt2max,
	    mode='markers',
	    showlegend=False,
    	marker=dict(
	        #size=16,
	        color = cb_tickvals, #purp, #df4.amt2max, #set color equal to a variable
	        colorbar = dict(title='USD', tickmode='array', tickvals=cb_tickvals, ticktext=cb_ticktext),
	        #colorscale=['rgba(128,0,128, 0.0)', 'rgba(128,0,128, 1.0)'],
	        #colorscale=[[0, 'rgba(128,0,128, 0)'],  [1, 'rgba(128,0,128, 1)']],
	        colorscale = purp2,
	        showscale=True,
	    	)
	) )

	fig = dict(data=plot_data4, layout=layout_ny)
	return fig

def get_div(fig):
	return py.plot(fig, include_plotlyjs=False, output_type='div')


def gen_plot(fig):
	py.plot(fig, filename='county_C01217_data.html')



#Write back to json
# with open('dataNY2.json', 'w') as outfile:
#     json.dump(plot_data4, outfile)



### Py Plot example

# fig5 = ff.create_choropleth(
#     fips=fips, values=values,
#     scope='NY', county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
#     legend_title='Conts by County')
