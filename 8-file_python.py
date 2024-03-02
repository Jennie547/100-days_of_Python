list_of_numbers = [5, 6, 3, 9, 12]

total_sum = 0

for i in range(len(list_of_numbers)):
    print(list_of_numbers[i], end="")

    if i < len(list_of_numbers) - 1:
        print(" + ", end="")

    total_sum += list_of_numbers[i]

#print("\n")
print(" =", total_sum)
