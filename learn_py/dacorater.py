# # # from time import time
# # # def _sum(fun):
# # #     def wrapper(*args, **kwargs):
# # #         t1 = time()
# # #         sum = args[0] + args[1]
# #         # subtraction = args[0] - args[1]
# # #         fun(*args, **kwargs)
# # #         t2 = time()
# # #         print(f"Took {(t2-t1)*1000} seconds to complete")
# # #         return sum
# # #     return wrapper


# # # @_sum
# # # def calculations(a,b):
# # #     print(f"Value a is {a} and Value is {b}")
# # #     return "ThankYou"

# # # if __name__ == "__main__":
# # #     print(f"This value is 10 or 20 calculations :- {calculations(20,10)}")


# # def _sum(a, b):
# #     try:
# #         yield a + b
# #     except:
# #         yield None
# #     yield "ThankYou"

# # if __name__ == "__main__":
# #     gen = _sum(5, 10)
# #     for item in gen:
# #         print(item)


# # ***************************************************************************

# # from time import time

# # def _arithmetic(fun):
# #     def wrapped(*args, **kwargs):
# #         t1 = time()
# #         ob = []
# #         sum = args[0] + args[1]
# #         ob.append(sum)
# #         sub = args[0] - args[1]
# #         ob.append(sub)
# #         mul = args[0] * args[1]
# #         ob.append(mul)
# #         div = args[0] / args[1]
# #         ob.append(div)
# #         t2 = time()
# #         fun(*args, **kwargs)
# #         print((t2 - t1) * 1000)
# #         return ob
# #     return wrapped

# # @_arithmetic
# # def calc(a, b):
# #     print(f"a is :{a} and b is :{b}")
# #     pass

# # print(calc(30, 40))


# # # ***************************************************************************


# # class MyRangeGen:
# #     current = 0

# #     def __init__(self, first, last):
# #         self.first = first
# #         self.last = last

# #     def __iter__(
# #         self,
# #     ):  # <-say that this is an iterator and that __next__ dundar works on it
# #         return self

# #     def __next__(self):
# #         if MyRangeGen.current < self.last:
# #             num = MyRangeGen.current  # current should be remembered as a class object
# #             MyRangeGen.current += 1
# #             return num
# #         raise StopIteration


# # gen = MyRangeGen(0, 5)
# # for i in gen:  # <-'for' loop use 'next' and 'iter' dundar methods to run
# #     print(i)

# # ***************************************************************************
# from functools import reduce

# print("\nUsing labda function")
# my_list = [1, 2, 3]
# print(list(map(lambda my_list_item: my_list_item * 2, my_list)))
# print(list(filter(lambda my_list_item: my_list_item % 2 == 0, my_list)))
# print(reduce(lambda acc, my_list_item: acc + my_list_item, my_list, 0))


# ***************************************************************************


# my_set4 = [value**2 for value in range(1, 10)]
# print(list(my_set4))
print(my_set4)

# simple_list = []
# for value in range(1,10):
#     print(value)
#     print(value**2)
#     simple_list.append(value**2)

# print(simple_list)