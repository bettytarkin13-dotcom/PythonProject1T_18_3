
'''
Targil:
input number from the user (must be between 1-9): 7

1
12
123
1234
12345
123456
1234567
123456
12345
1234
123
12
1

**Bonus (not be in exam): 7
   *
  ***
 *****
*******

'''

k = int(input('Enter length?'))
for i in range(1, k + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()

for i in range(k - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()