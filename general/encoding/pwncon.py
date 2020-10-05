from pwn import remote,listen

conn = remote('ftp.ubuntu.com',21)
conn.recvline() 
#'220 FTP server (vsftpd)'
conn.send('USER anonymous\r\n')
conn.recvuntil(' ', drop=True)
#'331'
conn.recvline()
#'Please specify the password.\r\n'
conn.close()

#for listening purpose
l = listen(9999)
r = remote('localhost', 9999) 
svr = l.wait_for_connection()
r.send('hello')
print(svr.recv())

