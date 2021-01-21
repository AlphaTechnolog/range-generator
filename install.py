import os
import subprocess

def execute(cmd):
    subprocess.run([cmd],
                   shell=True,
                   stdout=subprocess.PIPE)

def path(url):
    return url.replace('~', os.getenv('HOME'))

# -- Checking --

if os.path.isdir('/opt/range'):
    print('Range is already installed now!')
    exit(1)

if os.path.isfile(path('~/.local/bin/range')):
    print('Range is already installed now!')
    exit(1)

# -- Installing --

print("=> git clone https://github.com/AlphaTechnolog/range-generator.git")
execute('git clone https://github.com/AlphaTechnolog/range-generator.git ./alpha-range')

print("=> sudo mv ./range /opt/range")
execute("sudo mv ./alpha-range /opt/range")
print('=> sudo chmod -R 777 /opt/range')
execute("sudo chmod -R 777 /opt/range")
print('=> sudo chmod -R 777 /opt/range/*')
execute('sudo chmod -R 777 /opt/range/*')

print(f'=> ln -s /opt/range/range-generator {path("~/.local/bin/range")}')
execute(f'ln -s /opt/range/range-generator {path("~/.local/bin/range")}')

print('range generator is installed now!')
print('type range --help')
