class BitManipulation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def bitwise_and(self):
        return self.num1 & self.num2

    def bitwise_or(self):
        return self.num1 | self.num2

    def bitwise_xor(self):
        return self.num1 ^ self.num2
    
num1 = 12 
num2 = 25  

bit_manipulation = BitManipulation(num1, num2)

print(f"Bitwise AND of {num1} and {num2} is: {bit_manipulation.bitwise_and()}")
print(f"Bitwise OR of {num1} and {num2} is: {bit_manipulation.bitwise_or()}")
print(f"Bitwise XOR of {num1} and {num2} is: {bit_manipulation.bitwise_xor()}")
