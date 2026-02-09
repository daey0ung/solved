a = input()
language_list = ['dz=','c=','c-','d-','lj','nj','s=','z=']
for i in language_list:
    a = a.replace(i,'1')
print(len(a))