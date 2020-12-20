#classes sprite
import pygame as pg
from settings import *
import random
vetor = pg.math.Vector2

class Spritesheet:
    #utilidade, imagens, ainda não sei como funciona
    def __init__(self, nomeArquivo,x):
        if x == 1:
            self.spritesheet = pg.image.load(nomeArquivo).convert()
        else:
            self.spritesheetp = pg.image.load(nomeArquivo).convert()
    def cortar(self, x, y, lar, alt):
        #corta a imagem desejada da spritesheet
        imagem = pg.Surface((lar, alt))
        imagem.blit(self.spritesheet, (0, 0), (x, y, lar, alt))
        #para diminuir o tamanho da imagem
        imagem = pg.transform.scale(imagem, (lar//4, alt//4))
        return imagem
    def cortar2(self, x, y, lar, alt):
        #corta a imagem desejada da spritesheet
        imagem = pg.Surface((lar, alt))
        imagem.blit(self.spritesheetp, (0, 0), (x, y, lar, alt))
        return imagem

class Moedas(pg.sprite.Sprite):
    def __init__(self, x, y):
        self._layer = camadaJogador
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("imagens/moeda.png")
        self.image.set_colorkey(preto)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Fundo(pg.sprite.Sprite):
    def __init__(self):
        self._layer = camadaFundo
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load("imagens/fundo2.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Jogador(pg.sprite.Sprite):
    def __init__(self, Jogo):
        self._layer = camadaJogador
        pg.sprite.Sprite.__init__(self)
        self.Jogo=Jogo
        self.andando = False
        self.pulando = False
        self.frameAtual = 0
        self.ultimaMudanca = 0
        self.carregarImagens()
        self.image = self.framesParados[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (larguraTela/2, alturaTela/2)
        self.pos = vetor(50, alturaTela/2)
        self.vel = vetor(0,0)
        self.ace = vetor(0,0)

    def carregarImagens(self):
        self.framesParados = [self.Jogo.spritesheet.cortar(50, 430,130,300),
                              self.Jogo.spritesheet.cortar(820, 50,130,300)]
        for frames in self.framesParados:
            frames.set_colorkey(preto)
        self.framesEsquerda = [self.Jogo.spritesheet.cortar(460, 40,140,300),
                               self.Jogo.spritesheet.cortar(160, 30,140,300)]
        self.framesDireita = []
        for frames in self.framesEsquerda:
            frames.set_colorkey(preto)
            self.framesDireita.append(pg.transform.flip(frames, True, False))
        self.framePulo = self.Jogo.spritesheet.cortar(320, 420,240,280)
        self.framePulo.set_colorkey(preto)

    def Pular(self):
        #Pular apenas se estiver em cima de uma plataforma
        self.rect.y +=2
        coli = pg.sprite.spritecollide(self, self.Jogo.plataformas, False)
        self.rect.y -=2
        if coli and not self.pulando:
            self.Jogo.sompulo.play()
            self.pulando = True
            self.vel.y = -pulo_jogador

    def Pulo_cortado(self):
        if self.pulando:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self):
        self.animar()
        self.ace = vetor(0,gravidade_jogador)
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.ace.x = -ace_jogador
        if teclas[pg.K_RIGHT]:
            self.ace.x = ace_jogador


        #Aplica resistência
        self.ace.x += self.vel.x * resis_jogador
        #Equações de movimento, vetores
        self.vel += self.ace
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.ace
        #Para atravessar a tela
        if self.pos.x > larguraTela:
            self.pos.x = 0
        if self.pos.x < 20:
            self.pos.x = 0 +20

        self.rect.midbottom = self.pos

    def animar(self):
        #feita a animação do personagem usando frames
        agora = pg.time.get_ticks()
        if self.vel.x != 0:
            self.andando = True
        else:
            self.andando = False
        #animação andando
        if self.andando:
            if agora - self.ultimaMudanca > 200:
                self.ultimaMudanca = agora
                self.frameAtual = (self.frameAtual + 1) % len(self.framesDireita)
                pes = self.rect.bottom
                if self.vel.x >0:
                    self.image = self.framesDireita[self.frameAtual]
                else:
                    self.image = self.framesEsquerda[self.frameAtual]
                self.rect = self.image.get_rect()
                self.rect.bottom = pes

        #animação parado
        if not self.pulando and not self.andando:
            if agora - self.ultimaMudanca > 300:
                self.ultimaMudanca = agora
                self.frameAtual = (self.frameAtual + 1) % len(self.framesParados)
                self.image = self.framesParados[self.frameAtual]
        #animação pulo
        if self.pulando:
            self.image = self.framePulo
class Plataforma(pg.sprite.Sprite):
    def __init__(self, x, y, Jogo):
        global escolha
        self._layer = camadaPlataforma
        self.Jogo=Jogo
        pg.sprite.Sprite.__init__(self)
        plataformas = [self.Jogo.spritesheetp.cortar2(0,0,750,40),
                       self.Jogo.spritesheetp.cortar2(0, 100, 200, 40),
                       self.Jogo.spritesheetp.cortar2(0, 100, 600, 40),
                       self.Jogo.spritesheetp.cortar2(0, 200, 100, 30),
                       self.Jogo.spritesheetp.cortar2(0, 100, 135, 40),
                       self.Jogo.spritesheetp.cortar2(0, 300, 40, 30),
                       self.Jogo.spritesheetp.cortar2(0, 350, 220, 40),
                       self.Jogo.spritesheetp.cortar2(0, 450, 600, 40),
                       self.Jogo.spritesheetp.cortar2(200, 200, 100, 30),
                       self.Jogo.spritesheetp.cortar2(400, 200, 100, 30)]
        if x == 0 and y == alturaTela-40:
            escolha = 2
        elif x == larguraTela/3 and y == alturaTela - 170:
            escolha = 3
        elif x == 0 and y == alturaTela-39:
            escolha = 1
        elif (x == larguraTela/3 and y == alturaTela - 100) or (x == 849 and y == 370):
            escolha = 3
        elif x == 585 and y == alturaTela-40:
            escolha = 4
        elif x == 0 and y == alturaTela-38:
            escolha = 6
        elif (x == larguraTela/3 and y == alturaTela-101) or x == 525 or x == 665 or x == 825:
            escolha = 8
        elif y == alturaTela - 37:
            escolha = 7
        elif x == 260 or x == 440 or x == 245 or x == 620 or x == 545 or x == 745:
            escolha = 9
        elif y == alturaTela - 36:
            escolha = 0
        elif x == larguraTela-70:
            escolha = 5

        self.image = plataformas[escolha]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Texturas():
    pass