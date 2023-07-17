from treinador import Treinador, Pokedex
from pokedex import  Conexao, Tenta_quebrar
from batalha import batalha
conexao = Conexao()
treinador = Treinador()
pokedex = Pokedex()
captura = batalha()
seguranca = Tenta_quebrar()

while True:
    
    print("----------Menu de login do treinador----------\n\
    \n1 - Registrar treinador\
    \n2 - login de treinador\
    \n3 - Fechar login da pokedéx\n")

    escolha = seguranca.teste_int("Digite a opção desejada: ")

    if escolha == 1:
        
        treinador = treinador.registrar_treinador()
        pokedex.escolher_primero_pokemon(treinador) 
            
    elif escolha == 2:

        pokedex.login()

        while True:
            
            print("\n\n----------Menu da pokedex----------\n\
            \n1 - Capturar pokémon\
            \n2 - Renomear pokémon\
            \n3 - Listar pokémon capturados\
            \n4 - Procurar pokémon\
            \n5 - Soltar pokémon\
            \n6 - Sair do Menu\n")
            
            escolha = seguranca.teste_int("Digite a opção desejada: ")
            
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
                pokedex.fecha_conexao()
                break
            
            else:
                print("\nEscolha inválida")
        
        break
    
    elif escolha == 3:
        break

    else:
        print("Opção inválida")