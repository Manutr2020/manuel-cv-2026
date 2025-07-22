import pandas as pd
from geopy.geocoders import Nominatim
import time

df = pd.read_csv("tappe_sicure_tosa_nikki.csv")
df["latitudine"] = None
df["longitudine"] = None

geolocator = Nominatim(user_agent="trova_coordinate")

for index, row in df.iterrows():
    place = row["Nome moderno per Geopy"]
    try:
        location = geolocator.geocode(place)
        if location:
            df.at[index, "latitudine"] = location.latitude
            df.at[index, "longitudine"] = location.longitude
            print("OK")
        else:
            print(f"coordinate non trovate per {place}")
    except Exception as e:
        print(f"è sorto il seguente problema: {e}")
    time.sleep(1)

df.to_csv("tappe_tsurayuki_coordinate.csv")
print("TUTTO FATTO")






