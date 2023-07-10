import mysql.connector

class Conexao:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gk24ibp79",
            database="pokedex"
        )
        self.cursor = self.conexao.cursor()

    def fecha_conexao(self):
        self.cursor.close()
        self.conexao.close()

from abc import ABC, abstractmethod

class Pokemon(Conexao, ABC):
    
    @abstractmethod
    def __init__(self, numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades):
        super().__init__()
        self.numero_na_pokedex = numero_na_pokedex
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.geracao = geracao    
        self.habilidades = habilidades

    def pokemon(self):
        super().__init__()

    def pokemon_lendario(self):
        super().__init__()

class professor(Conexao):
    
    def __init__(self):
        super().__init__()
        
    def registrar_professor(self):
        sql = "INSERT INTO professores (nome, idade, cidade, senha) VALUES (%s, %s, %s, %s)"
        val = (self.nome, self.idade, self.cidade, self.senha)
        print('profesor registrado')
        self.cursor.execute(sql, val)
        self.conexao.commit()

    def login(self, nome, senha:str):
        sql = f"SELECT * FROM professores where nome = '{nome}';"
        self.cursor.execute(sql)
        professor = self.cursor.fetchone()
        print(professor)
        
        while True:
            
            if senha != professor[4] or  nome != professor[1]:
                print("sem registro")
                return False
            
            elif senha != professor[4] and nome == professor[1]:
                print("senha incorreta")
                return False
            
            if nome == professor[1] and  senha == professor[4]:
                print("login efetuado")
                return True

    def lista_geracao_pokemon(self):
        geracao = int(input('Insira a geração a ser exibida: '))
        sql = f'SELECT * FROM pokemon where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        
        for pokemon in pokemons:
            print(f"nome: {pokemon[1]}, ataque: {pokemon[2]}, defesa: {pokemon[3]}, vida: {pokemon[4]}, geração: {pokemon[5]}, habilidades: {pokemon[6]}")

    def informacoes_pokemon(self, id):
        id = int(input("digite o ID do pokemon: "))
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nvida: {resultado[4]}\ngeracao: {resultado[5]}\nhabilidades: {resultado[6]}")
            
    def informacoes_pokemon_lemdario(self):
        id = ("digite o ID do pokemon: ")
        sql =f"SELECT * FROM pokemon_lendarios WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nvida: {resultado[4]}\ngeracao: {resultado[5]}\nhabilidades: {resultado[6]}")
            
    def lista_geracao_pokemon_lendarios(self):
        geracao = input(int('Insira a geração a ser exibida: '))
        sql = f'SELECT * FROM pokemon_lendarios where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        
        for pokemon_lendarios in pokemons:
            
            print(f"nome: {pokemon_lendarios[1]}\nataque: {pokemon_lendarios[2]}\ndefesa: {pokemon_lendarios[3]}\nvida: {pokemon_lendarios[4]}\ngeracao: {pokemon_lendarios[5]}\nhabilidades: {pokemon_lendarios[6]}")
            
    def deleta_pokemon(self, id_pokemon):
        sql = "DELETE FROM pokemon WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon deletado com sucesso.")

    def deleta_pokemon_lendario(self, id_pokemon):
        sql = "DELETE FROM pokemon WHERE id_pokemon = %s"
        valor = (id_pokemon)
        self.cursor.execute(sql, valor)
        self.conexao.commit()
        print("Pokémon lendario deletado com sucesso.")

    def atualiza_pokemon(self, id_pokemon, novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades):
        sql = "UPDATE pokemon SET nome = %s, ataque = %s, defesa = %s, vida = %s, geracao = %s, habilidades = %s WHERE id_pokemon = %s"
        valores = (novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit() 
        
    def atualiza_pokemon_lendarios(self, id_pokemon, novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades):
        sql = "UPDATE pokemon_lendarios SET nome = %s, ataque = %s, defesa = %s, vida = %s, geracao = %s, habilidades = %s WHERE id_pokemon = %s"
        valores = (novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
    def registrar_pokemon(self, pokemon:Pokemon):
        sql = "INSERT INTO pokemon (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades) values (%s,%s,%s,%s,%s,%s,%s)"
        valores = (pokemon.numero_na_pokedex, pokemon.nome, pokemon.ataque, pokemon.defesa, pokemon.vida, pokemon.geracao, pokemon.habilidades)
        self.cursor.execute(sql, valores)
        self.conexao.commit()