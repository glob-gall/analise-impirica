import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Converter as latitudes e longitudes de graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Raio médio da Terra em quilômetros
    raio_terra = 6371.01

    # Diferenças das latitudes e longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Cálculo da fórmula do haversine
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em quilômetros
    distancia = raio_terra * c

    return distancia

# Entrada de exemplo
lat1 = -3.130601
lon1 = -60.02306
lat2 = -3.083550
lon2 = -60.027781

# Cálculo da distância
distancia = calcular_distancia(lat1, lon1, lat2, lon2)

# Arredondar a distância para duas casas decimais
distancia_arredondada = round(distancia, 2)

# Saída
print(distancia_arredondada)
