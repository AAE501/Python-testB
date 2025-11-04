IQTA = 500
IQTB = 700
IQTC = 15

IQ = (IQTA + IQTB) / IQTC
print("The IQ =", IQ)

if IQ > 180:
    print("This indicates Genius")
elif IQ > 120:
    print("This indicates Highly intelligent")
else:
    print("This indicates normal intelligence")