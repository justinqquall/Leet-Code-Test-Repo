class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(-x)
            y = []
            counter = 1
            while counter <= len(x):
                y.append(x[-counter])
                counter += 1
            y = int("".join(y)) 
            if y >= 2147483647:
                return 0
            else:
                return -y
        else:
            x = str(x)
            y = []
            counter = 1
            while counter <= len(x):
                y.append(x[-counter])
                counter += 1
            y = int("".join(y)) 
            if y >= 2147483647:
                return 0
            else:
                return y