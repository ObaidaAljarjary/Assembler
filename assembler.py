# By Obaida Ismail
file = open("assembly.txt", "r")
x = file.read()
file.close()
lst = x.split("\n")
print(lst)
pointer = int(lst[0].replace('org ', ''))
del lst[0]
c = pointer - 1
find_code_segment = False
for line in lst:
    c += 1
    if "db" in line or "dq" in line or "dw" in line:
        try:
            print(line[:line.index(" db")], f":{c}")
        except:
            try:
                print(line[:line.index(" dw")], f":{c}")
            except:
                print(line[:line.index(" dq")], f":{c}")

    if line == ".code":
        find_code_segment = True
    if ":" in line and find_code_segment:
        print(f"{line[:line.index(':')]}:{c}")

