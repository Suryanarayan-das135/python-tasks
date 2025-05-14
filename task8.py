# Write and Append Data to a File

text_to_write = input("Enter text to write to the file: ")
with open("Assignments/Assignment4/output.txt", "w") as file:
    file.write(text_to_write + ", ")
print("Data successfully written to output.txt.")

#  Append additional data to the same file
text_to_append = input("\nEnter additional text to append: ")
with open("Assignments/Assignment4/output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

#  Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("Assignments/Assignment4/output.txt", "r") as file:
    print(file.read())
