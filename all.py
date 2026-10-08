add = {
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,

        },
        "cost": 3.0,
    }

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_avaliable(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}")
           return False
    return True

