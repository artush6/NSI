from threading import Thread, Lock
from time import sleep

c = 0
verrou = Lock()


def traitementA():
    global c
    i = 0
    while i < 1000000:
        verrou.acquire()
        c = 1
        if c != 1:
            print("*********** PROBLEME POUR A **************")
        verrou.release()
        i += 1


def traitementB():
    global c
    i = 0
    while i < 1000000:
        verrou.acquire()
        c = 2
        if c != 2:
            print("*********** PROBLEME POUR B **************")
        verrou.release()
        i += 1


t1 = Thread(target=traitementA)
t2 = Thread(target=traitementB)

t1.start()
t2.start()

for i in range(10):
    print("Thread principal")
    sleep(0.01)

print("Thread principal terminé")
