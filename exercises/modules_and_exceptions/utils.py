def celsius_to_fahrenheit(c):
    F = c * 9/5 + 32
    return F
def fahrenheit_to_celsius(F):
    c = (F - 32) * 5/9
    return c

if __name__ == "__main__":
    print(celsius_to_fahrenheit(37))
    print(fahrenheit_to_celsius(98.6))