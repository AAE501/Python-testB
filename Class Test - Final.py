user_ch = 'Y'

while user_ch == 'Y' or user_ch == 'y':
    IQTA = int(input("Enter test A results: "))
    IQTB = int(input("Enter test B results: "))
    IQTC = int(input("Enter test C results: "))

    IQ = (IQTA + IQTB) / IQTC
    print("The IQ =", IQ)

    if IQ > 180:
        print("This indicates Genius")
    elif IQ > 120:
        print("This indicates Highly intelligent")
    else:
        print("This indicates normal intelligence")

    user_ch = input("Another IQ to calculate? (y/n): ")
