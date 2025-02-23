x, y, z = input("Calc: ").split(" ")

x = int(x)
z = int(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

print(f"{answer:.1f}")