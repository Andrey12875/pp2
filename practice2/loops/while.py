"""
Python While Loops

A while loop executes a block of code as long as a condition is True.
You must update the condition variable, otherwise the loop will never end.
"""

i = 1
while i < 6:
    print(i)
    i += 1

#example
i = 0
while i < 3:
    print("step", i)
    i += 1

n = 5
while n > 0:
    print(n)
    n -= 1

x = 2
while x <= 16:
    print(x)
    x *= 2

s = 0
k = 1
while k <= 4:
    s += k
    k += 1
print(s)

text = "abc"
idx = 0
while idx < len(text):
    print(text[idx])
    idx += 1
"""
The break statement

break stops the loop even if the condition is still True.
"""

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#example
i = 1
while True:
    print(i)
    if i == 2:
        break
    i += 1

x = 10
while x > 0:
    if x == 7:
        break
    x -= 1
print(x)

nums = [1, 3, 5, 6, 7]
j = 0
while j < len(nums):
    if nums[j] % 2 == 0:
        break
    j += 1
print(j)

i = 0
while i < 100:
    if i * i > 30:
        break
    i += 1
print(i)

attempts = 0
while attempts < 5:
    attempts += 1
    if attempts == 4:
        break
print(attempts)
"""
The continue statement

continue skips the current iteration and moves to the next one.
"""

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#example
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

x = 0
while x < 10:
    x += 1
    if x % 2 == 1:
        continue
    print(x)

text = "a-b-c"
p = 0
while p < len(text):
    if text[p] == "-":
        p += 1
        continue
    print(text[p])
    p += 1

n = 0
while n < 6:
    n += 1
    if n == 5:
        continue
    print(n)

i = 0
while i < 4:
    i += 1
    if i == 1 or i == 3:
        continue
    print(i)
"""
The else statement in while loops

The else block runs when the loop condition becomes False.
It does NOT run if the loop is stopped by break.
"""

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("loop finished")

#example
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("done")

x = 5
while x > 0:
    x -= 1
else:
    print("x reached zero")

k = 1
while k < 4:
    print(k * k)
    k += 1
else:
    print("squares printed")

i = 1
while i < 6:
    if i == 4:
        break
    i += 1
else:
    print("will not run")

s = "zzza"
j = 0
while j < len(s):
    if s[j] == "a":
        break
    j += 1
else:
    print("no a found")