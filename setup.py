from setuptools import setup, find_packages


# NOTE: Bare minimum set up file to register an entry point.
#   Once installed, 'fs3' command should be available in CLI.
#   e.g.) C:\fs3 --help
def main():
    setup(name='friendly-s3-uploader',
          version='0.0.1',
          package_dir={'': '.'},
          packages=find_packages('.'),
          entry_points={
              'console_scripts': [
                  'fs3=cli.__main__:cli'  # NOTE: replacing 'cli' with 'cli-xxx' won't work.
              ]
          })


if __name__ == '__main__':
    main()
