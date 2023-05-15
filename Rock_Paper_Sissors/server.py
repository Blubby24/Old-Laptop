import socket
from _thread import *
from Player import Player
import pickle
import numpy as np

server = "10.190.141.128"
port = 5900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = []

def makeColor():
    color = list(np.random.choice(range(256), size=3))
    return color

currentPlayer = 0

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    num = players[player].number
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players
            conn.sendall(pickle.dumps(reply))
        except:
            if num <= len(players)-1:
                #print()
                break
            while num > len(players)-1:
                #print('Reducing player. Num is ' + str(num))
                num -= 1
                player = num
            reply = players
            conn.sendall(pickle.dumps(reply))
            continue
    n = players[player]
    players.remove(n)
    print("Lost connection")
    conn.close()
    return None

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    players.append(Player(0,0,50,50,makeColor(), currentPlayer, ''))
    currentPlayer = len(players) - 1 
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print(currentPlayer)