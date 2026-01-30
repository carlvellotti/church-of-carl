#!/usr/bin/env python3
"""beep boop - like fizz buzz but better"""

def beep_boop(n: int) -> str:
    if n % 15 == 0:
        return "beep boop"
    elif n % 3 == 0:
        return "beep"
    elif n % 5 == 0:
        return "boop"
    return str(n)

if __name__ == "__main__":
    for i in range(1, 101):
        print(beep_boop(i))
