from pet import Pet

def main():
    my_pet = Pet("chuck")

    print("Initial status:")
    my_pet.get_status()

    print("\nAfter eating:")
    my_pet.eat()
    my_pet.get_status()

    print("\nAfter playing:")
    my_pet.play()
    my_pet.get_status()

    print("\nAfter sleeping:")
    my_pet.sleep()
    my_pet.get_status()

    # Bonus: Train and show tricks
    my_pet.train("Sit")
    my_pet.train("Roll Over")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
