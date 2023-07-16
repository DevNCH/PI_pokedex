from pokedex import Professor
professor = Professor()

while True:
    
    print("\n\n----------Menu de Login do Professor----------\n\
    \n1 - Criar conta de professor\
    \n2 - Login de profesor\
    \n3 - Sair do programa\n")
    
    try:
        escolha = int(input("Digite a opção desejada: "))
    
    except:
        print('Não é um número inteiro.')
        continue
    
    if escolha == 1:
        professor.registrar_professor()
    
    elif escolha == 2:
        professor.login()
        
        while True:
        
            print("----------Menu do banco de dados----------\n\
            \n1 - registrar novo pokémon\
            \n2 - registrar novo pokémon lendário\
            \n3 - Atualizar pokémon\
            \n4 - Atualizar pokémon lendário\
            \n5 - Listar pokémon por geração\
            \n6 - Listar pokémon lendários por geração\
            \n7 - Informações de um pokémon\
            \n8 - Informações de um pokémon lendário\
            \n9 - Deletar informações do pokémon\
            \n10 - Deletar informações do pokémon lendário\
            \n11 - Sair do menu do professor\n")

            escolha = int(input("Digite a opção desejada: "))
            
            if escolha == 1:
                professor.registrar_pokemon()
            
            elif escolha == 2:
                professor.registrar_pokemon_lendario()
                
            elif escolha == 3:
                professor.atualiza_pokemon()
                
            elif escolha == 4:
                professor.atualiza_pokemon_lendarios()
                                
            elif escolha == 5:
                professor.lista_geracao_pokemon()
                
            elif escolha == 6:
                professor.lista_geracao_pokemon_lendarios()  
            
            elif escolha == 7:
                professor.informacoes_pokemon()
                
            elif escolha == 8:
                professor.informacoes_pokemon_lemdario()
                
            elif escolha == 9:
                professor.deleta_pokemon()
                                
            elif escolha == 10:
                professor.deleta_pokemon_lendario()
                
            elif escolha == 11:
                break
            
            else:
                print('Escolha invalida')               
    
    elif escolha == 3:
        break

    else:
        print('Escolha inválida')

        
