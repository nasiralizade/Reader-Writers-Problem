"""
Labb 4 Reader-Writers problem
"""

from threading import Lock, Semaphore, Thread
from datetime import datetime

readLock = Semaphore(3)
writeLock = Lock()
NrOfSemaphores = int(readLock._value)


def lock_readers():  # Låser alla semaforer
    for i in range(NrOfSemaphores):
        readLock.acquire()


def unlock_readers():  # Låser upp alla semaforer
    for i in range(NrOfSemaphores):
        readLock.release()


class ReadWriteThreads():
    date = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S\n")

    def read(self):
        while (True):
            if (not writeLock.locked()):
                readLock.acquire()
                print(f"Thread is reading... {ReadWriteThreads.date}")  # Här är kritiska sektionen för read
                readLock.release()

    def write(self):
        while (1):
            writeLock.acquire()  # Detta betyder för readers att inga nya readers får köra
            lock_readers()  # Tar reader låsen en efter en
            ReadWriteThreads.date = (datetime.now()).strftime(
                "%Y/%m/%d %H:%M:%S")  # Här är kritiska sektionen för write
            print("Thread is writing to Date")
            writeLock.release()
            unlock_readers()

    def write_reverse(self):
        while (True):
            writeLock.acquire()  # Detta betyder för readers att inga nya readers får köra
            lock_readers()  # Tar reader låsen en efter en
            ReadWriteThreads.date = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S")[
                                    ::-1]  # Här är kritiska sektionen för writeReverse
            print("Thread is writing to Date in reverse")
            writeLock.release()
            unlock_readers()

    def start_threads(self):
        t1 = Thread(target=self.read)
        t1.start()
        t2 = Thread(target=self.write)
        t2.start()
        t3 = Thread(target=self.write_reverse)
        t3.start()
        t4 = Thread(target=self.read)
        t4.start()
        t5 = Thread(target=self.read)
        t5.start()


RW = ReadWriteThreads()
RW.start_threads()
