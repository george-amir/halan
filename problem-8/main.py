def index_of_first_duplicate(list):
    checked = {}
    for index, num in enumerate(list):
            if num in checked:
                    return index
            checked[num] = index

print(index_of_first_duplicate( [ 5, 17, 3, 17, 4, -1 ] ))