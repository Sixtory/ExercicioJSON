import json

f = open('data (1).json', encoding="utf8")
data = json.load(f)

final_data = []

for establishment in data["establishments"]:
    final_object = {"estabelecimento": establishment["name"], "categories": []}
    produtos = [prod for prod in data["products"]
                if prod["id"] in establishment["productsId"]]

    categorias_totais = []

    for category in data["categories"]:
        products = []
        for product in produtos:
            if category["id"] in product["categoriesId"]:
                products.append({"price": float(product["price"])/100})
        if len(products) > 0:
            final_object["categories"].append(
                {"categoria": category["name"], "products": products})

    final_data.append(final_object)


f.close()

json = json.dumps(final_data)

f = open("jsonfinal.json", "w", encoding="utf8", errors="strict")
f.write(json)
f.close()
