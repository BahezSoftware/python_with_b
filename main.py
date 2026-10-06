file = open("input.txt", "r")

text = file.read()

file.close()

text = text.replace("\t", "\\t")
text = text.replace("\n", "\\n")
text = text.replace(" ", "_")

output = open("output.txt", "w")

output.write(text)

output.close()

print("File processed successfully.")