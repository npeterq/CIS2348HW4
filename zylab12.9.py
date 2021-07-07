"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"12.9 CIS 2348 LAB: Exception handling to detect input string vs. integer"

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except Exception as ex:
        age = 0
    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]