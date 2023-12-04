string = input('Введите строку:')
message = ''

i = 0

for char in string:

    i+=1

    if (i == 3): 

        print("Третий символ пропущен")
        continue

    if (char == "с"): 

        message += f"с на {i} месте "    

    if (len(string) == i):

        continue    
        
    print("Символ "+ '%.0f' % i + ": " + char)
    
print(f"Длина строки: {len(string)} \n" + message)
