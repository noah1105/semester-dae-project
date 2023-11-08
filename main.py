<<<<<<< HEAD
=======

>>>>>>> 6de209790d341a85864fbda4c0a681fadb9ecce4
# Add another data type, a function 
# List of foods, their cooking instructions, ingredients, and cooking time
food_data = {
    "chicken": {
        "instructions": "1. Preheat the oven to 350°F.\n2. Season the chicken with salt and pepper.\n3. Bake for 45 minutes.",
        "ingredients": ["chicken", "salt", "pepper"],
        "cooking_time": "45 minutes"
    },
    "pasta": {
        "instructions": "1. Boil water in a large pot.\n2. Add pasta and cook for 8-10 minutes.\n3. Drain and serve with your favorite sauce.",
        "ingredients": ["pasta", "water", "sauce"],
        "cooking_time": "8-10 minutes"
    },
    "pizza": {
        "instructions": "1. Preheat the oven to 450°F.\n2. Place the pizza in the oven and bake for 10-12 minutes.",
        "ingredients": ["pizza", "oven"],
        "cooking_time": "10-12 minutes"
    }
}

<<<<<<< HEAD
# Function to print a message about the food being delicious
def print_deliciousness(food_item):
    print(f"The {food_item} is delicious!")

=======
>>>>>>> 6de209790d341a85864fbda4c0a681fadb9ecce4
while True:
    # Prompt the user for their food choice
    user_choice = input("Choose a food item (chicken, pasta, pizza): ").lower()

    # Check if the choice is in the instructions dictionary
    if user_choice in food_data:
        print("Here are the cooking instructions for", user_choice)
        print("Ingredients:", ", ".join(food_data[user_choice]["ingredients"]))
        print("Cooking Time:", food_data[user_choice]["cooking_time"])
        print("Instructions:")
        print(food_data[user_choice]["instructions"])
<<<<<<< HEAD
        print_deliciousness(user_choice)  # Call the function to print the deliciousness message
=======
>>>>>>> 6de209790d341a85864fbda4c0a681fadb9ecce4
    else:
        print("Sorry, I don't have instructions for that food.")

    # Option to repeat or exit
    user_option = input("Do you want to try another food (yes/no)? ").lower()
    if user_option != "yes":
        print("Goodbye!")
        break
