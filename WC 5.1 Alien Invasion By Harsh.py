x = int(input("Please Enter The Value Of X : "))
y = int(input("Please Enter The Value Of Y : "))
count = 0
if x != y:
    while x != y:
        if x > 1 and y > 1:
            if x % 2 == 0 and y % 2 == 0:
                if x != y and x > y:
                    y = y * 2
                    count = count + 1
                elif x != y and y > x:
                    x = x * 2
                    count = count + 1
                elif x == y:
                    x = x - 1
                    y = y - 1
                    count = count + 1
            elif x % 2 != 0 and y % 2 != 0:
                if x > y:
                    x = x * 2
                    count = count + 1
                elif y > x:
                    y = y * 2
                    count = count + 1
            elif x % 2 == 0 and y % 2 != 0:
                x = x - 1
                y = y - 1
                count = count + 1
            elif y % 2 == 0 and x % 2 != 0:
                x = x - 1
                y = y - 1
                count = count + 1
        elif x == 1:
            x = x * 2
            count = count + 1
        elif y == 1:
            y = y * 2
            count = count + 1
        print(x, y)
if x == y:
    count = count + x
print(count)