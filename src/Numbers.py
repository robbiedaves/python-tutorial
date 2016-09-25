class Numbers:

    @staticmethod
    def numbers_demo():
        # integer numbers are type int
        a = 2 + 2           # 4
        print(a)
        b = 50 - 5*6        # 50 - 30 = 20
        print(b)

        # decimal numbers are type float
        c = 8 / 5           # classic division returns float
        print(c)
        d = 17 // 3         # floor division discards fractional part (17/3 = 5.666) rounded down using //
        print(d)
        e = 17 % 3          # the % operator returns the remained (17/3 = 5.666) : 3 * 5 = 15 : remainder 2
        print(e)

        # mix integers with floats gives you float results
        f = 3 * 3.75 / 1.5  # result 7.5
        print(f)
        g = 7.0 / 2         # result 3.5
        print(g)

        # to the power of
        h = 5 ** 2          # 5 squared
        print(h)
        i = 2 ** 7          # 2 to the power of 7
        print(i)
