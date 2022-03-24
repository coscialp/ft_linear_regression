import csv
import sys

def model(a, b, x):
    return b + a * x

def normalize(x, mx, mn):
    return (x - mn) / (mx - mn)

if __name__  == '__main__':
    if len(sys.argv) != 2:
        print('Wrong number of arguments!')
        exit(1)

    try:
        x = float(sys.argv[1])
    except:
        print('Not a number!')
        exit(1)

    try:
        with open('data.txt', newline='') as file:
            data = csv.reader(file)
            mx, mn = next(data)
            a, b = next(data)
        x = normalize(x, float(mx), float(mn))
    except:
        a, b = 0, 0


    print(model(float(a), float(b), x))
    
