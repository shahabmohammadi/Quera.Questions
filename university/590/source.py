from math import gcd

if __name__ == "__main__":
    target = input().split(" ")
    a = int(target[0])
    b = int(target[1])
    gcd = gcd(a, b)
    lcm = int((a * b) / gcd)
    print(gcd, lcm)
