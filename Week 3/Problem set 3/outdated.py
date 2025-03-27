months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#enumerates() iterating list to give both index and element
mon = {month: i + 1 for i, month in enumerate(months)}

while True:
    date = input("Date: ").strip()
    if "/" in date:
        try:
            M, D, Y = map(int, date.split("/"))#map() converts list element into give datatype
            if (1 <= D <= 31 and 1 <= M <= 12):
                print(f"{Y}-{M:02}-{D:02}")
                break
        except ValueError:
            pass
    elif "," in date:
        try:
            M, D, Y = date.split(" ")
            M = M.title().strip()
            D = int(D.rstrip(","))#rstrip() remove anything from right side
            Y = int(Y.strip())
            if M in mon and 1<=D<=31:
                print(f"{Y:04}-{mon[M]:02}-{D:02}")
                break
        except (ValueError, KeyError):
            pass
