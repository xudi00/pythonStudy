list1 = ["a","b","c","d",1,2,3] * 2

list1[4] = list1[5] + list1[6]

list1[5] = 100

# print(len(list1))

list1.append('eml')

'''
for index,element in enumerate(list1):
    print(element,index)
'''

# 删除列表中的元素，如果没有会报错 list1.remove(1)


# 报错，int 和 str 两个类型无法一起排列 list2 = sorted(list1)

for index in range(int(len(list1))):
    print(list1[index],end='')