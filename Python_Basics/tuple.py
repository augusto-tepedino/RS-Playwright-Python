values = (1, 2, 'test', 4.5)
print(values[0])
print(values[-1])
print(values[1:3])
print(values)

# Não funciona, tuple é imutável:
# values[2] = 'I'
# print(values)