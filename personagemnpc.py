from personagem import Personagem

import random

class Npc(Personagem):
    def __init__(self, nome, sexo):
        super().__init__(nome, sexo)
        self.alimento = 50
        self.cofre = 50
    

    def abrirEstoque(self):
        v = 0

        if self.alimento == 50:
            sorteio = random.randint(0, 99)

            if sorteio < 40:

                print (f"Parece que Hebe tem um estoque de comida guardado! Quando você clica na fechadura eletrônica a seguinte mensagem aparece:\n 'Olá gracinha! para abrir o estoque responda a charada:\nMeu avô tem 5 filhos, cada filho tem 3 filhos. Quantos primos eu tenho?\nQue velha doida, né?\n")
                
                resp = int(input("De qualquer forma digite a resposta para abrir o cofre: "))
                if resp == (12):
                    print
                    print("Deu certo!")
                    self.alimento = 0
                    v = 50
                    return v
                else:
                    print("A senha está errada e o alarme disparou! É melhor você correr pra casa!")
            
       

    def abrirCofre(self):
        v = 0

        if self.cofre == 50:

            lista = list(range(99))
            sorteio = random.randint(0, 99)

            if sorteio in lista:

                print ("Que sorte! No meio das pilhas de ferramentas você encontrou um cofre! Provavelmente é do dono Xaropinho\nEmbaixo do cofre está um papel escrito:\n'rapaiz... senha: 2683'\n(claramente, ele não entende muito de segurança, não é mesmo?) Mas parece que os ratos roeram o quinto número do papel. Vale a pena chutar alguns números para abrir o cofre!")

                for i in range(5):

                    senha = 1
                    chute = int(input("Digite a senha: "))

                    if senha == chute:
                        self.cofre = 0
                        print("Parabens!!! Você acertou a senha!!!")
                        v = 50
                        return v
                    else:
                        print("Vc não conseguiu abrir o cofre... tururu! ")
            
 
