from lib.utils import *

if __name__ == '__main__':
    w = float(input("Enter width (cm): "))
    h = float(input("Enter height (cm): "))
    l = float(input("Enter length (cm): "))
    m = float(input("Enter mass (kg): "))
    print(sort(w, h, l, m))

    # exception captured in the application layer
    try:
        result = sort(100, 100, -50, 10)
        print(result)
    except ValueError as e:
        print("Error:", e)
