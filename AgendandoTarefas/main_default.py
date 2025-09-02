import schedule
import time
def tarefa():
    print('Testando agendador')
    
# Agendando
schedule.every().second.do(tarefa)
    
# Loop infinito
while True:
    schedule.run_pending()
    time.sleep(1)