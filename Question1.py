def search(str, lst, size):
    result = -1
    for i in range(first,size):
        if lst[i]==str:
            result = 1
    return result


str = 'a'
lst = ['f','g','c','a']
size = 4
first = 0

print(search(str,lst,size))