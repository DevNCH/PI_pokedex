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
    def __init__(self, nome, ataque, defesa, vida, geracao, habilidades):
        super().__init__()
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

class Professor(Conexao):
    
    def __init__(self):
        super().__init__()

    def treinador(self, nome, idade, cidade, senha):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.senha = senha
        
    def registrar_professor(self):
        nome = input("insira seu nome: ")
        idade = int(input("insira sua idade: "))
        cidade = input("insira sua cidade: ")
        senha = input("insira sua senha: ")
        sql = "INSERT INTO professores (nome, idade, cidade, senha) VALUES (%s, %s, %s, %s)"
        val = (nome, idade, cidade, senha)
        self.cursor.execute(sql, val)
        self.conexao.commit()
        print('profesor registrado')

    def login(self):
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
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
            print(f"número na pokedéx: {pokemon[0]}, nome: {pokemon[1]}, ataque: {pokemon[2]}, defesa: {pokemon[3]}, vida: {pokemon[4]}, geracao: {pokemon[5]}, habilidades: {pokemon[6]}")

    def informacoes_pokemon(self):
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
        id = int(input("digite o ID do pokemon: "))
        sql =f"SELECT * FROM pokemon_lendarios WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nvida: {resultado[4]}\ngeracao: {resultado[5]}\nhabilidades: {resultado[6]}")
            
    def lista_geracao_pokemon_lendarios(self):
        geracao = int(input('Insira a geração a ser exibida: '))
        sql = f'SELECT * FROM pokemon_lendarios where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        
        for pokemon in pokemons:
            print(f"número na pokedéx: {pokemon[0]}, nome: {pokemon[1]}, ataque: {pokemon[2]}, defesa: {pokemon[3]}, vida: {pokemon[4]}, geracao: {pokemon[5]}, habilidades: {pokemon[6]}")
            
    def deleta_pokemon(self):
        id_pokemon = int(input("Digite o ID do pokemon: "))
        sql = f"DELETE FROM pokemon WHERE numero_na_pokedex = {id_pokemon}"
        self.cursor.execute(sql)
        self.conexao.commit()
        print("Pokémon deletado com sucesso.")

    def deleta_pokemon_lendario(self):
        id_pokemon = int(input("Digite o ID do pokemon: "))
        sql = f"DELETE FROM pokemon_lendarios WHERE numero_na_pokedex = {id_pokemon}"
        self.cursor.execute(sql)
        self.conexao.commit()
        print("Pokémon lendario deletado com sucesso.")

    def atualiza_pokemon(self):
        id_pokemon = int(input("Digite o ID do pokemon que deseja atualizar: "))
        novo_nome = input("Nome: ")
        novo_ataque = int(input('Ataque: '))
        nova_defesa = int(input("Defesa: "))
        nova_vida = int(input('Vida: '))
        nova_geracao = int(input('Geração: '))
        quantidade = int(input('quantidade de habilidades vão ser inseridas: '))
        novas_habilidades = []
        for num in range(quantidade):
            habilidade = input('insira a habilidade: ')
            novas_habilidades.append(habilidade)
            num +=1
        novas_habilidades = str(novas_habilidades)
        sql = "UPDATE pokemon SET nome = %s, ataque = %s, defesa = %s, vida = %s, geracao = %s, habilidades = %s WHERE numero_na_pokedex = %s"
        valores = (novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit() 
        
    def atualiza_pokemon_lendarios(self):
        id_pokemon = int(input("Digite o ID do pokemon que deseja atualizar: "))
        novo_nome = input("Nome: ")
        novo_ataque = int(input('Ataque: '))
        nova_defesa = int(input("Defesa: "))
        nova_vida = int(input('Vida: '))
        nova_geracao = int(input('Geração: '))
        quantidade = int(input('quantidade de habilidades vão ser inseridas: '))
        novas_habilidades = []
        for num in range(quantidade):
            habilidade = input('insira a habilidade: ')
            novas_habilidades.append(habilidade)
            num +=1
        novas_habilidades = str(novas_habilidades)
        sql = "UPDATE pokemon_lendarios SET nome = %s, ataque = %s, defesa = %s, vida = %s, geracao = %s, habilidades = %s WHERE numero_na_pokedex = %s"
        valores = (novo_nome, novo_ataque, nova_defesa, nova_vida, nova_geracao, novas_habilidades, id_pokemon)
        self.cursor.execute(sql, valores)
        self.conexao.commit()   
        
    def registrar_pokemon(self):
        numero_na_pokedex = int(input("Número na pokedéx: "))
        nome = input("Nome: ")
        ataque = int(input('Ataque: '))
        defesa = int(input("Defesa: "))
        vida = int(input('Vida: '))
        geracao = int(input('Geração: '))
        quantidade = int(input('quantidade de habilidades vão ser inseridas: '))
        habilidades = []
        for num in range(quantidade):
            habilidade = input('insira a habilidade: ')
            habilidades.append(habilidade)
            num +=1
        habilidades = str(habilidades)
        sql = "INSERT INTO pokemon (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades) values (%s,%s,%s,%s,%s,%s,%s)"
        valores = (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    def registrar_pokemon_lendario(self):
        numero_na_pokedex = int(input("Número na pokedéx: "))
        nome = input("Nome: ")
        ataque = int(input('Ataque: '))
        defesa = int(input("Defesa: "))
        vida = int(input('Vida: '))
        geracao = int(input('Geração: '))
        quantidade = int(input('quantidade de habilidades vão ser inseridas: '))
        habilidades = []
        for num in range(quantidade):
            habilidade = input('insira a habilidade: ')
            habilidades.append(habilidade)
            num +=1
        habilidades = str(habilidades)
        sql = "INSERT INTO pokemon_lendarios (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades) values (%s,%s,%s,%s,%s,%s,%s)"
        valores = (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        


    