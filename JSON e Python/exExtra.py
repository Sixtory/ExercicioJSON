import json

f = open('jsonfinal.json', encoding="utf8")
data = json.load(f)


for estabelecimento in data:
    media = 0
    todosProdutos = 0
    for categorias in estabelecimento['categories']:
        todosProdutos += len(categorias['products'])
        for produto in categorias['products']:
            media += float(produto['price'])
    estabelecimento['avgPrice'] = float("{:.2f}".format(media/todosProdutos))
    print(estabelecimento)

f.close()


def ordemAvPrice(e):
    return e["avgPrice"]


data.sort(key=ordemAvPrice, reverse=True)

json = json.dumps(data)

f = open("jsonmedia.json", "w", encoding="utf8", errors="strict")
f.write(json)
f.close()
