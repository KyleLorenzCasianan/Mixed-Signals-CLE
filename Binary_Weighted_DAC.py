##Binary Weighted DAC
import math

def VoSolver(vRef, r, digital_input, bits):
    voSum = 0
    for i in range(bits):
        if digital_input[i] == '1':
            voSum += vRef / ((math.pow(2, i)) * r)
    vo = -Rf * voSum
    return  vo

VoSum,Vo = 0,0
VRef = float(input(f'Enter VRef: '))
R = float(input(f'Enter R: '))
Rf = float(input(f'Enter Rf: '))
Digital_input = input(f'Enter digital input: ')
Bits = 1 * len(Digital_input)


print(f'Vo = {-Rf}(', end = '')

for i in range(Bits) :
    if Digital_input[i] == '1' :
        VoSum += VRef/((math.pow(2,i))*R)
        if i == Bits - 1:
            print(f'{Digital_input[i]}/{math.pow(2, (i + 1))}', end='')
        else:
            print(f'{Digital_input[i]}/{math.pow(2, (i + 1))} + ', end='')
Vo = -Rf * VoSum
print(f') = {Vo:.2f}V', '\n')

print(f"{'Binary':<8} {'Analog (V)':<10}")
print("-" * 20)

for i in range(int(math.pow(2,Bits))):
    binary_str = f"{i:0{Bits}b}"
    Votable = (VoSolver(VRef, R, binary_str, Bits))
    print(f'{binary_str:<8} {Votable:.2f}')