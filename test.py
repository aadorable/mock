# *** coding: utf-8 ***
#@Time   : 2020/12/4 15:25
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test.py

# num1 = input('请输入第一个数字：')
# num2 = input('请输入第二个数字：')
# num3 = input('请输入第三个数字：')
#
# if num1.isdigit() and num2.isdigit() and num3.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     num3 = int(num3)
#     all_num = [num1, num2, num3]
#     print(all_num)
#     sort_num = []
#     for i in range(0, len(all_num)):
#         sort_num.append(max(all_num))
#         all_num.remove(max(all_num))
#     print(sort_num)
#
#
#     # all_num.sort(reverse=False)
#     # for i in range(0, len(all_num)):
#     #     for j in range(0, len(all_num)-1-i):
#     #         if all_num[j] > all_num[j+1]:
#     #             temp = all_num[j]
#     #             all_num[j] = all_num[j+1]
#     #             all_num[j+1] = temp
#     # print('排序的结果是：{}'.format(all_num))
# else:
#     print('非法的数字')



# def Fibonacci(num):
#     if num <= 0:
#         print('请输入一个正整数')
#     if num == 1:
#         print('斐波拉契数列：[0]')
#     elif num == 2:
#         print('斐波拉契数列：[0, 1]')
#     else:
#         n1 = 0
#         n2 = 1
#         count = 2
#         fib_list = [0, 1]
#         while count < num:
#             n3 = n1 + n2
#             fib_list.append(n3)
#             n1 = n2
#             n2 = n3
#             count += 1
#         print('斐波拉契数列：{}'.format(fib_list))
#
# def Fib(num):
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return Fib(num - 1) + Fib(num - 2)
#
#
# if __name__ == '__main__':
#     num = input('请输入斐波拉契数列项数：')
#     if num.isdigit():
#         fib_list = Fibonacci(int(num))
#     else:
#         print('非法项数')
#
#     for i in range(1, 11):
#         print(Fib(i), end=' ')


a = ['a', 'b', 'c']
b = ', '.join(a)
print(b)