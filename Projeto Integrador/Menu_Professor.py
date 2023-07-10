from pokedex import Professor, Conexao
professor = Professor

while True:
    
    try:
    
        print("          Menu de Login do Professor.          \n\n\
             Qual a opção desejada?     \n\
        \n1 - Registrar conta de Professor no banco de dados da pokedex.\n\
        \n2 - Login do profesor.\n\
        \n3 - Sair do Menu.\n")
        
        escolha = int(input("Digite a opção desejada: "))
        
        if escolha == 1:
            professor.registrar_professor()
            break
        
        elif escolha == 2:
            professor.login()
            
            while True:
            
                try:
                
                    print("          Menu do Professor.          \n\n\
                        Selecione a opção desejada:     \n\
                    \n1 - registrar novo pokémon\n\
                    \n2 - registrar novo pokémon lendario\n\
                    \n3 - Atualizar pokémon\n\
                    \n4 - Atualizar pokémon lendario\n\
                    \n5 - Listar pokémon registrados por geração\n\
                    \n6 - Listar pokémon lendaros registrados por geração\n\
                    \n7 - Imformações do pokémon\n\
                    \n8 - Imformações do pokémon lendario\n\
                    \n9 - Deleta informações do pokémon\n\
                    \n10 - Deleta informações do pokémon lendario\n\
                    \n11 - Sair do Menu\n")

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
                                       
                except:
                    print("Erro")
                        
    except:
        print("Erro")
        
