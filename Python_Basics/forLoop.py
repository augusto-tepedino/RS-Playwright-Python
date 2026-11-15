#for loop:

obj = [2, 3, 4, 7, 9]
for i in obj:
    print(i)
print('**********')

#sum of numbers from 1 to 5:
sum = 0
for i in range(1, 6): #for(let i = 1; i < 6; i++)
    sum+=i
print(sum)
print('**********')

#numbers from 1 to 5, with a 2 pace:
for i in range(1, 6, 2): #for(let i = 1; i < 6; i+=2):
    print(i)
print('**********')

#no need to have a starting range, so it starts on 0:
for i in range(10): #for(let i = 0; i < 10):
    print(i)