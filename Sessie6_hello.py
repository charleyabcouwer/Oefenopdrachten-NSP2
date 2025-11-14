import time

import click


@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
def hello(name, count):
    for _ in range(count):
        print(f"Hello {name}!")
        time.sleep(2)  # Wait 2 seconds


if __name__ == "__main__":
    hello()
