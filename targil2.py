num=input("Enter a number: ")

reversed_num = num[::-1]
print("Reversed:", reversed_num)

digits = [int(d) for d in num]

max_digit = max(digits)
print("Max digit:", max_digit)

min_digit = min(digits)
print("Min digit:", min_digit)

total=sum(digits)
print("sum:", total)

avg=total/len(digits)
print("Average:", avg)

