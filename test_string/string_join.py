#join用于连接字符串，数字和引用类型则报错，如下：
lst=['1',['2','4'],'3']
lst1=[1,2,3]
print('--'.join(lst))

lst=['a','b','c']
s="I'm a super student"
print(s.rsplit(' ',1))
print(s.find('s',2,-1))
print(s.endswith('nt',5,100))
a=2
b=3
print(a) if a>b else print(b)