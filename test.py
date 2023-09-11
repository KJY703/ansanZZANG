my__set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print (my__set)
print (setItem)

my_set = set([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")
print(set_tmp)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
print(my_set.union(set_item))

print(my_set - set_item)
print(my_set.difference(set_item))

print(my_set & set_item)
print(my_set.intersection(set_item))

my_set.add(9)
print(my_set)

my_set.update([5, 9, 7, 4])
print(my_set)

my_set.clear()
print (my_set)

my_set.update([5, 8, 3, 7, 1, "h"])

my_set.remove(5)
print(my_set)

my_set.discard(2)
print (my_set)

my_set.update([5])

my_set.difference_update(set_item)
print(my_set)

my_int = 10
my_str = str(my_int)
print(my_int)
print(my_str)

my_int = 10
print(my_int)

print(my_int + 10)

my_str = str(my_int)

print(my_str)

print(my_str + 10)

print(my_str + " hello")

my_str = '10'
my_int = int(my_str)
