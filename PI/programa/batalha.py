import random
from treinador import Pokedex
pokedex = Pokedex

class batalha(Pokedex):
        
            def captura_pokemon(self):
                numero = random.randint(1, 100)
                self.id_treinador = int(input("Digite seu ID: "))
            
                while True:
                            
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
                        pokemon_selvagen = random.choice(lista)
                        self.vidaInimigo = pokemon_selvagen[4]
                        print(f"Um {pokemon_selvagen[1]}\nAtaque: {pokemon_selvagen[2]}\nDefesa: {pokemon_selvagen[3]}\nVida: {pokemon_selvagen[4]}\n       deseja batalhar?")
                        numero = random.randint(1, 100)
                        escolha = input('\nDigite s pra sim ou n pra não: ')
                        enfraquecido = self.vidaInimigo*(20/100)
                        self.atacar_selvagen = pokemon_selvagen[2]
                        
                        if escolha == 's':
                            sql = f"SELECT * FROM pokemon_coletados where id_treinador = {self.id_treinador}"
                            self.cursor.execute(sql)
                            lista = self.cursor.fetchall()
                                
                            for pokemon in lista:
                                print(f"ID: {pokemon[1]} Pokemon: {pokemon[2]}")
                            self.id_pokemon = int(input('Insira o ID do pokémon: '))
                            sql = "SELECT * FROM pokemon_coletados WHERE id_pokemon = %s AND id_treinador = %s"
                            self.cursor.execute(sql, (self.id_pokemon, self.id_treinador))
                            resultado = self.cursor.fetchone()        
                                        
                            if resultado:
                                sql = f"SELECT * FROM pokemon WHERE numero_na_pokedex = {self.id_pokemon}"
                                self.cursor.execute(sql)
                                pokemon = self.cursor.fetchone()
                                self.vida = pokemon[4]
                                print(f"Pokemon: {pokemon[1]}\nAtaque: {pokemon[2]}\nDefesa: {pokemon[3]}\nVida: {pokemon[4]}\n\n")
                                opcao = input("Atacar ou Defender: ")
                                listapokemon = ['atacar','defender']
                                escolha_pokemon = random.choice(listapokemon)
                                self.atacar = pokemon[2]
                                
                                if opcao == 'atacar':
                                    ataque = random.randint(self.atacar-5,self.atacar+5)            
                                    self.vidaInimigo -= ataque
                                    
                                    if ataque > 0:
                                        print(f"Voçe deu {ataque} de dano")
                                
                                    if self.vidaInimigo <= enfraquecido:
                                        print("O pokemon esta enfraquecido, deseja captura?")
                                        captura = input("Digite sim para captura: ")
                                        
                                        if captura == "sim":
                                            numero = random.randint(1, 100)
                                            
                                            if numero >= 20:
                                                self.importa_pokemon(self.id_treinador, pokemon_selvagen[0], pokemon_selvagen[1])
                                                print("parabens voçê capturou o pokemon")
                                                return True
                                            
                                            else:
                                                print("Você fracassou em captura o pokemon")
                                                return False
                                
                                    elif ataque <= 0:
                                        print("Você n deu nenhum dano")
                                                        
                            if escolha_pokemon == 'atacar':
                                ataque = random.randint(self.atacar_selvagen-5,self.atacar_selvagen+5)            
                                self.vidaInimigo -= ataque
                                
                                if ataque > 0:
                                    print(f"Voçe tomou {ataque} de dano")
                                    
                                if self.vida <= enfraquecido:
                                    print("O seu pokemon esta enfraquecido, deseja trocar ?")
                                    escolha = input('s para sim e n para não: ')
                                
                                    if escolha == "n":
                                        return False
                                    
                                    else :
                                        print("Escolha invalida")
                                
                                elif self.vida <= 0:
                                    print("A vida do seu pokemon chegou a zero")
                                    return False
                                                        
                                elif ataque <= 0:
                                    print("Você n deu nenhum dano")
                                                
                            elif opcao == "defender":
                                ataque = random.randint(self.atacar_selvagen-5,self.atacar_selvagen+5)
                                self.vida -= ataque
                                
                                if ataque > 0:
                                    print(f"Voçe tomou {ataque} de dano")
                            
                            elif escolha_pokemon == 'defender':
                                ataque = random.randint(self.atacar-5,self.atacar+5)
                                self.vidaInimigo -= ataque
                                
                                if ataque > 0:
                                    print(f"Voçe deu {ataque} de dano")
                            
                            else :
                                print("Escolha invalida")                       
                    
                    if numero <= 20:
                        print("O pokemon fugiu, mas sorte da proxima vez")
                        return False
                        
                    elif escolha == 'n':
                        print("Você fugiu")
                    
                    else:
                        print("Escolha invalida")
                            
            