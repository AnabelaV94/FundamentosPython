import time
from datetime import datetime, timedelta

# Função para criar a animação
def anima_mensagem(mensagem, delay=0.1):
    for char in mensagem:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

# Função principal
def prenda_simbolica():
    # Definir a data de início
    data_inicio = datetime(2014, 2, 22)  # 22 de fevereiro de 2014
    hoje = datetime.now()

    # Ajustar para que o cálculo não conte o dia de hoje
    if hoje.month == 2 and hoje.day == 22:
        hoje = hoje - timedelta(days=1)  # Subtrair um dia para que o cálculo fique correto

    # Calcular a diferença de tempo
    diferenca = hoje - data_inicio
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    horas = diferenca.seconds // 3600

    # Criar a mensagem base
    mensagem_base = f"""
    🎉🎉 Parabéns para nós! 🎉🎉
    \nFaz {anos} anos que dois jovens de Gaia começaram a sua história de amor !
    \nCada segundo ao teu lado é uma aventura (exagerando para efeitos românticos),
    \numa jornada cheia de amor, risadas e muito mais. E já com 1 filho Kaidoso..... 
    \n💖 Não é só o tempo que importa, mas o que fazemos com ele! 💖
    \nVamos continuar a escrever a nossa história juntos.
    \n
    """
    
    # Adicionar um toque de humor no final
    mensagem_adicional = "\nP.S.: Hj vamos ao sushi? 😜"
    
    # Animação da mensagem base
    anima_mensagem(mensagem_base)
    time.sleep(1)
    
    # Animação da mensagem adicional
    anima_mensagem(mensagem_adicional)

# Chama a função para exibir a prenda
prenda_simbolica()