# Read a File and Handle Errors

try:
    print("Reading file content:")
    with open("Assignments/Assignment4/sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


