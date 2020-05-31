messages = input(">")
words = messages.split()
length = len(messages)




encode = {
    "a": "*",
    "b": "#"
}
onebyone =" "
output =" "
for i in range(length):
    onebyone += messages[i]

for word in onebyone:
    output += encode.get(word, word) + " "
print(output)



