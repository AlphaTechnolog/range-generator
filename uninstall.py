import os
import subprocess

def execute(cmd):
    subprocess.run([cmd],
                   shell=True,
                   stdout=subprocess.PIPE)

def path(url):
    return url.replace('~', os.getenv('HOME'))

# -- Checking --

if not os.path.isdir('/opt/range'):
    print('Range is not installed now!')
    exit(1)

if not os.path.isfile(path('~/.local/bin/range')):
    print('Range is not installed now!')
    exit(1)

# -- Uninstalling --

print('=> sudo rm -rf /opt/range')
execute('sudo rm -rf /opt/range')
print(f'=> rm {path("~/.local/bin/range")}')
execute(f'rm {path("~/.local/bin/range")}')

print('range generator is uninstalled now')
