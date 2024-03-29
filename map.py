import folium
import pandas


# create an html file using folium.Map
map = folium.Map(location=[38.58,-99.09], zoom_start=6)
# for loop for adding mutliple coordinates
#for coordinates in [[38.58,-99.09],[38.02,-100]]:
data = pandas.read_csv("/Users/vinee/Documents/workspace/code python/UdemyCourse/Mapping/Volcanoes.txt")
# for latitude 
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_produce(elevation):
    if elevation < 1000:
        return 'red'
    elif 1000 <= elevation <3000:
        return 'green'
    else:
        return 'black'

fg_v = folium.FeatureGroup(name = "Volcanoes") # feature group for Volcanoes

# marker layer
for lt,ln,el  in zip(lat, lon, elev):  
    fg_v.add_child(folium.CircleMarker(location= [lt,ln],radius= 6, popup= str(el)+ "m", 
    fill_color= color_produce(el), color = "grey", fill_capicity = 0.7))

fg_p = folium.FeatureGroup(name = "population") # feature group for population

# polygon layer for population
fg_p.add_child(folium.GeoJson(data = open("/Users/vinee/Documents/workspace/code python/UdemyCourse/Mapping/world.json",
"r", encoding = 'utf-8-sig').read(), 
style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fg_v)
map.add_child(fg_p) 

map.add_child(folium.LayerControl()) # layer control for both the layer as they come under fg
map.save("Map2.html")



