
def create_inventory(items):
    diccionario = dict()
    for item in items:
        if item in diccionario:
            diccionario[item] += 1
        else:
            diccionario[item] = 1
    return diccionario

lista = (["coal", "wood", "wood", "diamond", "diamond", "diamond"])
print(create_inventory(lista))
def add_items(inventory, items):#el diccionario ya fue creado y se llama inventory
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

diccionario= {"coal":3, "diamond":1, "iron":5}
lista = ["diamond", "coal", "iron", "iron"]
print(decrement_items(diccionario, lista))

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory
diccionario = {"coal":2, "wood":1, "diamond":2}
palabra = "coal"
print(remove_item(diccionario, palabra))

def list_inventory(inventory):
   resultado = []
   for key, value in inventory.items():
       if value > 0:
           resultado.append((key, value))# si pongo un solo parentesis pareceria que estoy pasasdo dos argumentos por separado
   return resultado
