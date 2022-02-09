def len_list(par, count=0):
    for i in par:
        count += 1
    return count


j = [9, 8, 7, 6]
h = ['a', 'b', 'c']
k = [9, 8, 7, 5, 7, 5]

print(len_list(h))
