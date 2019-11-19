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
        return 'green'
    elif 1000 <= elevation <3000:
        return 'red'
    else:
        return 'orange'



for lt,ln,el  in zip(lat, lon, elev):  
    map.add_child(folium.Marker(location= [lt,ln], popup= str(el)+ "m", icon=folium.Icon(color= color_produce(el))))
map.save("Map2.html")


