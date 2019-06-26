my_list = [float(input()) for i in range(4)]
list_sum = sum(my_list)
list_avg = sum(my_list) / len(my_list)
list_product = 1
for digit in my_list:
    list_product *= digit
my_list.sort()
print("Sum", ":", "{:.6f}".format(list_sum))
print("Average", ":", "{:.6f}".format(list_avg))
print("Product", ":", "{:.6f}".format(list_product))
print("MAX", ":", "{:.6f}".format(my_list[-1]))
print("MIN", ":", "{:.6f}".format(my_list[0]))
