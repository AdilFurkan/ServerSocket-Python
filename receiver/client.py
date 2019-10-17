import socket
s = socket.socket()
host = input(str("Lütfen göndericinin host adresini(adını) giriniz : "))
port = 8000
s.connect((host,port))
print("Bağlandı ... ")

filename = input(str("Alınan dosyanın yeni adını dosya uzantısı ile birlikte giriniz : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Dosya başarıyla alındı.")
