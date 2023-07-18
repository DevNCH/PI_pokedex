import mysql.connector
from abc import ABC

class Tenta_quebrar:
    def teste_int(self, valor) -> int:
        while True:
            try:
                num = int(input(f'{valor}'))
            except:
                print('não é um número inteiro')
                continue
            break
        return num

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

class Pokemon(Conexao, ABC, Tenta_quebrar):
    
    def __init__(self, pokemon):
        super().__init__()
        self.numero_na_pokedex = pokemon[0]
        self.nome = pokemon[1]
        self.ataque = pokemon[2]
        self.defesa = pokemon[3]
        self.vida = pokemon[4]
        self.geracao = pokemon[5]
        self.habilidades = pokemon[6]

class Professor(Conexao, Tenta_quebrar):
    
    def __init__(self):
        super().__init__()
        
    def registrar_professor(self):
        nome = input("insira seu nome: ")
        idade = self.teste_int("insira sua idade: ")
        cidade = input("insira sua cidade: ")
        senha = input("insira sua senha: ")
        sql = "INSERT INTO professores (nome, idade, cidade, senha) VALUES (%s, %s, %s, %s)"
        val = (nome, idade, cidade, senha)
        self.cursor.execute(sql, val)
        self.conexao.commit()
        print('profesor registrado')

    def login(self):

        while True:

            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            sql = f"SELECT * FROM professores where nome = '{nome}';"
            self.cursor.execute(sql)
            professor = self.cursor.fetchone()

            if professor == None:
                print("\nsem registro\n")
                continue
            
            elif senha != professor[4]:
                print("\nsenha incorreta\n")
                continue
            
            elif senha == professor[4]:
                print("\nlogin efetuado\n")
                break

    def lista_geracao_pokemon(self):
        geracao = self.teste_int('Insira a geração a ser exibida: ')
        sql = f'SELECT * FROM pokemon where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        
        for pokemon in pokemons:
            print(f"número na pokedéx: {pokemon[0]}, nome: {pokemon[1]}, ataque: {pokemon[2]}, defesa: {pokemon[3]}, vida: {pokemon[4]}, geracao: {pokemon[5]}, habilidades: {pokemon[6]}")

    def informacoes_pokemon(self):
        id = self.teste_int("digite o ID do pokemon: ")
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nvida: {resultado[4]}\ngeracao: {resultado[5]}\nhabilidades: {resultado[6]}")
            
    def informacoes_pokemon_lemdario(self):
        id = self.teste_int("digite o ID do pokemon: ")
        sql =f"SELECT * FROM pokemon_lendarios WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nvida: {resultado[4]}\ngeracao: {resultado[5]}\nhabilidades: {resultado[6]}")
            
    def lista_geracao_pokemon_lendarios(self):
        geracao = self.teste_int('Insira a geração a ser exibida: ')
        sql = f'SELECT * FROM pokemon_lendarios where geracao = {geracao}'
        self.cursor.execute(sql)
        pokemons = self.cursor.fetchall()
        
        for pokemon in pokemons:
            print(f"número na pokedéx: {pokemon[0]}, nome: {pokemon[1]}, ataque: {pokemon[2]}, defesa: {pokemon[3]}, vida: {pokemon[4]}, geracao: {pokemon[5]}, habilidades: {pokemon[6]}")
            
    def deleta_pokemon(self):
        id_pokemon = self.teste_int("Digite o ID do pokemon: ")
        sql = f"DELETE FROM pokemon WHERE numero_na_pokedex = {id_pokemon}"
        self.cursor.execute(sql)
        self.conexao.commit()
        print("Pokémon deletado com sucesso.")

    def deleta_pokemon_lendario(self):
        id_pokemon = self.teste_int("Digite o ID do pokemon: ")
        sql = f"DELETE FROM pokemon_lendarios WHERE numero_na_pokedex = {id_pokemon}"
        self.cursor.execute(sql)
        self.conexao.commit()
        print("Pokémon lendario deletado com sucesso.")

    def atualiza_pokemon(self):
        id_pokemon = self.teste_int("Digite o ID do pokemon que deseja atualizar: ")
        novo_nome = input("Nome: ")
        novo_ataque = self.teste_int('Ataque: ')
        nova_defesa = self.teste_int("Defesa: ")
        nova_vida = self.teste_int('Vida: ')
        nova_geracao = self.teste_int('Geração: ')
        quantidade = self.teste_int('quantidade de habilidades vão ser inseridas: ')
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
        id_pokemon = self.teste_int("Digite o ID do pokemon que deseja atualizar: ")
        novo_nome = input("Nome: ")
        novo_ataque = self.teste_int('Ataque: ')
        nova_defesa = self.teste_int("Defesa: ")
        nova_vida = self.teste_int('Vida: ')
        nova_geracao = self.teste_int('Geração: ')
        quantidade = self.teste_int('quantidade de habilidades vão ser inseridas: ')
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
        numero_na_pokedex = self.teste_int('Número na pokedéx: ')
        nome = input('Nome: ')
        ataque = self.teste_int('Ataque: ')
        defesa = self.teste_int('Defesa: ')
        vida = self.teste_int('Vida: ')
        geracao = self.teste_int('Geração: ')
        quantidade = self.teste_int('quantidade de habilidades: ')
        lista = []
        num = 0
        for num in range(quantidade):
            num += 1
            habilidade = input(f'{num}ª Habilidade: ')
            lista.append(habilidade)
        habilidades = str(lista)
        sql = "INSERT INTO pokemon (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades) values (%s,%s,%s,%s,%s,%s,%s)"
        valores = (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    def registrar_pokemon_lendario(self):
        numero_na_pokedex = self.teste_int('Número na pokedéx: ')
        nome = input('Nome: ')
        ataque = self.teste_int('Ataque: ')
        defesa = self.teste_int('Defesa: ')
        vida = self.teste_int('Vida: ')
        geracao = self.teste_int('Geração: ')
        quantidade = self.teste_int('quantidade de habilidades: ')
        lista = []
        num = 0
        for num in range(quantidade):
            num += 1
            habilidade = input(f'{num}ª Habilidade: ')
            lista.append(habilidade)
        habilidades = str(lista)
        sql = "INSERT INTO pokemon_lendarios (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades) values (%s,%s,%s,%s,%s,%s,%s)"
        valores = (numero_na_pokedex, nome, ataque, defesa, vida, geracao, habilidades)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        


    