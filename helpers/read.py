import geopandas as gp
import plotly.offline as py
import json
import colorlover as cl

df = gp.read_file("cb_2017_us_county_500k.shp")

#df.tail()

layout = dict(
    hovermode = 'closest',
    xaxis = dict(
        autorange = False,
        range = [-125, -65],
        showgrid = False,
        zeroline = False,
        fixedrange = True
    ),
    yaxis = dict(
        autorange = False,
        range = [25, 49],
        showgrid = False,
        zeroline = False,
        fixedrange = True
    ),
    margin = dict(
        t=20,
        b=20,
        r=20,
        l=20
    ),
    width = 1100,
    height = 650,
    dragmode = 'select'
)

plot_data = []
for index,row in df.iterrows():
    if df['geometry'][index].type == 'Polygon':
        x,y = row.geometry.exterior.xy
        c_x,c_y = row.geometry.centroid.xy
    elif df['geometry'][index].type == 'MultiPolygon':
        x = [poly.exterior.xy[0] for poly in df['geometry'][index]]
        y = [poly.exterior.xy[1] for poly in df['geometry'][index]]
        x_c = [poly.centroid.xy[0] for poly in df['geometry'][index]]
        y_c = [poly.centroid.xy[1] for poly in df['geometry'][index]]        
    else: 
        print('stop')
    county_outline = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "shapes",
            line = dict(color='black', width=1),
            x=x,
            y=y,
            fill='toself',
            fillcolor = 'purple',
            hoverinfo='none'
    )
    hover_point = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "centroids",
            name = row.NAME,
            marker = dict(size=2),
            x=c_x,
            y=c_y,
            fill='toself',
            fillcolor = 'purple'            
    )
    plot_data.append(county_outline)
    plot_data.append(hover_point)

fig = dict(data=plot_data, layout=layout)
py.plot(fig, filename='county_text.html')



#ONLY NY
df2 = df[df['STATEFP'] == '36']


layout_ny = dict(
    hovermode = 'closest',
    xaxis = dict(
        autorange = False,
        range = [-82, -72], 
        showgrid = False,
        zeroline = False,
        fixedrange = True
    ),
    yaxis = dict(
        autorange = False,
        range = [40, 46], 
        showgrid = False,
        zeroline = False,
        fixedrange = True
    ),
    margin = dict(
        t=20,
        b=20,
        r=20,
        l=20
    ),
    width = 800,
    height = 600,
    dragmode = 'select'
)

plot_data_ny = []
for index,row in df2.iterrows():
    if df2['geometry'][index].type == 'Polygon':
        x,y = row.geometry.exterior.xy
        c_x,c_y = row.geometry.centroid.xy
    elif df2['geometry'][index].type == 'MultiPolygon':
        x = [poly.exterior.xy[0] for poly in df2['geometry'][index]]
        y = [poly.exterior.xy[1] for poly in df2['geometry'][index]]
        x_c = [poly.centroid.xy[0] for poly in df2['geometry'][index]]
        y_c = [poly.centroid.xy[1] for poly in df2['geometry'][index]]        
    else: 
        print('stop')
    county_outline = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "shapes",
            line = dict(color='black', width=1),
            x=x,
            y=y,
            fill='toself',
            fillcolor = 'purple',
            hoverinfo='none'
    )
    hover_point = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "centroids",
            name = row.NAME,
            marker = dict(size=2),
            x=c_x,
            y=c_y,
            fill='toself',
            fillcolor = 'purple'            
    )
    plot_data_ny.append(county_outline)
    plot_data_ny.append(hover_point)


fig2 = dict(data=plot_data_ny, layout=layout_ny)
#py.plot(fig2, filename='ny_county_text.html')


#Write back to json
#open('dataNY.json', 'w') as outfile:
    #json.dump(fig2, outfile)


#Test on county data
df3 = pd.read_csv('C01217_FIPS.csv')
df = df2 #just to make it easier to follow tutorial, fix later
df2 = df3 #just to make it easier to follow tutorial, fix later

df['FIPS'] = df['STATEFP'] + df['COUNTYFP']
df3 = pd.merge(df, df2, on='FIPS', how='left')
df3['AMT'].fillna(0.00, inplace=True)


df3_ma = max(df3['AMT'])
df3['amt2max'] = df3['AMT']/df3_ma


bupu = cl.scales['9']['seq']['BuPu']
bupu = cl.interp( bupu, 48 )[32:48]
len(bupu)


#rgb(128,0,128) #purple


df4 = df3
plot_data4 = []
for index,row in df4.iterrows():
    if df4['geometry'][index].type == 'Polygon':
        x,y = row.geometry.exterior.xy
        c_x,c_y = row.geometry.centroid.xy
    elif df4['geometry'][index].type == 'MultiPolygon':
        x = [poly.exterior.xy[0] for poly in df4['geometry'][index]]
        y = [poly.exterior.xy[1] for poly in df4['geometry'][index]]
        x_c = [poly.centroid.xy[0] for poly in df4['geometry'][index]]
        y_c = [poly.centroid.xy[1] for poly in df4['geometry'][index]]        
    else: 
        print('stop')
    #fc = str(int(128*row['amt2max']))
    #fc_rgb = 'rgb(' + fc + ', ' + '0, ' + fc + ')'
    fc = 'rgba(128, 0, 128, ' + str(row['amt2max']) + ')'
    county_outline = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "shapes",
            line = dict(color='black', width=1),
            x=x,
            y=y,
            fill='toself',
            fillcolor = fc,
            hoverinfo='none'
    )
    hover_point = dict(
            type = 'scatter',
            showlegend = False,
            legendgroup = "centroids",
            name = row.NAME,
            text = 'Amt: ' + str(row['AMT']),
            marker = dict(size=2, color='white'),
            x=c_x,
            y=c_y,
            fill='toself',
    )
    plot_data4.append(county_outline)
    plot_data4.append(hover_point)

fig = dict(data=plot_data4, layout=layout_ny)
py.plot(fig, filename='county_C01217_data.html')
