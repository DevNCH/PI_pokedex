from treinador import Treinador, Pokedex

nome = input('nome: ')
idade = int(input('idade: '))
cidade = input('cidade: ')

treinador1 = Treinador(nome, idade, cidade)

treinador1.registrar_treinador()

treinador1.pokedex_treinador()
pokedex=Pokedex()

pokedex.escolher_primero_pokemon()
pokedex.fecha_conexao()