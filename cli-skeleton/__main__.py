import click


@click.command('hello')
@click.version_option('0.0.1', prog_name='skeleton cli')
def cli():
    click.echo('Hello there')


if __name__ == '__main__':
    cli()
