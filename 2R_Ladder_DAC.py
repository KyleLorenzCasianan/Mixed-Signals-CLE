import math

VRef = float(input('Enter VRef: '))
Rf = float(input('Enter Rf: '))
R = float(input('Enter R: '))
Digital_input = (input('Enter digital input: '))
Bits = int(input(f'Enter Bits: '))
VoSum,Vo = 0,0

print(f'Vo = {-VRef}({Rf}/{R}) (', end = '')

for i in range(Bits):
    VoSum += float(Digital_input[i])/math.pow(2,(i+1))
    print(f'{Digital_input[i]}/{math.pow(2,(i+1))} + ', end ='')
Vo = -VRef * ( (Rf/R) * VoSum)
print(f') = {Vo:.2f}')