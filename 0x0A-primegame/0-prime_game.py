#!/usr/bin/python3
"""Prime game"""


def sieve_of_eratosthenes(max_n):
    """Generates prime numbers up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes


def play_game(n, primes):
    """Simulates a game for a given n and returns the winner
    (0 for Maria, 1 for Ben)."""
    available = [True] * (n + 1)
    available[0] = False
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        move_made = False
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                move_made = True
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                turn = 1 - turn
                break
        if not move_made:
            break
    return 1 - turn  # The player who couldn't move loses, return the winner


def isWinner(x, nums):
    """Determines the overall winner of the game after x rounds."""
    if x < 1 or not nums:
        return None

    # Find the maximum value of n in nums to limit our sieve range
    max_n = max(nums)

    # Generate primes up to max_n
    primes = sieve_of_eratosthenes(max_n)

    # Determine the winner for each game
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n == 1:
            ben_wins += 1  # No prime numbers to pick from
        else:
            winner = play_game(n, primes)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None