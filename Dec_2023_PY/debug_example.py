# filename: debug_example.py

def divide_numbers(a, b):
    result = a / b
    return result

def main():
    x = 10
    y = 2
    z = divide_numbers(x, y)
    print(f"The result of {x} divided by {y} is: {z}")

if __name__ == "__main__":
    import pdb

    # Set a breakpoint using pdb
    pdb.set_trace()

    # Call the main function
    main()
