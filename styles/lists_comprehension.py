initial = [1,2,3,4,5,6,7,8,9]
str = ['alla', 'balla', 'portocala', 'alop']

for x in str:
    x = x + '2'
    print(x)

#str = [x+'4' for x in str if x[0] == 'a']
dictionary ={x:x+'6' for x in str}

print(dictionary)

for x in range(6):
    print(x)

months = ['jan', 'feb', 'mar']
index = [1,2,3,4]

result = {key:value for (key,value) in zip(index, months)}
print(result)

res = [x for x in str if x[0]=='a']
print(res)