import pygame as pg
import random
from Jogo.settings import *
from Jogo.sprites import *
from os import path


class Jogo:
    def __init__(self):
        #começar o jogo
        pg.mixer.pre_init(44100, -16, 1, 512)
        pg.init()

        self.tela = pg.display.set_mode((larguraTela, alturaTela))
        pg.display.set_caption(titulo)
        #ícone do jogo
        pg.display.set_icon(pg.image.load("imagens/icone.jpg").convert_alpha())
        self.clock = pg.time.Clock()
        self.funcionando = True
        self.ganhou = False
        self.nome_fonte = pg.font.match_font(nome_fonte)
        self.carregarDados()

    def carregarDados(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "imagens")
        #carregar o spritesheet
        self.spritesheet = Spritesheet(path.join(img_dir, spritesheet, ),1)
        self.spritesheetp = Spritesheet(path.join(img_dir, "plataformas.jpg" ), 2)
        #carreagar som
        self.som_dir=path.join(self.dir,"som")
        self.sompulo = pg.mixer.Sound(path.join(self.som_dir,"pulo.wav"))
        self.sompulo.set_volume(0.3)
        self.sommoeda = pg.mixer.Sound(path.join(self.som_dir,"moeda.wav"))
        self.sommoeda.set_volume(0.3)
        self.sommorte = pg.mixer.Sound(path.join(self.som_dir, "morre.wav"))
        self.sommorte.set_volume(0.3)

    def novoJogo(self):
        #começa novo jogo
        self.placar = 0
        self.fase = 1 #linha 56
        self.fundo=Fundo()
        self.todosSprites = pg.sprite.LayeredUpdates()
        self.plataformas = pg.sprite.Group()
        self.moedas = pg.sprite.Group()
        self.jogador = Jogador(self)
        self.todosSprites.add(self.jogador)
        self.grupoFundo = pg.sprite.LayeredUpdates()
        self.grupoFundo.add(self.fundo)
        for moedas in lista_moedas1:
            m1 = Moedas(*moedas)
            self.todosSprites.add(m1)
            self.moedas.add(m1)
        for plat in lista_plataformas1:
            p1 = Plataforma(*plat,self)
            self.todosSprites.add(p1)
            self.plataformas.add(p1)
        pg.mixer.music.load(path.join(self.som_dir,"musicafase.mp3"))
        self.Rodar()

    def Rodar(self):
        #Loop do jogo
        pg.mixer.music.play(loops=-1)
        self.jogando=True
        while self.jogando:
            self.clock.tick(fps)
            self.Eventos()
            self.Atualizar()
            self.Desenhar()
        pg.mixer.music.fadeout(500)
    def Atualizar(self):
        #Loop do jogo - Update
        self.todosSprites.update()
        #Colisão moedas
        colism = pg.sprite.spritecollide(self.jogador,self.moedas, True)
        if colism:
            self.sommoeda.play()
            self.placar+=1
        #Colisão de plataforma, apenas caindo
        if self.jogador.vel.y > 0:
            colis = pg.sprite.spritecollide(self.jogador, self.plataformas, False)
            if colis:
                abaixo = colis[0]
                for col in colis:
                    if col.rect.bottom > abaixo.rect.bottom:
                        abaixo = col
                if self.jogador.pos.y < abaixo.rect.bottom:
                    self.jogador.pos.y = abaixo.rect.top+1
                    self.jogador.vel.y = 0
                    self.jogador.pulando = False
        #Scroll da tela, incompleto
        if self.jogador.rect.top <= (alturaTela/4) and self.jogador.vel.y < 0:
            self.jogador.pos.y += abs(self.jogador.vel.y)
            for moeda in self.moedas:
                moeda.rect.y += abs(self.jogador.vel.y)
            for plat in self.plataformas:
                plat.rect.y += abs(self.jogador.vel.y)
        if self.jogador.rect.right >= larguraTela:
            self.jogador.pos.x = 50
            self.fase +=1
            self.fundo.rect.x -=  larguraTela
            for moedas in self.moedas:
                moedas.rect.x -= larguraTela
                if moedas.rect.right <= 10:
                    moedas.kill()
            for plat in self.plataformas:
                plat.rect.x -= larguraTela
                if plat.rect.right <= 10:
                    plat.kill()
        #Spawnar novas plataformas, moedas
                    self.novaFase()
        #Game over
        if self.jogador.rect.top > alturaTela:
            self.sommorte.play()
            self.jogando = False
        #Final do jogo
        if self.fase > 5:
            self.ganhou = True
            self.jogando = False

    #método nova fase

    def novaFase(self):
        if self.fase == 2:
            for plat in self.plataformas:
                plat.kill()
            for plat in lista_plataformas2:
                p2 = Plataforma(*plat,self)
                self.plataformas.add(p2)
                self.todosSprites.add(p2)
            for moedas in self.moedas:
                moedas.kill()
            for moedas in lista_moedas2:
                m2 = Moedas(*moedas)
                self.moedas.add(m2)
                self.todosSprites.add(m2)
        if self.fase == 3:
            for plat in self.plataformas:
                plat.kill()
            for plat in lista_plataformas3:
                p3 = Plataforma(*plat,self)
                self.plataformas.add(p3)
                self.todosSprites.add(p3)
            for moedas in self.moedas:
                moedas.kill()
            for moedas in lista_moedas3:
                m3 = Moedas(*moedas)
                self.moedas.add(m3)
                self.todosSprites.add(m3)
        if self.fase == 4:
                for plat in self.plataformas:
                    plat.kill()
                for plat in lista_plataformas4:
                    p4 = Plataforma(*plat,self)
                    self.plataformas.add(p4)
                    self.todosSprites.add(p4)
                for moedas in self.moedas:
                    moedas.kill()
                for moedas in lista_moedas4:
                    m4 = Moedas(*moedas)
                    self.moedas.add(m4)
                    self.todosSprites.add(m4)
        if self.fase == 5:
            for plat in self.plataformas:
                plat.kill()
            for plat in lista_plataformas5:
                p5 = Plataforma(*plat,self)
                self.plataformas.add(p5)
                self.todosSprites.add(p5)
            for moedas in self.moedas:
                moedas.kill()
            for moedas in lista_moedas5:
                m5 = Moedas(*moedas)
                self.moedas.add(m5)
                self.todosSprites.add(m5)

    def Eventos(self):
        #Loop do jogo - Eventos
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                self.jogando = False
                self.funcionando = False
            if event.type == pg. KEYDOWN:
                if event.key == pg.K_UP:
                    self.jogador.Pular()
            if event.type == pg. KEYUP:
                if event.key == pg.K_UP:
                    self.jogador.Pulo_cortado()

    def Desenhar(self):
        #Loop do jogo - Desenhar
        self.grupoFundo.draw(self.tela)
        self.todosSprites.draw(self.tela)
        self.Texto(str(self.fase), 22, preto, larguraTela / 2+2, 27)
        self.Texto(str(self.fase), 22, branco, larguraTela/2, 25 )
        self.Texto("ANO", 22, preto, larguraTela / 2 + 32, 27)
        self.Texto("ANO", 22, branco, larguraTela / 2 + 30, 25)
        self.Texto("/10", 25, preto, larguraTela - 58, 20)
        self.Texto("/10", 25, branco, larguraTela - 60, 18)
        self.Texto(str(self.placar), 25, preto, larguraTela - 86, 20)
        self.Texto(str(self.placar), 25, branco, larguraTela - 88, 18)
        self.tela.blit(pg.image.load("imagens/moeda.png"), (larguraTela - 45, 20))
        #mostrar fps
        self.Texto(str(self.clock.get_fps()//1), 22, verde, 20, 0)
        #Depois de desenhar tudo
        pg.display.flip()

    def telaGanhou(self):
        if not self.ganhou or not self.funcionando:
            return
        pg.mixer.music.load(path.join(self.som_dir, "musicavitoria.mp3"))
        pg.mixer.music.play(loops=-1)
        self.gameover=pg.image.load("imagens/ganhou.jpg")
        self.tela.blit(self.gameover, (0,0))
        self.Texto("VOCÊ CONSEGUIU!", 56, preto, larguraTela / 2+3, alturaTela / 3+3-40)
        self.Texto("VOCÊ CONSEGUIU!", 56, dourado, larguraTela / 2, alturaTela / 3-40)
        self.Texto("PLACAR:", 45, preto, larguraTela / 2 + 3-80, alturaTela / 3 + 63)
        self.Texto("PLACAR:", 45, dourado, larguraTela / 2-80, alturaTela / 3+60)
        self.Texto("Pressione qualquer tecla para começar de novo", 24, preto, larguraTela / 2+3, alturaTela / 2+103)
        self.Texto("Pressione qualquer tecla para começar de novo", 24, dourado, larguraTela / 2, alturaTela / 2+100)
        self.Texto("/10", 45, preto, larguraTela/2 + 83, alturaTela / 3 + 63)
        self.Texto("/10", 45, dourado, larguraTela/2 + 80, alturaTela / 3 + 60)
        self.Texto(str(self.placar), 45, preto, larguraTela/2 + 33, alturaTela / 3 + 63)
        self.Texto(str(self.placar), 45, dourado, larguraTela/2 + 30, alturaTela / 3 + 60)
        self.tela.blit(pg.image.load("imagens/moeda.png"), (larguraTela - 385, alturaTela/3 + 75))
        pg.display.flip()
        self.pressionarTecla()
        pg.mixer.music.fadeout(500)

    def telaDeInicio(self):
        #tela inicial/menu
        pg.mixer.music.load(path.join(self.som_dir, "musica4.mp3"))
        pg.mixer.music.play(loops=-1)
        self.tela.blit(pg.image.load("imagens/fundoinicial.png"), (0,0))
        self.Texto(titulo, 56, preto, larguraTela / 2+3, alturaTela / 5+3)
        self.Texto(titulo, 56, branco, larguraTela/2, alturaTela/5)
        self.Texto("Movimentação com as setas direcionais", 24, preto, larguraTela / 2 + 3, alturaTela / 3 + 3)
        self.Texto("Movimentação com as setas direcionais", 24, branco, larguraTela/2, alturaTela / 3)
        self.Texto("Pressione qualquer tecla para começar", 24, preto, larguraTela / 2+3, alturaTela * 3 / 4+3)
        self.Texto("Pressione qualquer tecla para começar", 24, branco, larguraTela/2, alturaTela * 3/4)
        pg.display.flip()
        self.pressionarTecla()
        pg.mixer.music.fadeout(500)
    def telaFinal(self):
        #game over/continuar
        if not self.funcionando or self.ganhou:
            return
        pg.mixer.music.load(path.join(self.som_dir, "musica3.mp3"))
        pg.mixer.music.play(loops=-1)
        self.gameover=pg.image.load("imagens/fundoteste.jpg")
        self.gameover = pg.transform.scale(self.gameover,(1000,500))
        self.tela.blit(self.gameover, (0,0))
        self.Texto("Game Over!", 56, preto, larguraTela / 2+3, alturaTela / 3+3)
        self.Texto("Game Over!", 56, vermelho, larguraTela / 2, alturaTela / 3)
        self.Texto("Pressione qualquer tecla para começar de novo", 24, preto, larguraTela / 2+3, alturaTela / 2+103)
        self.Texto("Pressione qualquer tecla para começar de novo", 24, vermelho, larguraTela / 2, alturaTela / 2+100)
        pg.display.flip()
        self.pressionarTecla()
        pg.mixer.music.fadeout(500)
    def pressionarTecla(self):
        #método para esperar o usuário pressionar uma tecla
        esperar = True
        while esperar:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    esperar = False
                    self.funcionando = False
                    self.ganhou = False
                if event.type == pg.KEYDOWN:
                    esperar = False
                    self.ganhou = False


    def Texto(self, texto, tamanho, cor, x , y):
        fonte = pg.font.Font(self.nome_fonte,tamanho)
        superficie_texto = fonte.render(texto, True, cor)
        texto_rect= superficie_texto.get_rect()
        texto_rect.midtop = (x,y)
        self.tela.blit(superficie_texto, texto_rect)

j = Jogo()
j.telaDeInicio()
while j.funcionando:
    j.novoJogo()
    j.telaFinal()
    j.telaGanhou()

pg.quit()
