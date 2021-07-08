from personagem import Personagem
from tempo import Tempo
import random
from personagemnpc import npc

class PersonagemPrincipal(Personagem):
    
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

            try:
                resposta = int(input())
            except:
                print("Opção invalida")
                self.buscarAlimento()

            # gasto de stamina de acordo com a escolha da ação
            if resposta == 1 and self.stamina >= 3:
                self.stamina -= 3
                self.tempo.passarHora(9)
            elif resposta == 2 and self.stamina >= 1:
                self.stamina -= 1
                self.tempo.passarHora(9)
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 2     
                self.tempo.passarHora(9)
            else:
                print("Opa! Parece que você não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? S/N")
                    resp = input()
                    if resp == 's' : 
                        print("Digite a quantidade de alimentos para comer: ")
                        c = int(input())
                        if c > self.inventario ["Alimento"]:
                            self.comer(c)      
                        else:
                            print("quantidade maior do que vc possui!")
                    elif resp == 'n':
                        print("Deseja dormir para recuperar stamina?")
                        resp = input()
                        if resp == 's':
                            print("quantas horas deseja dormir?")
                            descanso = int(input())
                            self.dormir(descanso)
                            print("falso")
                            continuar = False
                        else:
                            print("falso")
                            continuar = False                               
                else:      
                    print("Vc não tem mais energia para continuar, hora de ninar, qtas horas: ")        
                    descanso = int(input())
                    self.dormir(descanso)
                    print("falso")
                    continuar = False  


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
                    print("falso")
                    continuar = False 
                else:
                    print("falso")
                    continuar = False       

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
            elif resposta == 2 and self.stamina >= 5:
                self.stamina -= 5
                self.tempo.passarHora(9)
            elif resposta == 3 and self.stamina >= 3:
                self.stamina -= 3  
                self.tempo.passarHora(9)
            else:
                print("Opa! Parece que você não tem stamina para concluir essa tarefa")
                if self.inventario ["Alimento"] > 0:             
                    print(f"Vc tem {self.inventario ['Alimento']} alimento. Deseja comer? S/N")
                    resp = input()
                    if resp == 's' : 
                        print("Digite a quantidade de alimentos para comer: ")
                        c = int(input())
                        if c > self.inventario ["Alimento"]:
                            self.comer(c)      
                        else:
                            print("quantidade maior do que vc possui!")
                    elif resp == 'n':
                        print("Deseja dormir para recuperar stamina?")
                        resp = input()
                        if resp == 's':
                            print("quantas horas deseja dormir?")
                            descanso = int(input())
                            self.dormir(descanso)
                            continuar == False                           
                else:      
                    print("Vc não tem mais energia para continuar, hora de ninar, qtas horas: ")        
                    descanso = int(input())
                    self.dormir(descanso)
                    continuar == False  
                    

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

        if self.stamina >= 10:
            self.stamina = 10
    



















    def acordar(self):
        if self.stamina >= 10:
            print("Você está com {self.estamina} pontos de stamina. Não está cansado! Tente fazer algumas tarefas")
            print()

    def info(self):

        print("inventário:", self.inventario)
        print("dia:", self.tempo.dia)
        print("hora:", self.tempo.hora)
        print("stamina:",self.stamina)
        print()

    

#----------------------------------------------------------------------------------------------

    

        
    #----------------------------------------------------------------------------------------------------------
        

        