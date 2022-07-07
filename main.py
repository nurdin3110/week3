# shop_cash = [10000, 34000, 30000, 12300, 45000, 90000,78000]
# expenses = [10000, 3000, 20000, 5000, 5600, 7654, 3425]
# all_cash = sum(shop_cash)
# all_expenses = sum(shop_cash)
# profit = all_cash - all_expenses
# print(profit)

# shop_cash = [10000, 34000, 30000, 12300, 45000, 90000,78000]
# expenses = [10000, 3000, 20000, 5000, 5600, 7654, 3425]
#
#
# def get_many(shop_cash, expenses):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit
#
# mon = get_many(shop_cash, expenses)
# print(mon)


# *args **kwargs
#
#
# def get_arguments(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
# # get_arguments(1, 2, 3, "dffgg", {1, 0}, name="Nazgul", age=26)
#
# d = {
#     "name": "nazgul",
#     "age": 26
# }


def get_list_square(*args):
    result = []
    if args:
        for i in args:
            result.append(i**2)
    return result
print(get_list_square(1, 3, 7, 11))

