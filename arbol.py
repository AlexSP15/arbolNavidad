import math

max = 21
separacion = 5
j = 1

print((separacion+math.ceil(max/2)-j)*" "+"*")

for i in range(1, max, 2):
    fila = (separacion+math.ceil(max/2)-j)*" "
    fila += i*"0"
    j += 1
    print(fila)
