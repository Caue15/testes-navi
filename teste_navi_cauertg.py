# Ao rodar o programa, ele dará as instruções para rodar cada teste!
# (NÃO é preciso comentar ou descomentar nenhuma parte para rodar um teste individualmente)

def inicio():
    # boas vindas
    print('\n###########################################################')
    print('#                                                         #')
    print('#  Testes de Python para o Summer Intern da Navi Capital  #')
    print('#                                                         #')
    print('#                       Feito por:                        #')
    print('#                         Cauê Renatini Tironi Gordilho   #')
    print('#                                                         #')
    print('###########################################################')

inicio()

while True:
     
    teste = input('Digite o número do teste que gostaria de rodar e pressione enter: ')
    
    if teste == '1':
        # Teste 1
            
        # Dados de entrada
        n1 = 2 # para ser par
        n2 = 49 # múltiplo dado
        n3 = 37 # múltiplo dado
        mult = 0 # variável usada para contar o múltiplos
        n = 5000000 # limite dado
        i = 1 # variável para iteração
        
        while i <= n:
            if i % n1 == 0 and i % n2 == 0 and i % n3 == 0: # verifica as condições
                mult += 1 # adiciona no contador
            i += 1
        print('\nx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
        print('x                                                                   x')
        print(f'x Existem {mult} números que satisfazem essas condições no intervalo! x')
        print('x                                                                   x')
        print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
        
        seguir = input('Você quer sair ou rodar outro teste? Digite S para recomeçar ou outra tecla para terminar: ')
        if seguir.upper() == 'S':
            continue
        print('\nMuito obrigado!!')
        break


    if teste == '2':
        # Teste 2
        
        # Importa bibliotecas necessárias
        import numpy as np
        from math import factorial
        
        x = np.zeros(10) # cria vetor
        
        for i in range(len(x)):
            if (i+1) % 2 == 0: # verifica se é par
                x[i] = (3**(i+1))+7*(factorial(i+1)) # fórmula dada
            else:
                x[i] = (2**(i+1))+4*np.log(i+1) # fórmula dada
        
        maximo = np.argmax(x) + 1 # guarda a posição. soma 1 pois o vetor começa com índice 0, a contagem das posições começa na 1ª
        media = round(np.mean(x),2) # econtra a média do vetor e arredonda com 2 casas decimais
        print('\nx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
        print('x                                                 x')
        print(f'x  O maior elemento do vetor está na {maximo}ª posição! x\nx  E a média dos elementos do vetor é {media}. x')
        print('x                                                 x')
        print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
        
        seguir = input('Você quer sair ou rodar outro teste? Digite S para recomeçar ou outra tecla para terminar: ')
        if seguir.upper() == 'S':
            continue
        print('\nMuito obrigado!!')
        break
        
        
    if teste == '3':
        #Teste 3
        
        dados = {} # cria dicionário vazio que terá os dados dos alunos
        
        for i in range(5):
            nome = input('Nome do Aluno: ') # lê nome do aluno
            nota = input('Nota: ') # lê nota do aluno
            dados[nome] = float(nota) # salva no dicionário
            #maximo = dados(max[dados])
        
        maximo = max(dados.values()) # encontra o valor máximo
        chaves = [c for c,v in dados.items() if v == maximo] # verifica onde ele está e se há duas notas máximas iguais
        
        if len(chaves) == 1: # verifica se o valor máximo se repete
            print(f'\n\nO aluno com a maior nota é: {chaves[0]}\nSua nota foi {maximo}!')
        else:
            alunos = ', '.join(chaves) # caso haja mais de 1 aluno com nota máxima, cria string com os nomes separados por vírgula (apenas para estética)
            print(f'\n\nOs alunos com a maior nota são: {alunos}.\nA nota deles foi {maximo}!')
            
        seguir = input('\nVocê quer sair ou rodar outro teste? Digite S para recomeçar ou outra tecla para terminar: ')
        if seguir.upper() == 'S':
            continue
        print('\nMuito obrigado!!')
        break