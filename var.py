""" my_var = 10
print(my_var)  

my_list = [1, 2, 3]
print(my_list)
print(*my_list)

shift + alt + a는 주석 단축키!!
 """

""" # 정수
my_int = 10

# 부동 소수점
my_float = 3.14

# 복소수
my_complex = 3 + 4j
print(my_int)

my_charcte = 'A'
my_char = "@"
print(my_char)

my_string = 'Hello, World!'
str_name = "python"

my_bool = True
bFlag = False
print(bFlag)
 """
 
#my_list = [10, 3, 8, 9, 42, "hello"]
""" print(my_list)
print(my_list.__len__()) 
print(my_list[3])

list_el = my_list[3]
print(list_el)

my_list[3] = "t"
print(*my_list) 
 """
 
""" #print(my_list[3] - my_list[5])

slice_ls = my_list[2:]
print(slice_ls)
 """
 
""" #my_list = [10, 3, 8, 9, 42, "hello", [2, 5, "y"]]
#my_list = [10, 3, 8, 9, 42]
#my_list = ['c', 'z', 'a']
my_list = ['python', 'hello', 'apple']

print(my_list[4][1]) 인덱스 4가 없어서 찾지 못함 오류!!

#my_list.insert(20, "e")
#res = my_list.index(4)
#res = my_list.count(3)
#res = my_list.pop()
res = my_list.sort()
#print(res)

print(my_list) """

""" my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
my_list.reverse()

print(*my_list) """

""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend(list_tmp)

print(*my_list) """

""" my_list = [10, 3, 8, 9, 42,8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend(list_tmp)

print(*my_list)

list_tmp.clear()

print(list_tmp) """

""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

#my_list.remove(3)
my_list.remove(2)

print(*my_list) """

""" my_list = [10,3 ,8, 9, 42, 8, "hello"]

print(my_list)

del my_list[2]

print(*my_list) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.__len__())

#my_tup[2] = 9

print(my_tup.count[6]) """

""" my_tup = (4, 2, 6, 1, "py", "w", ("h, 8, 7, 3"))
print(my_tup) """

""" my_tup = (4, 2, 6, 1, "py", "w)

print(my_tup.index(2, 0, 3)) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index("py", 3, 5)) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index(1, 0, 3)) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}

my_item = my_dict.items()

print(my_item) """

""" idx = ("key1", "key2", "key3")

dicts = dict. fromkeys(idx, "0")

print(dicts) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

print(my_dick["key1"])  """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}

my_str = my_dict.get("key2")

print(my_str) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict.pop("key1"))

print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}

dicts = my_dict.copy()

print(dicts)

print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}     

my_dict["key3"] = "value3"

pritn(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}

my_dict.setdefault("key3")

print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({"key1" : "v4"})

print(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict["key2"]

pritn(my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list = list(my_dict.keys())
print(my_list) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_set = set(my_dict.keys())
print(my_set) """

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.clear()
print(my_dict)