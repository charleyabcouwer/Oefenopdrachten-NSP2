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
@click.option("--tea/--no-tea", default=True)
def hello(name, count, tea):
    for _ in range(count):
        print(f"Hello {name}!")
        if tea:
            print("Wil je thee?")
        time.sleep(2)  # Wait 2 seconds


if __name__ == "__main__":
    hello()

# make boolean flag tea/no-tea


# function, parameter name, count, pause and tea
# repeat count times
# print hello <name>!
# if wished offer tea
# pause

# when run this script:
# run function
