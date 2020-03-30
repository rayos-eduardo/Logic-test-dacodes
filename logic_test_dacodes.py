while True:
    try:
        t = int(input('T value: '))
    except (ValueError):
        print("Please enter a valid number for T.\nIt must be between 1-5000")
        continue
    if not(1 <= t <= 5000):
        print("Please enter a valid number for T.\nIt must be between 1-5000")
        continue   
    else:
        break
              

for x in range(t):
    while True:
        try:
            n, m = map(int, input("Values for N and M: ").split())
        except ValueError:
            print("Please enter a valid number for n and/or m, at this format 'n m'.\nThey must be numbers between 1-10^9")
            continue
        if not(1 <= n <= pow(10,9)):
            print("Please enter a valid number for T.\nIt must be between 1-5000")
            continue
        if not(1 <= m <= pow(10,9)):
            print("Please enter a valid number for T.\nIt must be between 1-5000")
            continue  
        else:
            break
              
    if (n % 2 == 0):
        if (n > m):
            direction = 'U'
        else:
            direction = 'L'
    else:
        if (n == m):
            direction = 'R'
        else:
            direction = 'D'

    print(direction)
        
        
            
