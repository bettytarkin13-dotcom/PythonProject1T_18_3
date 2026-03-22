#Q1-A
def nth_biggest(numbers,n):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    if n>len(unique_numbers)or n<=0:
       return None

    return unique_numbers[n-1]

nums=[88,90,95,95,97,97,97,99,100]
print(nth_biggest(nums,4))