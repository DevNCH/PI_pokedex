from pokedex import Professor, Conexao
professor = Professor()

while True:
    
#    try:
    
        print("          Menu de Login do Professor          \n\n\
             Qual a opção desejada?     \n\
        \n1 - Registrar conta de Professor no banco de dados da pokedex.\n\
        \n2 - Login do profesor.\n\
        \n3 - Sair do Menu.\n")
        
        escolha = int(input("Digite a opção desejada: "))
        
        if escolha == 1:
            professor.registrar_professor()
        
        elif escolha == 2:
            professor.login()
            
            while True:
            
#                try:
                
                    print("          Menu do Professor          \n\n\
Selecione a opção desejada:     \n\
1 - registrar novo pokémon\n\
2 - registrar novo pokémon lendario\n\
3 - Atualizar pokémon\n\
4 - Atualizar pokémon lendario\n\
5 - Listar pokémon por geração\n\
6 - Listar pokémon lendários por geração\n\
7 - Informações do pokémon\n\
8 - Informações do pokémon lendario\n\
9 - Deletar informações do pokémon\n\
10 - Deletar informações do pokémon lendario\n\
11 - Sair do Menu\n")

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
                                       
#                except:
#                    print("Erro")
        elif escolha == 3:
            break
                        
#    except:
#        print("Erro")
        
