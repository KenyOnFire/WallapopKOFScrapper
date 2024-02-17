import requests

# URL base
base_url = "https://api.wallapop.com/api/v3/general/search"

# Parámetros de búsqueda
params = {
    "filters_source": "quick_filters",
    "keywords": "iphone 13 mini",
    "longitude": -3.69196,
    "latitude": 40.41956,
    "min_sale_price": 200,
    "max_sale_price": 700,
    "distance": 10000,
    "time_filter": "lastWeek",#"today",
    "order_by": "price_low_to_high"
}

# Encabezado de agente de usuario (Recomendado hacer una rotacion de el user-agent con algun modulo de python que nos lo permita)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# Realizar la solicitud con los parámetros y el encabezado
response = requests.get(base_url, params=params, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear los datos JSON
    data = response.json()
    # Filtrar los datos si es necesario
    search_objects = data.get("search_objects", [])
    new_objects = []
    if search_objects:
        for item in search_objects:
            if "13" in item["title"] and item["flags"]["reserved"] == False:
                new_objects.append(item["title"])
                #print("Reservado:", item["flags"]["reserved"])
                print("Title:", item["title"])
                #print("Description:", item["description"])
                print(f"URL: https://es.wallapop.com/item/{item['web_slug']}")
                print("Price:EUR", item["price"])
                #print("Price -50EUR:", (item["price"] - 50))
                #print("Images:", item["images"])
                #print("\n")
                pass
    else:
        print("No se encontraron resultados.")
else:
    print("Error al realizar la solicitud. Código de estado:", response.status_code)
print(len(new_objects))
