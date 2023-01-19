def unique(list):
   checked = {}
   for index, item in enumerate(list):
       if item in checked:
               list.pop(index)
               list.pop(checked[item])
       else:
               checked[item] = index
   return list

print(unique(['apples', 'oranges', 'flowers', 'apples']))
print(unique(['apples', 'apples']))