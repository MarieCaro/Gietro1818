import folium

m = folium.Map (location = [46.072217, 7.217847], zoom_start=12)

folium.Marker([46.072217, 7.217847],
              popup="Lieu, dégâts",
              icon=folium.Icon(color='red')).add_to(m),

folium.Marker([46.082217, 7.217847],
              popup="Lieu, dégâts",
              icon=folium.Icon(color='red')).add_to(m)

m.save("app/templates/pages/map.html")