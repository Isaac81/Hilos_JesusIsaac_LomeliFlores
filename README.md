# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierias
## Departamento de ciencias computacionales
Computacion Tolerante a fallas - Seccion D06

Profesor: *Lopez Franco Michel Emanuel*

Alumno: *Lomeli Flores Jesus Isaac*

## Introducción a sistemas distribuidos con python.

### Introducción

<p align="justify">
  Los hilos resultan ser una manera de ejecutar procesos en paralelo a un proceso principal sin afectar al flujo de este último, razón por la cual resultan útiles para
  crear sistemas que toleren de mejor manera los fallos, pues al ser independientes del proceso principal, si uno de estos hilos falla el sistema seguirá funcionando.
</p>


</div>

### Desarrollo

<p align="justify">
Para el desarrollo de esta practica se utilizo el lenguaje de programación python en su versión 3.11 para implementar un código que utilizara hilos para ejecutar dos
acciones de forma independiente, siendo la primera el proceso principal encargada de crear procesos para ejecutar en un hilo, cuyo código es el siguiente.

</p>


```py
if __name__ == '__main__':
    threading.Thread(target=calcular, daemon=True).start()
    print("Comenzando procesamiento... \n")
    for item in range(1, 7):
        q.put(item)

    q.join()
    print("Procesamiento concluido")
```


<p align="justify">
El hilo, por su parte, Tiene como función simular la ejecución de los procesos los procesos que son almacenados en la cola por el proceso principal. Estos procesos
consisten en multiplicar el número que se encuentra en la cola por si mismo, mostrar el resultado de la operación y esperar un segundo para simular el tiempo de
procesamiento.
</p>


```py
def calcular():
    while True:
        item = q.get()
        print(f'Calculando {item} * {item}')
        print(f'Resultado del proceso {item}: {item * item} \n')
        q.task_done()
        sleep(1)
```


<p align="justify">
El programa proceso principal esperara a que el proceso secundario finalice gracias a la función join(), por lo que la linea de procesamiento concluido no será impresa
sino hasta que el hilo secundario termine su ejecución.
</p>

![Ejecucíon de hilos](/Imagenes/Proceso.gif)


### Conclusion

<p align="justify">
Se logró comprender la importancia y aplicaciones de los hilos cómo herramientas que ayudan a crear sistemas tolerantes a fallos, pues al ser estos subprocesos 
independientes del proceso principal, en caso de que algún hilo falle, no afectaran el funcionamiento del hilo principal.
</p>


### Bibliografia
* H. (2022, 27 junio). Escáner de puertos con python básico. HackCode. Recuperado el 18 de Febrero de 2023, de https://hackcode.club/escaner-de-puertos-con-python-basico/ *
