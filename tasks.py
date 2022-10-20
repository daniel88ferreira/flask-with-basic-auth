import os
import subprocess

from click import group


@group()
def cli():
    pass


@cli.command()
def run_debug():
    """
    Run app in debug
    """
    os.environ["FLASK_DEBUG"] = "True"
    cmd = 'python -m app'
    subprocess.run(cmd, shell=True, check=True)


@cli.command()
def test():
    """
    Run unit tests.
    """
    cmd = 'python -m unittest discover -s tests -p "test_*.py"'
    subprocess.run(cmd, shell=True, check=True)


if __name__ == '__main__':
    cli()
