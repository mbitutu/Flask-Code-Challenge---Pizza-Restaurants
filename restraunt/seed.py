from random import randint, choice
from restraunt.app import app, db, Restaurant, Pizza, Restaurant_Pizza

# Sample names for restaurants and pizzas
restaurant_names = [
    "Tasty Eats",
    "The Pizza Place",
    "Italiano Delight",
    "Gourmet Grill",
    "Spicy Bites",
    "Café Roma",
    "Sushi Haven",
    "Mama's Kitchen",
    "Peppy Pies",
]

pizza_names = [
    "Classic Margherita",
    "Pepperoni Perfection",
    "Hawaiian Luau",
    "Meat Feast",
    "Veggie Delight",
    "BBQ Bliss",
    "Buffalo Ranch",
    "White Wonder",
    "Four Cheese Pleasure",
]

addresses = [
    "123 Elm Street",
    "456 Oak Avenue",
    "789 Maple Lane",
    "101 Cedar Road",
    "202 Pine Drive",
]

ingredients = [
    "Tomato sauce", "Mozzarella cheese", "Pepperoni", "Pineapple",
    "Sausage", "Mushrooms", "Onions", "Bell peppers", "Olives",
]

with app.app_context():
    db.create_all()

    Restaurant.query.delete()
    Pizza.query.delete()
    Restaurant_Pizza.query.delete()

    restaurant_list = []
    pizza_list = []

    # Generate 5 restaurants
    for name in restaurant_names:
        address = choice(addresses)
        restaurant = Restaurant(name=name, address=address)
        restaurant_list.append(restaurant)

    db.session.add_all(restaurant_list)
    db.session.commit()

    # Generate 9 pizzas
    for name in pizza_names:
        ingredients_list = [choice(ingredients) for _ in range(3)]
        pizza = Pizza(name=name, ingredients=", ".join(ingredients_list))
        pizza_list.append(pizza)

    db.session.add_all(pizza_list)
    db.session.commit()

    # Link pizzas and restaurants to the RestaurantPizza table
    for restaurant in restaurant_list:
        for pizza in pizza_list:
            price = randint(10, 50)
            restaurant_pizza = Restaurant_Pizza(
                restaurant=restaurant,
                pizza=pizza,
                price=price
            )
            db.session.add(restaurant_pizza)

    db.session.commit()

print("Sample data seeded successfully.")

