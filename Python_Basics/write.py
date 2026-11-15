# Read the file
# Reverse the list
# Write the list back to the file

# opens and close, no need to do the close:
with open("test.txt", "r") as reader:
    content = reader.readlines()  # [aas, br21, c, dfe3, "e3"]
    rContent = reversed(content)
    with open("test.txt", "w") as writer:
        for line in rContent:
            writer.write(line)
