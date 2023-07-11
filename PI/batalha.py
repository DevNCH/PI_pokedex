from pokedex import Conexao
import random
from treinador import Pokedex

class batalha(Pokedex):
    
    def captura_pokemon(self):
        numero = random.randint(1, 100)
        
        while True:
            
#            try:
            
                if numero <= 10: 
                    sql = "SELECT * FROM pokemon_lendarios;"
                    self.cursor.execute(sql)
                    lista = self.cursor.fetchall()
                    pokemon = random.choice(lista)
                    print(f"Um {pokemon[1]}, se ferrou\nID: {pokemon[0]}")
                    return False
            
                else: 
                    sql = "SELECT * FROM pokemon;"
                    self.cursor.execute(sql)
                    lista = self.cursor.fetchall()
                    pokemon = random.choice(lista)
                    print(f"Um {pokemon[1]}, deseja capturar?\nID: {pokemon[0]}")
                    numero = random.randint(1, 100)
                    escolha = input('\n\nDigite "s" pra sim ou "n" pra não: ')
                    
                    if escolha == 'n':
                        print("O pokémon fugiu")
                        return False

                    if numero <= 20:
                        print("O pokémon fugiu, mas sorte da proxima vez")
                        
                    else:
                        treinador = int(input("Qual é seu ID: "))
                        self.importa_pokemon(treinador, pokemon[0], pokemon[1])
                        print("parabéns voçê capturou o pokémon")
                        return True
            
#            except:
#                print('Erro')