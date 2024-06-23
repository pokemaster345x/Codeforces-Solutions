def cambiar(tiempo):
    hh, mm = map(int, tiempo.split(':'))
    if hh == 0:
        return f"12:{mm:02d} AM"
    elif hh < 12:
        return f"{hh:02d}:{mm:02d} AM"
    elif hh == 12:
        return f"12:{mm:02d} PM"
    else:
        return f"{hh-12:02d}:{mm:02d} PM"

t = int(input())

for i in range(t):
    tiempo = input().strip()
    print(cambiar(tiempo))
