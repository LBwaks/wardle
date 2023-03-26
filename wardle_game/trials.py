birthdays={'Alice':'1 April','johnn':'2 may','kili':'5 dec'}
while True:
    print('Enter a name: (blank to quit)')
    name =input()
    if name =="":
        break
    if name in birthdays:
        print(f'{name}birthday is on {birthdays[name]}')