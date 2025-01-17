#Essa classe será constituída por uma função, função essa que será chamada pela classe jogo quando o jogador pressionar a tecla "ESC"
#se quiser visualizar a interface, basta chamar a função pause na classe menu
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.gameimage import *
from options import options

#inicializações
screen = Window(1224, 720);
mouse = Window.get_mouse();

background = GameImage("Assets/backgrounds/sky1.png");

#função pause
def pause ():
    #colocando o logo pause encima da tela
    pausar = Sprite("Assets/pause/pauselg.png");
    pausar.set_position(screen.width/2 - pausar.width/2, screen.height/16);

    #inicializando o botão: retorna para o jogo
    retrn = Sprite("Assets/pause/rtrn.png");
    retrn.set_position(screen.width/2 - retrn.width/2, screen.height/1.31);

    retrnpink = Sprite("Assets/pause/pinkretrn.png");
    retrnpink.set_position(screen.width/2 - retrnpink.width/2, screen.height/1.31);

    #inicializando o botão: opções
    opt = Sprite("Assets/pause/opt.png");
    opt.set_position(screen.width/2 - opt.width/2, screen.height/1.21);

    optpink = Sprite("Assets/pause/pinkopt.png");
    optpink.set_position(screen.width/2 - opt.width/2, screen.height/1.21);

    #inicializando o botão: sair (que leva ao menu principal)
    qt = Sprite("Assets/pause/quit.png");
    qt.set_position(screen.width/2 - qt.width/2, screen.height/1.125);

    qtpink = Sprite("Assets/pause/pinkquit.png");
    qtpink.set_position(screen.width/2 - qt.width/2, screen.height/1.125);

    #Game Loop
    while True:
        background.draw();

    #botão quit
        if (mouse.is_over_object(qt)):
            qt.hide();
            qtpink.draw();
            if (mouse.is_button_pressed(1)):
                return True;
        else:
            qt.unhide();

    #botão opções
        if (mouse.is_over_object(opt)):
            opt.hide();
            optpink.draw();
            if (mouse.is_button_pressed(1)): 
                options();
        else:
            opt.unhide();
        
    #botao retorna
        if (mouse.is_over_object(retrn)):
            retrn.hide();
            retrnpink.draw();
            if (mouse.is_button_pressed(1)):
                return False;
        else:
            retrn.unhide();
        
        pausar.draw();
        retrn.draw();
        opt.draw();
        qt.draw();
        screen.update();