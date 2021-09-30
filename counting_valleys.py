def countingValleys(steps, path):
    # Write your code here
    velley = 0
    level = 0

    for ch in path:
        if ch == 'U':
            level += 1
        if ch == 'D':
            level -= 1

        if level == 0 and ch == 'U':
            velley += 1 

    return velley



    
if __name__ == "__main__":
    D = 'D'
    U = 'U'
    steps = [D, D, U, U, D, D, U, D, U, U, D]
    result = countingValleys(len(steps), steps)


