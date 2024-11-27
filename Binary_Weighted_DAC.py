##Binary Weighted DAC
import math

def vosolver(vRef, r, digital_input, bits):
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
Bits = int(input(f'Enter Bits: '))

print(f'Vo = {-Rf}(', end = '')

for i in range(Bits) :
    if Digital_input[i] == '1' :
        VoSum += VRef/((math.pow(2,i))*R)
        print(f' ({VRef} / {((math.pow(2,i))*R)}) +', end = '')
Vo = -Rf * VoSum
print(f') = {Vo:.2f}V')

print(f"{'Binary':<8} {'Analog (V)':<10}")
print("-" * 20)

for i in range(int(math.pow(2,Bits))):
    binary_str = f"{i:0{Bits}b}"  # Format binary number with leading zeros
    Votable = (vosolver(VRef,R, binary_str, Bits))
    print(f'{binary_str:<8} {Votable:.2f}')