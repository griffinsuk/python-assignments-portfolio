def equation_for_math(x):
    if not (0 <= x <= 1):
        print("Error!")

    approximation = 0.0
    n = 0
    error_bound = float('inf')

    while error_bound > 0.0001:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        approximation += term
        n += 1

        error_bound = x ** (2 * n + 1) / (2 * n + 1)

    return approximation, n, error_bound

test_values = [-1, 0, 0.25, 0.5, 0.75, 1]
for value in test_values:
    result = equation_for_math(value)
    print(f"equation_for_math({value}) = {result}")