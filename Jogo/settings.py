#CONFIGURAÇÕES
titulo="SI Simulator"
fps=60
larguraTela=1000
alturaTela=500
nome_fonte = "arial"
spritesheet = "spritesheet_jesus.png"

#Propriedades do jogador
ace_jogador = 0.5
resis_jogador = -0.10
gravidade_jogador = 0.8
pulo_jogador = 15

#Propriedades do jogo
camadaJogador = 2
camadaPlataforma = 1
camadaInimigo = 2
camadaMoeda = 1
camadaFundo = 0

#Plataformas
lista_plataformas1 = [(0, alturaTela-40),
                    (larguraTela*3/4, alturaTela-40),
                    (larguraTela/3 , alturaTela - 170)]
lista_plataformas2 = [(0, alturaTela-39),
                    (585, alturaTela-40),
                    (larguraTela/3 , alturaTela - 100),
                      (849, 370)]
lista_plataformas3 = [(0, alturaTela-38),
                      (525, 330),
                      (665, 240),
                      (825, 130),
                    (larguraTela/3 , alturaTela - 101)]
lista_plataformas4 = [(0, alturaTela-37),
                      (260, 360),
                      (440, 240),
                      (245, 130),
                      (620, 275),
                      (545, 63),
                      (745, 180),
                      (745, -60)]
lista_plataformas5 = [(0, alturaTela-36),
                    (larguraTela -70 , alturaTela - 105)]

#Moedas
lista_moedas1 = [(larguraTela*3/4 + 50, alturaTela - 100), (larguraTela/3 + 30, alturaTela - 300)]
lista_moedas2 = [(360, 245), (625, alturaTela - 100), (800, 300)]
lista_moedas3 = [(480, 165), (840, 0)]
lista_moedas4 = [(275,-100),(920,-250)]
lista_moedas5 = [(920,230)]

#CORES
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
azulceu=(135,206,235)
verdeGrama=(124,252,0)
cinzaVerde=(47,79,79)
marrom =(130,135,0)
teste1 = (240,230,140)
teste2 = (128,0,0)
teste3 = (0,139,139)
teste4 = (100,149,237)
dourado = (255,215,0)

