import pandas as pd
import folium

df = pd.read_csv("tappe_tsurayuki_coordinate.csv")

#creazione mappa
mappa = folium.Map(
    location=[34.4370,134.8694],
    zoom_start=7,
    tiles="CartoDB positron"
)

#aggiungi marker e popup
for _, row in df.iterrows():
    testo_popup = f"<b>{row['Toponimo antico']}</b><br>{row['Informazione storica']}"

    folium.Marker(
        location = [row["latitudine"], row["longitudine"]],
        popup = testo_popup,
        tooltip = row["Toponimo antico"],
        icon = folium.Icon(icon="tents", prefix='fa') #da font awsome
    ).add_to(mappa)

#salva mappa
mappa.save("tosa_nikki_map.html")
print("mappa creata con successo")


