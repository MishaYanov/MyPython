import folium
from folium.map import Marker, Popup
import pandas
from pandas.core.accessor import register_dataframe_accessor
#creating a data frame of the volcanos sheet, create list of columns 
volc=pandas.read_excel("MapApp/volcanos.xlsx") 
lat=list(volc["Latitude"])
lon=list(volc["Longitude"])
name=list(volc["Volcano Name"])
hgt=list(volc["Elevation"])

#print(lat)
#print(lon)
#Using html to create a information frame.
html = """<h4>Volcano information:</h4>
Name: %s.<br>
Height: %s m
"""
#Function that creates a height based marker on the map
def VolcColor(elev):
    if elev > 4000:
        return 'red'
    elif 1000<elev<4000:
        return 'orange'
    else:
        return 'green'

#creating an object that stores all the volcanos 
PointVolcano= folium.FeatureGroup(name="Volcanos") 
Population=folium.FeatureGroup(name="Population") 
#Creating my map with folium 
Map=folium.Map(location=[32.10,34.855], zoom_start=6, tiles="Stamen Terrain",max_bounds=True, min_zoom=2)

for i, j, z, x in zip(lat, lon, name, hgt):
    #print(i, j, z ,type(z)) check if everything is correct.
    #the html object that will go as a popup on the map.
    frame=folium.IFrame(html=html %(z,x), width=200, height=100)
    PointVolcano.add_child(folium.CircleMarker(location=[i,j], popup=folium.Popup(frame),radius=6, fill_color=VolcColor(x), color='grey', fill_opacity=1))
#adding a poligon layer to the map 
Population.add_child(folium.GeoJson(data=(open('MapApp\world.json', 'r', encoding="utf-8-sig").read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'yellow' if 10000000<= x['properties']['POP2005'] < 30000000
else 'orange' if 30000000 <=x['properties']['POP2005']<60000000 else 'red' }))

Map.add_child(PointVolcano)
Map.add_child(Population)
Map.add_child(folium.LayerControl())
#creating my map in folder.
Map.save("Map1.html")

