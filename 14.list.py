#list = used to store multiple items in a single variable

food = ["Pizza🍕","Burger🍔","French Fries🍟","Hot Dog🌭","Pop Corn🍿"]
food[0] = "Meat🍖"

food.append("Sushi🍥")
food.remove("French Fries🍟")
food.sort()
food.reverse()
food.pop()
food.insert(2,"chess🧀")
food.clear()


for i in food:
    print(i)