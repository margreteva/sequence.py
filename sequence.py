# Design an algorithm that generates the first n numbers in the 
# following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line
for i in range (1,n):
    if i == 1:
        current = 1
        first = 1
    elif i == 2:
        current = 3
        second = 3
    elif i == 3:
        current = 3
        third = 3
    else:
        current = first + second + third
        first, second, third = second, third, current
    print(current)