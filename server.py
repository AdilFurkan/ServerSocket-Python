import socket

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host,port))
s.listen(1)
print(host)
print("Bağlantı bekleniyor ... ")
conn, addr = s.accept()
print(addr, "Servere bağlanıldı..")

filename = input(str("Lütfen gönderilecek dosyanın adını uzantısıyla birlikte giriniz : "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Dosya başarıyla gönderildi.")
