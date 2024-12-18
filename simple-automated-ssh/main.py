import getpass
from fabric import Connection, Config

password = getpass.getpass('Enter your root password: ')

config = Config(overrides={'sudo': {'password': password}})
conn = Connection('127.0.0.1', user='johndoe', config=config)

result = conn.run('ls -la', hide=True)


conn.run("ls -la")
conn.run("pwd")

with conn.cd('/folder/folder'):
    conn.run('touch text.txt')
    conn.run('pwd')

conn.sudo("apt-get install")