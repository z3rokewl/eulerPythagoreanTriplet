import math


def triplet_generator():
    for a in range(1,500):
        for b in range(1,500):
            c = math.sqrt(a**2 + b**2)
            if int(c) == c:
                if a + b + c == 1000:
                    return (a,b,c)



def main():
    triplet = triplet_generator()
    print triplet[0] * triplet[1] * triplet[2]
    return 0 


if __name__ == '__main__':
    main()