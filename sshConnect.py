import paramiko
from getpass import getpass

class connect():
    def connectServer(self):
        try:
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

            return self.client
        except:
            print("User information error, please input again!")
            self.connectServer()

    def query(self):
        cmd = input("Please input your cmd: ")
        stdin, stdout, stderr = session.exec_command(cmd)
        result = stdout.read().decode()
        print(result)

    def closeConnection(self):
        print("-----------------------------------")
        print("Thank you for using! Good bye!")
        print("-----------------------------------")
        self.client.close