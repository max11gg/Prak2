NumD = 0
year = float(input('Введите год:'))

if year % 4 == 0:
    fevr = 29
else:
    fevr = 28
Mass = [31, fevr, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for kol in range(len(Mass)):
    for num in range(Mass[kol]):
       num += 1
       NumD += sum(map(int, str(num)))
print(NumD)