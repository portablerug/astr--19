def function(x):
    return (x**3 + 8)

def main():
    x = 9
    answer = function(x)
    print(f"when x = {(x)}, the function is {answer}")

    if answer > 27:
        print("YAY!")


if __name__ == "__main__":
    main()
     