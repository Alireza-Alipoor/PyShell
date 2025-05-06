import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = sys.stdin.readline().rstrip('\n')
        sys.stdout.write(f'{command}: command not found')


if __name__ == "__main__":
    main()
