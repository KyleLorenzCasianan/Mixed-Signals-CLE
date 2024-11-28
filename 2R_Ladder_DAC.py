#2R/Ladder DAC
import math

VoSum,Vo = 0,0
VRef = float(input('Enter VRef: '))
Rf = float(input('Enter Rf: '))
R = float(input('Enter R: '))
Digital_input = (input('Enter digital input: '))
Bits = 1 * len(Digital_input)

print(f'Vo = {-VRef}({Rf}/{R}) (', end = '')

for i in range(Bits):
    VoSum += float(Digital_input[i])/math.pow(2,(i+1))
    if i == Bits - 1:
        print(f'{Digital_input[i]}/{math.pow(2, (i + 1))}', end='')
    else:
        print(f'{Digital_input[i]}/{math.pow(2, (i + 1))} + ', end='')

Vo = -VRef * ( (Rf/R) * VoSum)
print(f') = {Vo:.2f}V', '\n')

