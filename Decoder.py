import base64
import getpass
user = getpass.getpass("Masukan Password ")
passwd = base64.b64decode("c2VtdWFpbmlkYXJpYWxsYWg=")
if(user == passwd):	
	f = open("Solver.cpp", "r")
	plain = base64.b64decode(f.read())
	f = open("loveyou.cpp", "w")
	f.write(plain)
	f.close()
	print("Berhasil")
else:
	print("Password Salah")
