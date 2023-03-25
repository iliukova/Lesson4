# Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр,
# сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.

ticket = list(map(int, input("ticket number = ")))
res = "Так, це щасливий квиток" if ticket[0]+ticket[1] == ticket[-1]+ticket[-2] else "Ні, нажаль цей квиток не щасливий."
print(res)