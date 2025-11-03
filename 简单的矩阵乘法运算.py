import sympy as sp

#定义符号变换
x1,x2,x3 = sp.symbols("x1,x2,x3")

#定义矩阵
A = sp.Matrix([
    [1,2,3],
    [4,5,6]
])

#输入向量
x = sp.Matrix([x1, x2, x3])

y = A * x

print("符号表示：")
print(f"y = {y}")

