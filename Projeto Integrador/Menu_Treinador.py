
import mysql.connector
from treinador import Treinador, Pokedex
from pokedex import  Conexao
from batalha import batalha
conexao = Conexao()
treinador = Treinador()
pokedex = Pokedex()
captura = batalha()
conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Senac2021",
            database="pokedex")
cursor = conexao.cursor()

while True:
    
    try:
        
        print("          Menu de login da Pokedex          \n\n\
            Qual opção desejada:\n\
        \n1: Registra jogador\n\
        \n2: Fazer login")

        escolha = int(input("\n\nDigite a opção desejada: "))

        if escolha == 1:
            treinador.registrar_treinador()
            
            while True:
            
                try:
            
                    id_treinador = int(input('Digite seu ID para continuar: '))
                    sql = f"SELECT * FROM treinadores where id_treinador = '{id_treinador}';"
                    cursor.execute(sql)
                    treinador = cursor.fetchone()
                
                    if id_treinador == treinador[0]:
                        pokedex.escolher_primero_pokemon(id_treinador)
                        break
                
                    elif id_treinador != treinador[0]:
                        print("ID não encontrado")
                
                except:
                    print("Erro em escolher pokémon")
                
                
        elif escolha == 2:
            pokedex.login()
            break
            
        else:
            print("Opção inválida")
            
    except:
        print("Erro no menu")

while True:

    try:
        
        print("          Menu da pokedex          \n\n\
            Qual opção desejada:\n\
        \n1: Capturar pokémon\n\
        \n2: Renomear pokémon\n\
        \n3: Listar pokémon capturados\n\
        \n4: Procurar pokémon\n\
        \n5: Soltar pokémon\n\
        \n6: Sair do Menu\n")
        
        escolha = int(input("Digite a opção desejada: "))
        
        if escolha == 1:
            captura.captura_pokemon()
            
        elif escolha == 2:
            pokedex.nomea_pokemon()
            
        elif escolha == 3:
            pokedex.lista_pokemon_capturados()
        
        elif escolha == 4:
            pokedex.exibir_pokemon()
            
        elif escolha == 5:
            pokedex.solta_pokemon()
            
        elif escolha == 6:
            break
        
        else:
            print("\nEscolha inválida")
        
    except:
        print("\nVoçê errou tente novamente")
        
conexao.close()