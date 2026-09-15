import socket
import os
import time
from datetime import datetime
import threading
import pytest

print( datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

PORT = 50979

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("0.0.0.0", PORT))   # accessible depuis le reseau
serveur.listen(5)
print(f"Serveur de charge en ecoute sur le port {PORT}")

compteur =0

verrou = threading.Lock()

def travail(connexion, adresse):
	global compteur
	time.sleep(0.001)
	#with verrou:
	lu = compteur
	time.sleep(0.001)
	compteur = lu + 1
	print(f"{compteur}") 
	time.sleep(5)
	message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	connexion.sendall( message.encode())
	connexion.close()

while True:
	connexion, adresse = serveur.accept()

	t = threading.Thread(target=travail, args=(connexion, adresse))
	t.start() 
	    
	

	
	
