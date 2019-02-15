# 判断数字的长度，每个数字出现的次数，个位、十位、百位……依次输出
num = input(">>>:").strip().lstrip('0')
print('num length:{}'.format(len(num)))
num_count_lst=[0]*10
print(num_count_lst)
for i in range(len(num_count_lst)):
    num_count_lst[i]=num.count(str(i))
    if num_count_lst[i]:
        print('{} count:{}'.format(i,num_count_lst[i]))

for j in range(len(num)):
    print(num[-j-1],end=' ')