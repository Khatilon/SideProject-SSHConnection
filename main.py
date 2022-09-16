import sshConnect
if __name__ == "__main__":
    clientInstace = sshConnect.connect()
    clientInstace.connectServer()

    cmd = "frsit"

    while(cmd):
        clientInstace.query()

        if (cmd == "close"):
            break
    
    clientInstace.closeConnection()