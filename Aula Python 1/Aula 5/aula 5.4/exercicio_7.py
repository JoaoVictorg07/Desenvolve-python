op = int(input("(1) maior ou (2) menor?"))
if op ==1:
    result = float("-inf")
    op_function = lambda a,b: a>b
else:
    result = float("inf")
    op_function = lambda a,b: a<b

while True:
    x = int(input())
    if x == 0:break

    if op_function(x, result):
        result = x

print(result)