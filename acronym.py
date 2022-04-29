user_input = str(input("Enter a phrase "))
a = ""
text = user_input.split()
for i in text:
    a = a + str(i[0]).upper()
print(a)
