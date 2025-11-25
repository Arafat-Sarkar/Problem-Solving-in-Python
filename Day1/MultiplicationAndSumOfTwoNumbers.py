n1, n2 = map(int, input("Enter Two Number: ").split())

def multipl_and_sum(a, b):
    multiplication = a * b
    summation = a + b
    return multiplication, summation

multiplication, summation = multipl_and_sum(n1, n2)

if multiplication < 1000:
    print("The multiplication is:", multiplication)

else:
    print("The sum is:", summation)

