#!/usr/bin/python3
import getpass, os, sys, paramiko

hostname = sys.argv[2]
if hostname.find('@') >= 0:
    username, hostname = hostname.split('@')
else:
    username = getpass.getuser()
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, allow_agent=False, look_for_keys=False, key_filename=sys.argv[1])
stdin,stdout,stderr = client.exec_command(' '.join(sys.argv[3:]))
status = stdout.channel.recv_exit_status() # waits for command to terminate
os.fdopen(sys.stdout.fileno(), 'wb').write(stdout.read())
os.fdopen(sys.stderr.fileno(), 'wb').write(stderr.read())
#calling client.close() here produces a weird exception on exit??
sys.exit(status)