from personagem import Personagem
from personagemnpc import Npc
from tempo import Tempo
import random


# from personagemnpc import npc
#Classe que configura a dinâmica do personagem principal e suas possibilidade.
class PersonagemPrincipal(Personagem):

    npc1 = Npc("Hebe", "F")
    npc2= Npc("Xaropinho", "F")
    tempo = Tempo()
    cont1 = 0
    cont2 = 0

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.stamina = 10
        self.inventario = {"Alimento":0, "Equipamento":0}    

        #Função de alimentação

    def getAlimento(self):
        return self.inventario  ["Alimento"]  

        #Função de busca por ferramentas e equipamentos.

    def getEquipamento(self):
        return self.inventario ["Equipamento"]    
    
    #Função de buscar alimentos para adicionar ao estoque do inventário
    def buscarAlimento(self):

        continuar = True
        while continuar == True and self.tempo.getDia() < 3:    
            
            while True:
                print("Digite 1 para ir caçar")
                print("Digite 2 para pedir comida da rua")
                print("Digite 3 para roubar do vizinho")
                print()

                try:
                    resposta = int(input())
                    if 0 < resposta < 4:
                        break
                    else:
                        print('\nOpção inválida!\n')
                except:
                    print("\nDigite apenas números!\n")
                    self.buscarAlimento()

            # gasto de stamina varia de acordo com a escolha da ação, ações mais garantidas gastam mais stamina.
            if resposta == 1 and self.stamina >= 3:
                self.stamina -= 3
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 2 and self.stamina >= 1:
                self.stamina -= 1
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 2     
                self.tempo.passarHora(9)
                self.estoqueNPC()
                if self.tempo.getDia() >= 3:
                    return 
            else:

                resposta = 0
                
                print("Opa! Parece que você não tem stamina para concluir essa tarefa\n")
                if self.inventario ["Alimento"] > 0:             
                    while True:
                        print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? [S/N]")
                        resp = input()[0].lower().strip()
                        if resp in ['s', 'n']:
                            break
                        else:
                            print('\nOpção Inválida!\n')

                    if resp == 's': 
                        while True:
                            print("Digite a quantidade de alimentos para comer: ")
                            try:
                                c = int(input())
                                if c < 1 or c > self.inventario['Alimento']:
                                    print('\nDigite uma quantidade válida!\n')
                                else:
                                    self.comer(c)
                                    break
                            except:
                                print('\nDigite apenas números!\n')
                    
                     #Caso o usuário fique sem stamina deverá dormir para recuperar energia.
                    elif resp == 'n':
                        while True:
                            print("Deseja dormir para recuerar energia?") 
                            resp = input()[0].lower().strip()
                            if resp in ['s', 'n']:
                                break
                            else:
                                print('\nOpção Inválida!\n')
                        if resp == 's':
                            while True:
                                print("Quantas horas deseja dormir?")
                                try:
                                    d = int(input())
                                    break
                                except:
                                    print('Digite apenas números!')
                            self.dormir(d)
                            return
                        elif resp == 'n':
                            print("Vc desmaiou, pois não tem força") 
                            self.desmaiar()
                            return 
                        
                                                      
                else:      
                                                                     
                    while True:  
                        print("Deseja dormir para recuperar energia? [S/N]")
                        resp = input()[0].lower().strip()
                        if resp in ['s', 'n']:
                            break
                        else:
                            print('\nOpção Inválida!\n')
                    if resp == 's':
                        while True:
                            print("Quantas horas deseja dormir?")
                            try:
                                d = int(input())
                                break
                            except:
                                print('Digite apenas números!')
                        self.dormir(d)
                        return
                    elif resp == 'n':
                        print("Você desmaiou de sono!") 
                        self.desmaiar()
                        return

            # quantidade de alimento conseguida na ação, varia de acordo com o resultado do sorteio:

            sorteio = random.randint(1,3)

            if sorteio == 1:
                a = 7
            elif sorteio == 2:
                a = 2
            elif sorteio == 3:
                a = 4        

            if resposta == sorteio:
                self.inventario ["Alimento"] += a

            self.info() #Informações do usuário sobre sua stamina e inventário
            
            while True:
                print("Deseja continuar?") 
                resp = input()[0].lower().strip()
                if resp in ['s', 'n']:
                    break
                else:
                    print('\nOpção Inválida!\n')
            if resp == 's':
                continuar = True
            elif resp == 'n':
                continuar = False

            print("\033c")
            print()
            self.info() #Informações do usuário sobre sua stamina e inventário
            print()



    #Função para buscar equipamentos 
    def buscarEquipamentos(self):

        continuar = True
        while continuar == True and self.tempo.getDia() < 3:    
            
            self.info()
            # Menu buscar equipamentos
            while True:
                print("Digite 1 para buscar no ferro velho")
                print("Digite 2 para fabricar peças")
                print("Digite 3 para roubar peças")
                print()

                try:
                    resposta = int(input())
                    if 0 < resposta < 4:
                        break
                    else:
                        print('\nOpção inválida!\n')
                except:
                    print("\nDigite apenas números!\n")
                    self.buscarEquipamentos()
            
            # Gasto de stamina de acordo com a escolha da ação
            if resposta == 1 and self.stamina >= 2:
                self.stamina -= 2
                self.tempo.passarHora(9)
                self.cofreNPC()
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 2 and self.stamina >= 5:
                self.stamina -= 5
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 3  
                self.tempo.passarHora(9)
                if self.tempo.getDia() >= 3:
                    return 
            else:

                resposta = 0
                
                print("Opa! Parece que você não tem stamina para concluir essa tarefa\n")
                if self.inventario ["Alimento"] > 0:             
                    while True:
                        print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? S/N")
                        resp = input()[0].lower().strip()
                        if resp in ['s', 'n']:
                            break
                        else:
                            print('\nOpção Inválida!\n')
                    if resp == 's': 
                        while True:
                            print("Digite a quantidade de alimentos para comer: ")
                            try:
                                c = int(input())
                                if c < 1 or c > self.inventario['Alimento']:
                                    print('\nDigite uma quantidade válida!\n')
                                else:
                                    self.comer(c)
                                    break
                            except:
                                print('\nDigite apenas números!\n')

                        self.comer(c)      
                    
                    elif resp == 'n':
                        while True:
                            print("Deseja dormir para recuperar energia? [S/N]")
                            resp = input()[0].lower().strip()
                            if resp in ['s', 'n']:
                                break
                            else:
                                print('\nOpção Inválida!\n')
                        if resp == 's':
                            while True:
                                print("Quantas horas deseja dormir?")
                                try:
                                    d = int(input())
                                    break
                                except:
                                    print('Digite apenas números!')
                            self.dormir(d)
                            return
                        elif resp == 'n' and self.stamina == 0:
                            print("Você desmaiou de sono!") 
                            self.desmaiar()
                            return
                        
                                                        
                else:      
                    while True:
                        print("Deseja dormir para recuperar energia?")
                        resp = input()[0].lower().strip()
                        if resp in ['s', 'n']:
                            break
                        else:
                            print('\nOpção Inválida!\n')
                    if resp == 's':
                        while True:
                            print("Quantas horas deseja dormir?")
                            try:
                                d = int(input())
                                break
                            except:
                                print('Digite apenas números!')
                        self.dormir(d)
                        return
                    elif resp == 'n' and self.stamina == 0:
                        print("Vc desmaiou desmaiou de sono!") 
                        self.desmaiar()
                        return
                    
        # quantidade de equipamento varia de acordo com o sorteio.

            sorteio = random.randint(1,3)

            if sorteio == 1:
                e = 2
            elif sorteio == 2:
                e = 7
            elif sorteio == 3:
                e = 4        

            if resposta == sorteio:
                self.inventario ["Equipamento"] += e 

            self.info() #Informações do usuário sobre sua stamina e inventário

            while True:
                print("Deseja continuar?") 
                resp = input()[0].lower().strip()
                if resp in ['s', 'n']:
                    break
                else:
                    print('\nOpção Inválida!\n')
            if resp == 's':
                continuar = True
            elif resp == 'n':
                continuar = False 

            print("\033c")     
            self.info() #Informações do usuário sobre sua stamina e inventário
            print()
          
                     

    def relogio (self):     #Função de controle da passagem do tempo.
        return self.tempo.getDia()


    def comer (self, comida): #função de busca de alimento para o inventário. 
        self.inventario ["Alimento"] -= comida       
        self.stamina += comida

        
    def dormir(self, horasDormidas): #Função usada para recuperar a stamina. 
        self.tempo.passarHora(horasDormidas)
        self.stamina += horasDormidas
        if self.stamina >= 10:
            self.stamina = 10
    

    def desmaiar(self): #Função chamada quando o usuário fica compeltamente sem energia e não dorme.
        self.stamina = 8
        self.tempo.passarHora(8)
    

    def acordar(self): #Função chamada quando a stamina volta aos valores máximos
        if self.stamina >= 10:
            print("Você está com {self.estamina} pontos de stamina. Não está cansado! Tente fazer algumas tarefas")
            print()

    #Funções de inventário dos npc's.
    def estoqueNPC(self):
        if self.cont1 == 0:
            v = self.npc1.abrirEstoque()
            if v != None:
                self.inventario ["Alimento"] += v
                self.cont1 +=1
        
        

    def cofreNPC(self):
        if self.cont2 == 0:
            v = self.npc2.abrirCofre()
            if v != None:
                self.inventario ["Equipamento"] += v
                self.cont2 +=1        
      


    #Função de retorno do inventário. 
    def info(self):

        print("Aqui estão as suas informações essenciais, elas permitem que você planeje suas tarefas, fique atento a elas!")
        print()
        print(f"A quantidade de itens no seu inventário é: {self.inventario}. \nVocê precisa de no mínimo 25 itens de Alimento e 25 itens de Equipamentos para efetuar sua viagem com sucesso.")
        tempoRestante = 5 - self.tempo.getDia()
        print(f"Hoje é dia: {self.tempo.getDia()}, você tem apenas mais {tempoRestante} para finalizar suas tarefas!")
        print()
        print(f"Agora são: {self.tempo.getHora()} horas.")
        print(f"Sua stamina é: {self.stamina}")
        print()