#Quantizing and Encoding Method
import  math

Level = int(input('Enter Number of bits (N): '))
VMax = int(input('Enter VMax: '))
VMin = int(input('Enter VMin: '))

Step_Size = (VMax-VMin) / math.pow(2,Level)
print(f'q = ( ({VMax}) - ({VMin}) ) / 2^{Level} = {Step_Size:.2f} V', '\n')

print(f"{'Level':<8} {'Binary':<8} {'Voltage (V)':<10}")
print("-" * 30)

for i in range(int(math.pow(2,Level))):
    binary_str = f"{i:0{Level}b}"
    print(f'{i:<8} {binary_str:<8}  {VMin + (Step_Size * i):.2f}')