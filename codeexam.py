x='VIJAYAWADA'

print('Length of the String:',len(x))
a = int(input('Enter index of your choice:'))
print('String from the given Index',x[a:])

print('---------------Traversed String----------------')
for i in x[a:]:
    print(i)

# Find the Ovels in the Given Index
print('---------------Ovel Testing----------------')
b = int(input('Enter index of your choice:'))
ovel = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
if x[b] in ovel:
    print('Hurray! It is an Ovel')
else:
    print('Nah! Consonent')
    


