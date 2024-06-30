def check_number(N):
    if N > 0:
        return "positive"
    elif N == 0:
        return "zero"
    else:
        return "negative"


N = -5
result = check_number(N)
print(result)
