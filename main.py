from os import system, name
from time import sleep


def clear():
    if name == "nt":
        _ = system("cls")


for i in range(4):
    print("Searching for Hackers.")
    sleep(0.5)
    clear()
    print("Searching for Hackers .")
    sleep(0.5)
    clear()
    print("Searching for Hackers  .")
    sleep(0.5)
    clear()

clear()

s = "Found all Hackers"
d = "Displaying"

# print(dl)

print(s)


clear()
print(d)
with open("names.txt", "r", encoding="utf8") as file:
    txtname = file.read()

lstname = txtname.replace("\n", "$")
name = lstname.split("$")
name.pop()

for i in name:
    print(i)
    sleep(0.4)

sleep(5)