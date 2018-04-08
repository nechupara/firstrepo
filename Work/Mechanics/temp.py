k_g_dict = {5: 0.8, 10: 1.0, 20: 1.15, 30: 1.3, 40: 1.4, 50: 1.45, 70: 1.6, 100: 1.75}

h = 3

len_dict = len(k_g_dict)
list_k_g = list(k_g_dict)
# print(list_k_g)
print(len_dict)
for i in range(1, len_dict):
    print(i)
    # if list_k_g[i-1] < h < list_k_g[1]:
    #     return
# def find_k_g():
