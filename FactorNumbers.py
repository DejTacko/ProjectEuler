num = int(input("To be fractured"))
output = []
output_str = ""
stop = False
power = 0

def primegen(n):
    if n< 2:
        return False

    for i in range(2,n):
        if n%i == 0:
            return False

    return True

for i in range(1, num):
    if primegen(i):
        while num % i == 0:
            num = num / i
            print(i)
            power = power + 1
            if num == 1:
                stop = True

        if power != 0:
            output.append(i)
            if power != 1:
                output.append('^')
                output.append(power)

            output.append('*')
            power = 0

    if stop == True:
        break

del output[-1]
placeholder = [str(i) for i in output]
output_str = ''.join(placeholder)
print(output_str)
