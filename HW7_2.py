numbers = [int(input()) for _ in range(10)]

remainders = [num % 42 for num in numbers]

print(len(set(remainders)))