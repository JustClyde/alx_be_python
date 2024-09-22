def draw_square_pattern(size):
    row = 0  
    while row < size:
        for col in range(size):
            print("*", end="")
        print()
        row += 1


def main():
    size = int(input("Enter the size of the pattern: "))

    # Check if the input is a positive integer
    if size > 0:
        draw_square_pattern(size)
    else:
        print("Please enter a positive integer.")