import datetime
import time

while True:
    # Obter a hora atual
    now = datetime.datetime.now()
    
    # Formatando a hora no formato desejado
    current_time = now.strftime("%H:%M:%S")
    
    # Limpar o terminal
    print("\033c", end="")
    
    # Imprimir o horário atual
    print("Relógio:")
    print(current_time)
    
    # Aguardar um segundo antes de atualizar o relógio
    time.sleep(1)
