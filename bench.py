import argparse


def print_help():
    print("Welcome to the algorithm Test Bench\n")
    print("Enter the number corresponding to the algorithm to test:\n")
    print("1: Brute Force\n2: Aho-Corsick\n3: Boyer-Moore\n4: KMP\n5: Rabin-Karp")

def brute_force():
    print("ToDO: Implement me")

def aho_corsick():
    print("ToDo: Implement me")

def boyer_moore():
    print("ToDo: Implement me")

def kmp():
    print("ToDO: Implement me")

def rabin_karp():
    print("ToDo: Implement me")

ALGORITHMS = {
        0: brute_force,
        1: aho_corsick,
        2: boyer_moore,
        3: kmp,
        4: rabin_karp
        }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run pattern matching for string matching')
    parser.add_argument('algo', type=int, help=print_help())
    args = parser.parse_args()

    algo = args.algo
    ALGORITHMS.get(args.algo, brute_force)()

