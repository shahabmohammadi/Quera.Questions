start = int(input())
begin = int(input())
my_list = []


def prime_check(number):
    for i in range(2, number):
        if num % i == 0:
            return False
    return True


for num in range((start + 1), begin):
    if prime_check(num):
        my_list.append(str(num))
print(",".join(my_list))
