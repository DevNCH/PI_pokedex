from pokedex import Conexao
import random
from treinador import Pokedex

class batalha(Pokedex):
    
    def captura_pokemon(self):
        numero = random.randint(1, 100)
        
        while True:
            try:
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
                    print(f"Um {pokemon[1]}, deseja captura ?\nID: {pokemon[0]}")
                    numero = random.randint(1, 100)
                    escolha = input('\n\nDidite s pra sim ou n pra não: ')
                    
                    if escolha == 'n':
                        print("O pokemon fugiu")
                        return False

                    if numero <= 20:
                        print("O pokemon fugiu, mas sorte da proxima vez")
                        
                    else:
                        treinador = int(input("Qual é seu ID: "))
                        self.importa_pokemon(treinador, pokemon[0], pokemon[1])
                        print("parabens voçê capturou o pokemon")
                        return True
            
            except:
                print('Voçê errou, tente novamente')