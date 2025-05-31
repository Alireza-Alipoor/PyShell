import sys
import shutil
import shlex
import subprocess

COMMANDS = {
    "exit": lambda args: handle_exit(args),
    "echo": lambda args: handle_echo(args),
    "type": lambda args: handle_type(args),
    "pwd": lambda args: handle_pwd(args),
    "cd": lambda args: handle_cd(args)}


def handle_input(input: str) -> None:
    command, *args = shlex.split(input)
    if command in COMMANDS:
        COMMANDS[command](args)
    elif shutil.which(command):
        subprocess.run([command, *args], capture_output=True,
                       text=True,
                       stderr=sys.stderr,
                       stdout=sys.stdout)
    else:
        sys.stdout.write(f'{command}: command not found\n')


def handle_exit():
    ...


def handle_echo():
    ...


def handle_type():
    ...


def handle_pwd():
    ...


def handle_cd():
    ...


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            input = sys.stdin.readline()
            handle_input(input)
        except ValueError:
            continue


if __name__ == "__main__":
    main()
