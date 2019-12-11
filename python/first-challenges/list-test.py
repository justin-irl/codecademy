list = [1, 2, 3, 4, 5, 6, 7]

print(list)

def cut_list(lst, start, end):
    lst_start = start + 2
    lst_end =  end - 1

    return lst_start # + lst_end

# (remove_middle([4, 8, 15, 16, 23, 42], 1, 3)

lst1 = [4, 8, 15, 16, 23, 42]
print(lst1[:1])

move = lst1[:1 + 1]
print(str(move) + "moved")

lst2 = [4, 8, 15, 16, 23, 42]
print(lst2[3:])

end = 3
move2 = lst2[1 + end:]
print(str(move2) + " moved2")

print(lst1[:1]+lst2[3:])