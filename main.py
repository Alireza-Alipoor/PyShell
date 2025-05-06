import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command, *args = sys.stdin.readline().rstrip('\n').split()
        except ValueError:
            continue
        match command:
            case 'exit':
                exit()
            case 'echo':
                sys.stdout.write(' '.join(args)+'\n')


if __name__ == "__main__":
    main()
