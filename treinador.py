import time
from pokedex import Conexao



class Treinador(Conexao):

    def __init__(self):
        super().__init__()
    
    def treinador(self, nome, idade, cidade):
        self._nome = nome
        self._idade = idade
        self._cidade = cidade
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self.nome = valor
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, valor):
        self.idade = valor

    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self, valor):
        self.cidade = valor

    def registrar_treinador(self):
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        cidade = input('digite sua cidade: ')
        sql = "INSERT INTO treinadores (nome, idade, cidade) VALUES (%s, %s, %s)"
        val = (nome, idade, cidade)
        self.cursor.execute(sql, val)
        self.conexao.commit() 
        self.cursor.execute(f"select * from treinadores where nome = '{nome}'")
        treinador = self.cursor.fetchone()
        print(f'treinador registrado\nSeu ID é {treinador[0]}')
    
    def pegar_id(self):
        self.cursor.execute(f"select * from treinadores where nome = '{self.nome}'")
        treinador = self.cursor.fetchone()
        return treinador[0]
    
      
class Pokedex(Conexao):

    def login(self):

        while True:
            id_treinador = int(input('Insira seu id: '))
            nome = input('Insira seu nome: ')
            sql = f"SELECT * FROM treinadores where id_treinador = '{id_treinador}';"
            self.cursor.execute(sql)
            treinador = self.cursor.fetchone()
        
            try:
                
                if id_treinador != treinador[0] or  nome != treinador[1]:
                    print("sem registro")
                    return False
            
                elif id_treinador != treinador[0] and nome == treinador[1]:
                    print("ID incorreta")
                    return False
        
                if nome == treinador[1] and  id_treinador == treinador[0]:
                    print(treinador[0], treinador[1])
                    print("login efetuado")
                    return True
        
            except:
                print('Conta não encontrada.')



    def escolher_primero_pokemon(self, id_treinador):
        pokedex = Pokedex()
        pokemon1 = pokedex.procura_pokemon(1)
        pokemon2 = pokedex.procura_pokemon(4)
        pokemon3 = pokedex.procura_pokemon(7)


        print(f"Escolha um dos seguintes pokémons para ser o seu primeiro:")
        print(f"1 - {pokemon1[1]} (Tipo: {pokemon1[2]}, ataque: {pokemon1[3]})")
        print(f"2 - {pokemon2[1]} (Tipo: {pokemon2[2]}, ataque: {pokemon2[3]})")
        print(f"3 - {pokemon3[1]} (Tipo: {pokemon3[2]}, ataque: {pokemon3[3]})")
        
        escolha = None
        tempo_inicial = time.localtime()
        while True:
            escolha = input('digite o número do pokémon que você quer escolher: ')
            
            if escolha in ['1', '2', '3']:
                escolha = int(escolha)
                match escolha:
                    case 2: escolha = 4
                    case 3: escolha = 7
                break
            
            else:
                print(' entrada invalida. digite 1, 2 ou 3.')
                tempo_atual = time.localtime()
                if float(time.strftime("%S",tempo_atual)) - float(time.strftime("%S",tempo_inicial)) > 10:
                    print("Tempo esgotado. Um pikachu será escolhido pelo sistema.")
                    escolha = 25
                    break
        
        self.cursor.execute(f"select * from pokemon where numero_na_pokedex = {escolha}")
        pokemon = self.cursor.fetchone()
        self.importa_pokemon(id_treinador, escolha, pokemon[1])
        print(f"Parabéns! Você escolheu o {pokemon[1]} como seu primeiro pokémon.")
                             
   
    
    def solta_pokemon(self):
        id_pokemon = int(input("Digite o ID do pokémon que deseja solta: "))
        sql = f"DELETE FROM pokemon_coletados WHERE id_pokemon = {id_pokemon}"
        self.cursor.execute(sql)
        self.conexao.commit()
        
        print("Pokémon solto com sucesso.")
    
    def nomea_pokemon(self):
        lista = self.lista_pokemon_capturados('não')
        
        num = 1

        for pokemon in lista:
            print(f'{num} - {pokemon[2]}')

            num += 1
       
        Escolha = int(input('Insira o número do pokémon de escolha: '))
        escolha = lista[Escolha-1]
       
        print(escolha[2])
       
        id = escolha[1]
        novo_nome = input('Insira o novo nome do pokémon: ')
        sql = "UPDATE pokemon_coletados SET nome_pokemon = %s WHERE id_pokemon = %s"
        valores = (novo_nome, id)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        
        print("pokemon renomeado com sucesso")

    def lista_pokemon_capturados(self, opcao):
        id_treinador = int(input("Digite o ID do treinador: "))
        lista = []
        sql = f"SELECT * FROM pokemon_coletados WHERE id_treinador = {id_treinador}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        
        if opcao == 'print':
            print('número na pokedéx - nome')
        
        for pokemon in resultado: 
            lista.append(pokemon)
            if opcao == 'print':
                
                print(f'{pokemon[1]} - {pokemon[2]}')
        
        
        return lista
    
    def procura_pokemon(self, id):
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
            return None
        
        else:
            return resultado
        
    def exibir_pokemon(self):
        id_pokemon = int(input("digite o ID do pokemon: "))
        sql =f"SELECT * FROM pokemon WHERE numero_na_pokedex = {id_pokemon}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if resultado is None:
            print('pokémon não encontrado')
        
        else:
             print(f"nome: {resultado[1]}\nataque: {resultado[2]}\ndefesa: {resultado[3]}\nhabilidades: {resultado[6]}")

    def importa_pokemon(self, id_treinador, id_pokemon, nome_pokemon):
        self.cursor.execute(f"insert into pokemon_coletados (id_treinador,id_pokemon,nome_pokemon) values ({id_treinador},{id_pokemon},'{nome_pokemon}')")
        self.conexao.commit()
    
    


