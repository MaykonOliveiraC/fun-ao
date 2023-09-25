import schedule
import time

frases = ['Meu respeito não é demandado, é merecido.','Eu não tenho sorte, eu faço minha própria sorte.', 'A única vez em que o sucesso vem antes do trabalho é no dicionário.', 'Essa é a diferença entre eu e você. Você quer perder pouco, eu quero vencer muito.', 'Se você tem uma arma apontando para sua cabeça, você saca uma arma maior.', 'Se suas costas estiverem contra a parede, derrube a maldita coisa.']


@schedule.repeat(schedule.every().second)
def tarefa():
    for frase in frases:
        time.sleep(1)
        print(frase)
    
#schedule.every(5).weeks.do(tarefa)
#schedule.every().hour.at(":20").do(tarefa)
#schedule.every().day.at("14:00").do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
   

