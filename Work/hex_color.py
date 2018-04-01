color_dex = (00, 22, 15)

print('#%02x%02x%02x' % (color_dex[0], color_dex[1], color_dex[2]))
x = '#%02x' % color_dex[2]
print(x)

x = 5
y = 6
op = '+'
res_str ='k =' + str(x)+op+str(y)
res = exec(res_str)
# eval(res_str)
print(res)
# print(m)
# exec