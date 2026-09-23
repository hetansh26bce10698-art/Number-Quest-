import random


def generate_number_guess():
    number = random.randint(1, 50)

    return {
        "type": "guess",
        "question": "Guess the number between 1 and 50.",
        "answer": number
    }


def generate_prime_question():
    number = random.randint(2, 50)

    return {
        "type": "prime",
        "question": f"Is {number} a prime number? (yes/no)",
        "answer": is_prime(number)
    }


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def generate_fibonacci_question():
    n = random.randint(5, 10)

    answer = fibonacci(n)

    return {
        "type": "fibonacci",
        "question": f"What is the {n}th Fibonacci number?",
        "answer": answer
    }
