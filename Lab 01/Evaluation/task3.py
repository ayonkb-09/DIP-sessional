# Using for loop
sum_for = 0
for i in range(1, 101):
    sum_for += i
print("Sum using for loop:", sum_for)

# Using while loop
sum_while = 0
i = 1
while i <= 100:
    sum_while += i
    i += 1
print("Sum using while loop:", sum_while)

# Simulated do-while loop
sum_do_while = 0
i = 1
while True:
    sum_do_while += i
    i += 1
    if i > 100:
        break
print("Sum using do while loop:", sum_do_while)
