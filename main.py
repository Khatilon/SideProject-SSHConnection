import paramiko
from getpass import getpass

if __name__ == "__main__":
    hostname = "abc123.sh.qwe.com"  # Please put real server host name
    username = input("Please enter the username: ")
    password = getpass("Please enter the password: ")

    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    
    session.connect(
        hostname=hostname,
        username=username,
        password=password
    )

    print("-----------------------------------")
    print(f"Hello {username}, welcome to server: {hostname}")
    print("-----------------------------------")

    cmd = "first"

    while(cmd):
        if (cmd == "frist"):
            cmd = input("Please input the cmd: ")
            continue

        stdin, stdout, stderr = session.exec_command(cmd)
        print(stdout.read().decode())

        cmd = input("Please input the cmd: ")
        
        if (cmd == "close"):
            print("-----------------------------------")
            print("Thank you for using! Good bye!")
            print("-----------------------------------")
            break

    session.close()