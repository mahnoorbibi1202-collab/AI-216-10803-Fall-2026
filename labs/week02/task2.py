usage = float(inut("Enter your internet usage in G :"))
if usage < 0:
    print("Invalid - usage cannot be negative")
elif 0 <= usage <= 5:
     print("Basic")
elif 5 < usage <= 15:
    print("Standard")
else:
    print("Premium")
