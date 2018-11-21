dataset = {
        "bob@gmail.com": {
                            "human": {
                                        "name": "bob",
                                        "age": 19
                                    },
                            "food": {
                                        "sup": {
                                                "carrot": 2 ,
                                                "onion": 1 ,
                                                "water": 3
                                              },
                                        "salat": {
                                                "salat": 2 ,
                                                "onion": 1,
                                                "tomat": 3
                                                }
                                    }
                        },

    "boba@gmail.com": {
        "human": {
            "name": "boba",
            "age": 19
        },
        "food": {
            "sup": {
                "carrot": 2

            }
        }
    }

}
def getNames(dataset, keys):
    if keys==[]:
        return
    key = keys[0]
    name = dataset[key]["human"]["name"]
    print(name)
    getNames(dataset, keys[1:])
getNames(dataset,list(dataset.keys()))

for key in list(dataset.keys()):
    humanName = dataset[key]["human"]["name"]


    products = set()
    for food in dataset[key]["food"].values():
        for product in food:
            products.add(product)
    print(humanName,len(products))
    productSum = 0
    for food in dataset[key]["food"].values():
        for product in food.values():
            productSum+= product
    print(humanName,productSum)
