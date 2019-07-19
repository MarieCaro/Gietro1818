import folium

m = folium.Map (location = [46.072217, 7.217847], zoom_start=12)

folium.Marker([46.07863, 7.21052],
              popup="Le Châble",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.07937, 7.21661],
              popup="Villette",
              icon=folium.Icon(color='red')).add_to(m),

folium.Marker([46.07165, 7.22454],
              popup="Le Martinet [Martinets]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.06890, 7.22876],
              popup="Le Liappey [Glapey]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.06247, 7.23787],
              popup="Les Places [Places]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.05792, 7.24285],
              popup="Champsec",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.05583, 7.25293],
              popup="Le Freygnoley [Fraignoley]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.05403, 7.26397],
              popup="Lourtier",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.06800, 7.26043],
              popup="Au Mayen",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([	46.10601, 7.10982],
              popup="Granges Neuves",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.03308, 7.30795],
              popup="Fionnay [Fioney]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.02448, 7.32049],
              popup="Le Brecholet [Bressoley]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.02246, 7.32810],
              popup="Bonatchiesse [Bonachissa]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.00279, 7.34290],
              popup="Mauvoisin",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([45.97974, 7.36372],
              popup="Gietro [Giétroz]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([45.97929, 7.35869],
              popup="Torrembet",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([45.94627, 7.36266],
              popup="Boussine [Bussenas]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([45.93440, 7.37289],
              popup="Le Lancet [Lanzet]",
              icon=folium.Icon(color='red')).add_to(m)

folium.Marker([46.074514, 7.155718],
              popup="Sembrancher",
              icon=folium.Icon(color='red')).add_to(m)


m.save("app/templates/pages/map.html")