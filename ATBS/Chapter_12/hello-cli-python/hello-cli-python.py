import sys

def main():
    # Read the name from command line arguments
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()