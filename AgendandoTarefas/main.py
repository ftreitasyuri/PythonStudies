import schedule
import time

def tarefa():
    print('Testando agendador')
    
# Agendando
# schedule.every().second.do(tarefa)


# Agendando 5 second
# schedule.every(5).seconds.do(tarefa)

# Agendando por horário especifico
# schedule.every().day.at('13:39').do(tarefa)

# Agendando por horário e dia especifico
# schedule.every().tuesday.at('13:40').do(tarefa)

# Agendando por minuto em toda hora
# schedule.every().hour.at(':56').do(tarefa)


# Agendando a cada hora até um horário especifico
schedule.every().second.until('13:58').do(tarefa)


    
# Loop infinito
while True:
    schedule.run_pending()
    time.sleep(1)