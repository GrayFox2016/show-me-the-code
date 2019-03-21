#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量与数据类型

# 变量：不需要声明就可以使用，弱类型
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# 不可以使用保留字

# 基本数据类型

# 整型
# 十进制
int1 = 10
# 十六进制 0x开头
int2 = 0xff00
# 显示数值及类型
print(type(int1))
print(int2)
print(type(int2))

# 浮点型
# 数学写法
float1 = 1.23
# 科学计数法
float2 = 1.23e9

print(type(float1))
print(float2)
print(type(float2))

# 字符串
# 单引号
str1 = 'hello'
# 双引号
str2 = "world"
# 三引号
str3 = '''
hello
world
'''
# 转义
str4 = 'I\'m \"OK\"!'

print(str1)
print(str2)
print(str3)
print(str4)

# 布尔型
bool1 = True
bool2 = False
bool3 = (3 < 2)

print(bool3)

# 
