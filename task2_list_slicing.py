# Task 2: Demonstrate List Slicing

def demonstrate_list_slicing():
    """Creates a list, extracts a slice, reverses it, and displays results."""
    
    numbers = list(range(1, 11))
    print("Original list:", numbers)
    first_five = numbers[:5]
    print("First five elements:", first_five)
    
    # Reverse elements
    reversed_five = first_five[::-1]
    print("Reversed first five elements:", reversed_five)


# Run the program
if __name__ == "__main__":
    demonstrate_list_slicing()
