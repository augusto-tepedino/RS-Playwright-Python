str = "This is a string.demo"
str1 = "  Another string  "

print(str[1])  # h
print(str[0:4])  # This, substring
print(str + str1)  # Concatenation

str2 = "is a"
print(str2 in str)  # substring check


var = str.split(".")
print(var)

str1Trim = str1.strip()
print(str1Trim)
