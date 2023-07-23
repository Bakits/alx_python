def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for i in range(2, n):
        next_fibonacci = sequence[-1] + sequence[-2]
        sequence.append(next_fibonacci)

    return sequence
