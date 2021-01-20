def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

d = {
        "entree": "beef",
        "drink": "ice coffee",
        "dessert": "ice",
        }
menu(**d)
