lines = []
for i in range(0,5):
    str = input(f"Enter line {i+1}:")
    lines.append(str+'\n')
    with open("file.txt", "w") as file:
        file.writelines(lines)

print("Data written to file.txt successfully.")

with open("file.txt", "r") as file:
    content = file.read()
    print("Content of file.txt:")
    print(content)