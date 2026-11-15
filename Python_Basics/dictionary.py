values = {1:'2', 2:'3', 'test':'tested', 4:4.5}
print(values[1])

print(values[2])
print(values['test'])
print(values)

values.popitem()
print(values)

values.pop(1, 'testw')
print(values)

del values['test']
print(values)

values['banana'] = 'yellow'
print(values)

# Não funciona, tuple é imutável:
# values[2] = 'I'
# print(values)