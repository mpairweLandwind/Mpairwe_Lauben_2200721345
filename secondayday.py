def get_movie_price_and_discount(age):
    
   # Determine the price of a movie ticket and the discount based on the age of the customer.
    
    
    full_price = 2000
    if age < 13:
        discount = 1000
        price = full_price - discount
    elif 13 <= age < 18:
        discount = 500
        price = full_price - discount
    elif 18 <= age < 60:
        discount = 0
        price = full_price
    else:
         # Senior citizens pay more than full price
        price = 5000
    
    return price, discount

# Main function to get user input and display the ticket price and discount
def main():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            price, discount = get_movie_price_and_discount(age)
            print(f"Age: {age}")
            print(f"Discount: shs {discount}")
            print(f"Price of ticket: shs {price}")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

if __name__ == "__main__":
    main()
