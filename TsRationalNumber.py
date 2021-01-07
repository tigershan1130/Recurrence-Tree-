class TsRationalNumber:
    def __init__(self, dividend, divisor):
        # divisor and dividend must be rational numbers
        try:
            self.divisor = int(divisor)
            self.dividend = int(dividend)
        except ValueError:
            self.divisor = 1
            self.dividend = 0        
        return


    def __str__(self):
        return f'{self.dividend}/{self.divisor}'

    # operation override for two rational numbers
    def __add__(self, other):
        lcd = self.lcm(self.divisor, other.divisor)
        
        num1 = (lcd / self.divisor) * self.dividend
        num2 = (lcd /other.divisor) * other.dividend

        res_num = num1 + num2

        return TsRationalNumber(int(res_num), int(lcd))

    # calculate GCD of two numbers
    def gcd(self,a,b):
        if(a == 0):
            return b

        return self.gcd(b % a, a)

    # least common multiple of deonminators
    def lcm(self, a, b):
        return (a * b) / self.gcd(a,b)