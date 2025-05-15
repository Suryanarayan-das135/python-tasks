# Demonstrate List Slicing 

#  Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

#  Extract the first five elements
first_five = numbers[:5]

#  Reverse the extracted elements
reversed_five = first_five[::-1]

#  Print the original, extracted, and reversed lists
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_five)
