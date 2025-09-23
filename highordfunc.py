from functools import reduce
#lambda arg : expr

add = lambda a,b : a+b
print(add(10,20))

square = lambda x : x*x
print(square(6))

#map - map(function,iterable o/p is a map object)

str_list = ['apple','banana','mango']
output_list = list(map(lambda eachval : eachval.upper(), str_list))
print(output_list)

int_list = [1,2,3,4,5]
out_list = list(map(lambda x : x *x , int_list))
print(out_list)

#filter - filter(func,iterable)
out_filter = list(filter(lambda x: x % 2 == 0,int_list))
print(out_filter)

#reduce - reduce(fuction, iterable) - returns a single value take 2 args.
out_reduce = reduce(lambda a,b : a+b, int_list)
print(out_reduce)

#Finding the max num in the list
nums = [10,5,22,7]
out_max = reduce(lambda a,b : a if a > b else b, nums)
print(out_max)


