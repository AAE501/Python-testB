user_ch = 'Y'
IQ_n = 0
IQ_sum = 0

while user_ch.lower() == 'y':
    try:
        IQTA = int(input("Enter test A results: "))
        IQTB = int(input("Enter test B results: "))
        IQTC = int(input("Enter test C results: "))

        if IQTC == 0:
            print("Error: Test C result cannot be zero.")
            continue

        IQ = (IQTA + IQTB) / IQTC
        print(f"The IQ = {IQ:.2f}")

        IQ_n += 1
        IQ_sum += IQ

        if IQ > 180:
            print("This indicates Genius")
        elif IQ > 120:
            print("This indicates Highly intelligent")
        else:
            print("This indicates normal intelligence")

    except ValueError:
        print("Please enter valid numeric values.")
        continue

    user_ch = input("Another IQ to calculate? (y/n): ")

if IQ_n > 0:
    IQ_avg = IQ_sum / IQ_n
    print(f"A total of {IQ_n} IQs were calculated with an average of {IQ_avg:.2f}")
else:
    print("No IQs were calculated.")