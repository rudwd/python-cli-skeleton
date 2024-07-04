import click
from pathlib import Path
from collections import deque


# Example: Basic example taking only one argument without an option.
@click.command('ls')
@click.argument('paths',
                nargs=-1,
                type=click.Path(
                    exists=True,
                    file_okay=False,
                    readable=True,
                    path_type=Path,

                ))
@click.version_option('0.0.2', prog_name='skeleton cli')
def ls(paths):
    for i, path in enumerate(paths):
        if len(paths) > 1:
            click.echo(f'PATH: {path}/')

        for entry in path.iterdir():
            click.echo(f'{entry.name:{len(entry.name) + 5}}', nl=False)

        if i < len(paths) - 1:
            click.echo('\n')
        else:
            click.echo()


# Example: To show a simple option namely '-n' for number of lines.
@click.command()
@click.option('-n', '--lines', type=click.INT, default=10)
@click.argument(
    'file',
    type=click.File(mode='r')
)
def tail(file, lines):
    for line in deque(file, maxlen=lines):
        click.echo(line, nl=False)


# Example: Boolean option
@click.command()
@click.argument('name', default='World')
@click.option('--upper/--no-upper', default=False)
def upper_lower(name, upper):
    message = f'Hello {name}!'
    if upper:
        message = message.upper()
    click.echo(message)


@click.command()
@click.argument('name', default='World')
@click.option('--upper', 'casing', flag_value='upper')  # option name = --upper & its value if set = 'upper'
@click.option('--lower', 'casing', flag_value='lower')  # option name = --lower & its value if set = 'lower'
def upper_lower_2(name, casing):
    message = f'Hello {name}!'
    if casing == 'upper':
        message = message.upper()
    elif casing == 'lower':
        message = message.lower()
    click.echo(message)


@click.command()
@click.option(
    '--weekday',
    type=click.Choice([
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ])
)
def weekday(weekday):  # 'weekday' must match the parameter name namely '--weekday'.
    click.echo(f'Weekday: {weekday}')


def cli():
    print('hello there')


if __name__ == '__main__':
    # ls()
    # tail()
    # upper_lower()
    # upper_lower_2()
    # weekday()
    cli()
