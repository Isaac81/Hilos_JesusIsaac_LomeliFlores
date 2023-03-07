import threading
import queue
from time import sleep

q = queue.Queue()

def calcular():
    while True:
        item = q.get()
        print(f'Calculando {item} * {item}')
        print(f'Resultado del proceso {item}: {item * item} \n')
        q.task_done()
        sleep(1)


if __name__ == '__main__':
    threading.Thread(target=calcular, daemon=True).start()
    print("Comenzando procesamiento... \n")
    for item in range(1, 7):
        q.put(item)

    q.join()
    print("Procesamiento concluido")