from personagem import Personagem
from tempo import Tempo
import random

class PersonagemPrincipal(Personagem):

    # metodo trabalho
    
    tempo = Tempo()

    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.stamina = 10
        self.inventario = {"Alimento":0, "Equipamento":0}


    def buscarAlimento(self):

        continuar = True
        while continuar:    

            self.info()

            print("Digite 1 para ir caçar")
            print("Digite 2 para pedir comida da rua")
            print("Digite 3 para roubar do vizinho")

            resposta = int(input())
            
            # gasto de stamina de acordo com a escolha da ação
            if resposta == 1:
                self.stamina -= 3
                self.tempo.passarHora(9)
            elif resposta == 2:
                self.stamina -= 1
                self.tempo.passarHora(9)
            elif resposta == 3:
                self.stamina -= 2     
                self.tempo.passarHora(9)
            else:
                print("Vc não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer para se recuperar? S/N")
                    resp = input()
                    if resp == 's' : 
                        self.comer()      


            sorteio = random.randint(1,3)

            # quantidade de alimento de acordo com o sorteio
            if sorteio == 1:
                a = 7
            elif sorteio == 2:
                a = 2
            elif sorteio == 3:
                a = 4        

            if resposta == sorteio:
                self.inventario ["Alimento"] += a

            print(self.inventario)    
            print(self.stamina)

            print("Deseja continuar? S/N") 
            resp = input()
            if resp == 's':
                continuar = True
            else:
                print("Deseja dormir para recuperar stamina?")
                resp = input()
                if resp == 's':
                    print("quantas horas deseja dormir?")
                    descanso = int(input())
                    self.dormir(descanso)
                    continuar == False    

            print()
            print()


    def buscarEquipamentos(self):

        continuar = True
        while continuar:    
            
            self.info()

            print("Digite 1 para buscar no ferro velho")
            print("Digite 2 para fabricar peças")
            print("Digite 3 para roubar peças")

            resposta = int(input())
            
            # gasto de stamina de acordo com a escolha da ação
            if resposta == 1 and self.stamina >= 2:
                self.stamina -= 2
                self.tempo.passarHora(9)
                self.eventoCofre()
            elif resposta == 2 and self.stamina >= 5:
                self.stamina -= 5
                self.tempo.passarHora(9)
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 3  
                self.tempo.passarHora(9)
            else:
                print("Vc não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer para se recuperar? S/N")
                    resp = input()
                    if resp == 's' : 
                        self.comer()  
                    

            sorteio = random.randint(1,3)

            # quantidade de equipamento de acordo com o sorteio
            if sorteio == 1:
                e = 2
            elif sorteio == 2:
                e = 7
            elif sorteio == 3:
                e = 4        

            if resposta == sorteio:
                self.inventario ["Equipamento"] += e 

            print(self.inventario)    
            print(self.stamina)

            print("Deseja continuar? S/N") 
            resp = input()
            if resp == 's':
                continuar = True
            else:
                print("Deseja dormir para recuperar stamina?")
                resp = input()
                if resp == 's':
                    print("quantas horas deseja dormir?")
                    descanso = int(input())
                    self.dormir(descanso)
                    continuar == False 
        
            print()
            print()            
                     



    def comer (self, comida):

        self.inventario ["Alimento"] -= comida       
        self.stamina += comida

        
    def dormir(self, horasDormidas):

        self.tempo.passarHora(horasDormidas)

        self.stamina += horasDormidas

        if self.stamina > 10:
            self.stamina = 10

    def info(self):

        print("intentario:", self.inventario)
        print("dia:", self.tempo.dia)
        print("hora:", self.tempo.hora)
        print("stamina:",self.stamina)
        print()

    def eventoCofre(self):

        lista = list(range(20))
        sorteio = random.randint(0, 99)

        if sorteio in lista:
            self.abrirCofre()


    def abrirCofre(self):

        print ("Vc achou um cofre..... ")

        for i in range(5):

            senha = 1234
            chute = input("Digite a senha: ")

            if senha == chute:
                self.inventario ["Equipamento"] += 50
                return
        
        print("Vc não conseguiu abrir o cofre... tururu! ")
    
        

        