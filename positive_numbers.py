def positive_numbers(n):
    p_numbers = [num for num in n if num > 0]
    return p_numbers 

list1 = [12, -7, 5, 64, -14]
print("Input: ",list1)
print("Output: ",positive_numbers(list1))
list2 = [12, 14, -95, 3]
print("Input: ",list2)
print("Output: ",positive_numbers(list2))
