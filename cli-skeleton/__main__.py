import click
from pathlib import Path
from collections import deque


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


@click.command()
@click.option('-n', '--lines', type=click.INT, default=10)
@click.argument(
    'file',
    type=click.File(mode='r')
)
def tail(file, lines):
    for line in deque(file, maxlen=lines):
        click.echo(line, nl=False)


if __name__ == '__main__':
    # ls()
    tail()
