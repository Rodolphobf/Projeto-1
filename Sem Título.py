# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:28:53 2015

@author: rodolphobeninifilgueiras
"""



import random

pJogador1 = 0

CPU=0

opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']

while CPU <3 and pJogador1 <3:
        
        jogador=input('Vamos Jogar? escolha uma das opcoes !\n", pedra , papel, tesoura, lagarto e spock \n')
    
        JogadaCPU = random.choice(opcoes)
        
        print(JogadaCPU)
        
        if jogador == JogadaCPU:
            print("empatou")
            print('Placar esta: \n', pJogador1, "X", CPU)
        
        if jogador == 'pedra' and JogadaCPU == 'tesoura':
            pJogador1 += 1
            print('Voce ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
        
        if jogador == 'pedra' and JogadaCPU =='lagarto':
            pJogador1=pJogador1 + 1
            print('Voce ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
        
        if jogador== 'pedra' and JogadaCPU == 'papel':
            CPU=CPU + 1
            print("Computador ganhou 1 ponto")   
            print('Placar esta: \n ', pJogador1, "X", CPU )
            
        if jogador== 'pedra' and JogadaCPU == 'spock':
            CPU=CPU + 1
            print("Computador ganhou 1 ponto")   
            print('Placar esta: \n ', pJogador1, "X", CPU )
        
        if jogador == 'papel' and JogadaCPU == 'tesoura':
            CPU=CPU+1
            print('Computador ganhou 1 ponto')
            print('Placar esta: \n ', pJogador1, "X", CPU)
            
        if jogador == 'papel' and JogadaCPU == 'spock':
            pJogador1=pJogador1+1
            print('Voce ganhou 1 ponto')
            print('Placar esta: \n ', pJogador1, "X", CPU)
            
        if jogador == 'papel' and JogadaCPU == 'lagarto':
            CPU=CPU+1
            print('Computador ganhou 1 ponto')
            print('Placar esta: \n,', pJogador1, "X", CPU)
       
        if jogador == 'papel' and JogadaCPU == 'pedra':
            pJogador1+=1
            print('Computador ganhou 1 ponto')
            print('Placar esta: \n,', pJogador1, "X", CPU)
            
        if jogador == 'tesoura' and JogadaCPU == 'spock':
            CPU=CPU+1
            print('Computador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
          
        if jogador == 'tesoura' and JogadaCPU == 'lagarto':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'tesoura' and JogadaCPU == 'papel':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'tesoura' and JogadaCPU == 'pedra':
            CPU += 1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'spock' and JogadaCPU == 'pedra':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'spock' and JogadaCPU == 'tesoura':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'spock' and JogadaCPU == 'lagarto':
            CPU+=1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'spock' and JogadaCPU == 'papel':
            CPU+=1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'lagarto' and JogadaCPU == 'pedra':
            CPU+=1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'lagarto' and JogadaCPU == 'spock':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'lagarto' and JogadaCPU == 'papel':
            pJogador1=pJogador1+1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
        if jogador == 'lagarto' and JogadaCPU == 'tesoura':
            CPU+=1
            print('Jogador ganhou 1 ponto')
            print('Placar esta: \n', pJogador1, "X", CPU)
            
if CPU >=3:
        print(" PERDEU PLAYBOY !")
        
if pJogador1 >=3:
        print("PARABENS, MAS FOI SORTE !")
    
    

        
    