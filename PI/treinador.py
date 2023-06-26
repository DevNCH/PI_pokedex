import mysql.connector
import time

class Treinador:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        self.cursor = self.conexao.cursor()
    def registrar_treinador(self):
        sql = "INSERT INTO treinadores (nome, idade, cidade) VALUES (%s, %s, %s)"
        val = (self.nome, self.idade, self.cidade)
        print('treinador registrado')
        self.cursor.execute(sql, val)
        self.conexao.commit()
   
    def pokedex_treinador(self):
        sql = "CREATE TABLE pokemon_coletados (id_treinador INT PRIMARY KEY, nome_treinador VARCHAR(50), id_pokemon INT, nome_pokemon VARCHAR(50))"
        self.cursor.execute(sql)
        self.conexao.commit()       
class Pokedex:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        self.cursor = self.conexao.cursor()
        
    def escolher_primero_pokemon(self):
        pokedex = Pokedex()
        pokemon1 = pokedex.procurar_pokemon(1)
        pokemon2 = pokedex.procurar_pokemon(4)
        pokemon3 = pokedex.procurar_pokemon(7)
        
        print(f"Escolha um dos seguintes pokémons para ser o seu primeiro:")
        print(f"1 - {pokemon1[1]} (Tipo: {pokemon1[2]}, ataque: {pokemon1[3]})")
        print(f"2 - {pokemon2[1]} (Tipo: {pokemon2[2]}, ataque: {pokemon2[3]})")
        print(f"3 - {pokemon3[1]} (Tipo: {pokemon3[2]}, ataque: {pokemon3[3]})")
        
        escolha = None
        tempo_inicial = time.time()
        while True:
            escolha = input('digite o número do pokémon que você quer escolhe: ')
            
            if escolha in ['1', '2', '3']:
                escolha = int(escolha)
                break
            
            else:
                print(' entrada invalida. digite 1, 2 ou 3.')
                
                tempo_atual = time.time()
                if tempo_atual - tempo_inicial > 30:
                    print("Tempo esgotado. Um pikachu será escolhido pelo sistema.")
                    escolha = 25
                    break
        self.importa_pokemon(escolha)
        print(f"Parabéns! Você escolheu o {self.pokemons[0][1]} como seu primeiro pokémon.")
                     
    def lista_pokemon(self):
        sql = "SELECT * FROM pokemon_coletados"
        self.cursor.execute(sql)
        pokemons_capturados = self.cursor.fetchall()
        for pokemon in pokemons_capturados:
            print(pokemon)
    
    def solta_pokemon(self, id_pokemon):
        sql = "DELETE FROM pokemon_coletados WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon solto com sucesso.")
    
    def nomea_pokemon(self, id_pokemon, novo_nome):
        sql = f"UPDATE {self.nome} SET nome = %s WHERE id_pokemon = %s"
        valores = (novo_nome, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        
    def procurar_pokemon(self, id):
        sql =f"SELECT * FROM pokedex WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
        
        else:
            print(resultado)
            
    
    def fecha_conexao(self):
        self.cursor.close()
        self.conexao.close()


