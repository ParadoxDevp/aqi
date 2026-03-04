from script import (
    get_AQI_bucket,
    get_CO_subindex,
    get_NH3_subindex,
    get_NOx_subindex,
    get_O3_subindex,
    get_PM10_subindex,
    get_PM25_subindex,
    get_SO2_subindex
)

pollutants = {
    "PM2.5": get_PM25_subindex,
    "PM10": get_PM10_subindex,
    "SO2": get_SO2_subindex,
    "NOx": get_NOx_subindex,
    "NH3": get_NH3_subindex,
    "CO": get_CO_subindex,
    "O3": get_O3_subindex
}

subindices = {}

for pollutant, func in pollutants.items():
    value = float(input(f"Enter {pollutant} value: "))
    subindices[pollutant] = func(value)


avg_aqi = max(subindices.values())
print("AQI:", round(avg, 2))

final_aqi = get_AQI_bucket(avg)
print("The air quality is ", final_aqi)