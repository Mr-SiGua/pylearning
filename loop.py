classmates = ['Michael', 'Bob', "Tracy"]
for name in classmates:
    print(name)
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

# range(5)生成的序列是从0开始小于5的整数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
