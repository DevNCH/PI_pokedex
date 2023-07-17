import random
from treinador import Pokedex
from pokedex import Pokemon

class batalha(Pokedex):
        
    def captura_pokemon(self):
        self.id_treinador = self.teste_int("Digite seu ID: ")
    
        while True:

            morreu = 0
            numero = random.randint(1, 100)

            if numero <= 10: 
                sql = "SELECT * FROM pokemon_lendarios;"
                self.cursor.execute(sql)
                lista = self.cursor.fetchall()
                pokemon = random.choice(lista)
                print(f"Um {pokemon[1]}, se ferrou")
                return False
            
            else: 
                sql = "SELECT * FROM pokemon;"
                self.cursor.execute(sql)
                lista = self.cursor.fetchall()
                pokemon_selvagen = Pokemon(random.choice(lista))
                self.vidaInimigo = pokemon_selvagen.vida
                print(f"Um {pokemon_selvagen.nome}\nAtaque: {pokemon_selvagen.ataque}\nDefesa: {pokemon_selvagen.defesa}\nVida: {pokemon_selvagen.vida}\n       deseja batalhar?")
                numero = random.randint(1, 100)
                escolha = input('\nDigite "s" para sim ou "n" para não: ').lower()
                enfraquecido_inimigo = self.vidaInimigo*(20/100)
                self.atacar_selvagen = pokemon_selvagen.ataque
                y = 0
                while y == 0:
                    if morreu == 1:
                        break
                    if escolha == 's':
                        sql = f"SELECT * FROM pokemon_coletados where id_treinador = {self.id_treinador}"
                        self.cursor.execute(sql)
                        lista = self.cursor.fetchall()
                            
                        for pokemon in lista:
                            print(f"ID: {pokemon[1]} Pokemon: {pokemon[2]}")
                        self.id_pokemon = self.teste_int('Insira o ID do pokémon: ')
                        sql = "SELECT * FROM pokemon_coletados WHERE id_pokemon = %s AND id_treinador = %s"
                        self.cursor.execute(sql, (self.id_pokemon, self.id_treinador))
                        resultado = self.cursor.fetchone()        
                                    
                        if resultado:
                            sql = f"SELECT * FROM pokemon WHERE numero_na_pokedex = {self.id_pokemon}"
                            self.cursor.execute(sql)
                            pokemon = self.cursor.fetchone()
                            self.vida = pokemon[4]
                            enfraquecido_aliado = self.vida*(20/100)
                            print(f"Pokemon: {pokemon[1]}\nAtaque: {pokemon[2]}\nDefesa: {pokemon[3]}\nVida: {pokemon[4]}\n\n")
                            self.ataque = pokemon[2]
                            x = 0
                            while x == 0:
                                opcao = input('"a" para atacar ou "d" defender: ').lower()
                                if opcao == 'a':
                                    z = self.atacar(pokemon, pokemon_selvagen, enfraquecido_inimigo)
                                    if z == True:
                                        return True
                                    x = 1
                                elif opcao == "d":
                                    ataque = random.randint(self.atacar_selvagen-5,self.atacar_selvagen+5)
                                    
                                    if ataque > 0:
                                        self.vida -= ataque
                                        print(f"Você tomou {ataque} de dano")
                                        if self.vida <= 0:
                                            print("A vida do seu pokémon chegou a zero")
                                            morreu = 1
                                            break
                                            
                                        elif self.vida <= enfraquecido_aliado:
                                            a = 0
                                            while a == 0:
                                                print("O seu pokémon está enfraquecido, deseja trocar?")
                                                escolha = input('"s" para sim e "n" para não: ').lower()
                                            
                                                if escolha == "n":
                                                    print("Você fugiu")
                                                    return False
                                                elif escolha == "s":
                                                    for pokemon in lista:
                                                        if pokemon[1] == self.id_pokemon:
                                                            lista.pop(pokemon[1])
                                                    print(lista)
                                                    y = 0
                                                else :
                                                    print("Escolha inválida")
                                                    a = 0
                                else:
                                    print("Escolha inválida")
                                    x = 0
                                break
                            if morreu == 1:
                                break
                            lista_pokemon = ['atacar','defender']
                            escolha_pokemon = random.choice(lista_pokemon)
                            if escolha_pokemon == 'atacar':
                                print(f'o {pokemon_selvagen.nome} ataca!!!')
                                ataque = random.randint(self.atacar_selvagen-5,self.atacar_selvagen+5)            
                                self.vidaInimigo -= ataque
                                
                                if ataque > 0:
                                    print(f"Você tomou {ataque} de dano")
                                    self.vida -= ataque

                                    if self.vida <= 0:
                                        print("A vida do seu pokémon chegou a zero")
                                        morreu = 1
                                        break
                                        
                                    elif self.vida <= enfraquecido_aliado:
                                        print("O seu pokémon está enfraquecido, deseja trocar?")
                                        escolha = input('"s" para sim e "n" para não: ').lower()
                                    
                                        if escolha == "n":
                                            print("Você fugiu")
                                            return False
                                        elif escolha == "s":
                                            y = 0
                                            for pokemon in lista:
                                                if pokemon[1] == self.id_pokemon:
                                                    lista.pop(pokemon[1])
                                            print(lista)
                                        
                                        else :
                                            print("Escolha inválida")
                        
                            elif escolha_pokemon == 'defender':
                                print(f'o {pokemon_selvagen.nome} fica se defendendo')
                                ataque = random.randint(self.ataque-5,self.ataque+5)
                                self.vidaInimigo -= ataque
                                
                                if ataque > 0:
                                    print(f"Você deu {ataque} de dano") 

                                    if self.vidaInimigo <= enfraquecido_inimigo:
                                        print("O pokémon esta enfraquecido, deseja capturar?")
                                        captura = input('Digite "s" para capturar: ').lower()
                                        
                                        if captura == "s":
                                            numero = random.randint(1, 100)
                                            
                                            if numero >= 20:
                                                self.importa_pokemon(self.id_treinador, pokemon_selvagen.numero_na_pokedex, pokemon_selvagen.nome)
                                                print("parabéns você capturou o pokémon!!!")
                                                return True
                                            
                                            else:
                                                print("Você fracassou em captura o pokémon")
                                                return False
                                
                                elif ataque <= 0:
                                    print("Você não deu nenhum dano")                    
            
                    elif escolha == 'n':
                        print('você fugiu')
                        y = 1
            
            procurar = input('deseja procurar um pokémon para capturar (s/n)? ')
            if procurar == 'n':
                break
    
    def atacar(self, pokemon, pokemon_selvagen, enfraquecido_inimigo):
        ataque = random.randint(self.ataque-5,self.ataque+5)            
        string = pokemon[6]
        lista = string.split("', '")
        lista_nova = []
        for i in lista:
            novo_i = i.replace('[', '').replace(']', '').replace("'", '')
            lista_nova.append(novo_i)
        habilidade = random.choice(lista_nova)
        habilidade = habilidade.upper()
        print(f'{pokemon[1]}, {habilidade}!!!')
        
        if ataque > 0:
            print(f"Você deu {ataque} de dano")
            self.vidaInimigo -= ataque
    
            if self.vidaInimigo <= enfraquecido_inimigo:
                print("O pokémon esta enfraquecido, deseja capturar?")
                captura = input('Digite "s" para capturar: ').lower()
                
                if captura == "s":
                    numero = random.randint(1, 100)
                    
                    if numero >= 20:
                        self.importa_pokemon(self.id_treinador, pokemon_selvagen.numero_na_pokedex, pokemon_selvagen.nome)
                        print("parabéns você capturou o pokémon!!!")
                        return True
                    
                    else:
                        print("Você fracassou em captura o pokémon")
                        return False

        elif ataque <= 0:
            print("Você não deu nenhum dano")