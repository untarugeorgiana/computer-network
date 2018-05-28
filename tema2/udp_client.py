# UDP client
import socket
import logging
import sys
import time
#from scapy.all import *

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = '0.0.0.0'
server_address = (adresa, port)

ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = server_address), timeout = 1)


try:
    for element in range (0,10000):
        mesaj = str(element)
      
        ACK= " "
        logging.info('Trimitem mesajul "%s" catre %s', mesaj, adresa)
        sent = sock.sendto(mesaj, server_address)
        logging.info('Asteptam un raspuns...')
        ACK, server = sock.recvfrom(4096)
        logging.info('Content primit: "%s"', ACK)
        future=time.time()+0.5  
        while True:
            if time.time() > future:
                    logging.info('Trimitem mesajul "%s" catre %s', mesaj, adresa)
                    sent = sock.sendto(mesaj, server_address)
                    future=time.time()+0.5
            if (ACK!=" "):
                    break 

#logging.info('%s', ans[1].hwsrc)
#logging.info('%s',ans[1].psrc)

         
    
finally:
    logging.info('closing socket')
    sock.close()




  

   
       
   
    
mysocket.close()
