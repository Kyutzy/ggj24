﻿define cookie = Character("Cookie")
define panetone = Character("Panetone")
define massa = Character("Massa")
define pizza = Character("Pizza")
define pao_de_viagem = Character("Pão de Viagem")

define todos = Character("Todos")
define narrador = Character("Narrador")

define back = "bgmain.png"

label start:
    window hide
    show inicio
    play music "bgm.mp3" 
    pause
    jump game

label game:
    
    transform cookie_meio:
        xalign 0.5 yalign 0.70 zoom 0.2
    transform panetone_meio:
        xalign 0.5 yalign 0.56 zoom 0.92
    transform massa_meio:
        xalign 0.5 yalign 0.65 zoom 1.0
    transform pizza_meio:
        xalign 0.5 yalign 0.50 zoom 0.4
    transform pao_de_viagem_meio:
        xalign 0.5 yalign 0.66 zoom 0.2

    # Contadores para o final
    $ contFesta = 0
    $ contCasa = 0
    $ contCalma = 0
    $ contViagem = 0

    $ Introducao = ["cena_1", "cena_2"]
    $ Final_Pizza = ["cena_1", "cena_2"]    # Festa & Viagem 
    $ Final_Panetone = ["cena_1", "cena_2"] # Festa e Casa
    $ Final_Cookie = ["cena_1", "cena_2"]   # Casa e Calma
    $ Final_Bolor =  ["cena_1", "cena_2"]   # Casa e Viagem
    
    default pergunta1 = False
    default pergunta2 = False
    default pergunta3 = False
    default pergunta4 = False
    default pergunta5 = False

    # ================================== #
    #            INTRODUCAO              #
    # ================================== #
    # while Introducao:
    #     scene bg "[Introducao[0]]" 
    #     $ Introducao.pop(0)
    #     pause 3

    # ================================== #
    #              INICIO                #
    # ================================== #
    scene bgmain

    
    narrador "Pou, um som estrodoso. Lentamente, o mundo parece se mover em uma direção. Ao fundo, um barulho do crepitar das chamas pode ser ouvido. Está tudo muito escuro."

    show pao_de_viagem at pao_de_viagem_meio 
    pao_de_viagem "Essa não… morremos…"
    hide pao_de_viagem
    
    show pizza at pizza_meio
    pizza "NÃÃÃÃÃÃOOOOOO, eu sou lindo demais para morrer"
    hide pizza 

    show panetone at panetone_meio
    panetone "Não sei o que está acontecendo mas sei que isso com certeza nos amassou :D"
    hide panetone

    narrador "A MASSA se levanta da superfície gelada, ainda um pouco confusa pela queda"

    show massa duvida at massa_meio
    massa "A gente não morreu, pessoal. A gente chegou na ESTEIRA"
    hide massa

    todos "Ahhhhhhhhhhhh…"

    narrador "As luzes se acendem. A MASSA se vê dentro de um espaço amplo, cercado de paredes de metal. O fogo está à espreita, aquecendo o ambiente cada vez mais."

    show pizza smile at pizza_meio
    pizza "Então é aqui que vou pegar um bronze! Mal posso esperar"
    hide pizza 

    show pao_de_viagem at pao_de_viagem_meio
    pao_de_viagem "Não é assim que funciona… aqui é nosso fim. Não tem mais para onde ir"
    hide pao_de_viagem
    
    show cookie at cookie_meio
    cookie "Não fique tristinho, pelo menos ainda somos um"
    hide cookie

    show massa sad at massa_meio
    massa "É verdade, vocês ainda são parte de mim, saco"
    hide massa
    
    show cookie at cookie_meio
    cookie "hihihihihi"
    hide cookie

    show pizza flex at pizza_meio
    pizza "Vocês acham que parte dele conseguiria fazer isso?"
    hide pizza 

    narrador "MASSA ouve sons que soam como grunhidos de esforço de alguém fazendo várias poses de musculação."

    show pao_de_viagem at pao_de_viagem_meio
    pao_de_viagem "Estamos prestes a deixar de existir e é isso é isso que escolhe fazer?"
    hide pao_de_viagem

    show pizza smile at pizza_meio
    pizza "Pelo menos eu não fico choramingando por um calorzinho"
    hide pizza

    show massa mad at massa_meio
    massa "Ei, sem brigas por aqui"
    hide massa

    show panetone at panetone_meio
    panetone "É isso aí! Se não vou sovar vocês!"
    hide panetone

    show pizza flex at pizza_meio
    pizza "Se for sovar eu quero ajudar!"
    hide pizza

    massa "(...)"

    show massa mad at massa_meio
    massa "É difícil aceitar que vocês são parte de mim…" 
    hide massa  

    show massa sad at massa_meio
    narrador "Olhando ao redor, A MASSA percebe que está sozinha, e não tem muito como escapar. As paredes de sua plataforma de metal que lentamente avança no caminho são altas demais para que consiga escalar."

    massa "A jornada parece ser longa… e agora? Só eu por um tempo?"
    show massa duvida at massa_meio
    massa "O que será que está por vir?"
    hide massa

    # ================================== #
    #            Perguntas               #
    # ================================== #

    label perguntar:
        menu:
            "O que vai acontecer depois da morte?" if not pergunta1:
                $   pergunta1 = True
                jump p1
            "Se você fosse Rei, o que eu faria?" if not pergunta2:
                $ pergunta2 = True
                jump p2
            "Qual superpoder você gostaria de ter?" if not pergunta3:
                $ pergunta3 = True
                jump p3
            "Do que eu mais tenho medo?" if not pergunta4:
                $ pergunta4 = True
                jump p4
            "Que história eu gostaria de viver?" if not pergunta5:
                $ pergunta5 = True
                jump p5
            "Chega de pensar." if pergunta1 and pergunta2 and pergunta3 and pergunta4 and pergunta5:
                jump decidirFinal

    # ================================== #
    #                P1                  #
    # ================================== #

    label p1:
        show cookie at cookie_meio
        cookie "Ah, talvez nós iremos para uma linda fazenda onde vão todas as massas que caíram no chão. E podemos andar pelos campos e nadar nas lagoas"
        hide cookie

        show massa happy
        massa "Isso não soa nada ruim, na verdade."
        hide massa

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Sempre achei que seria como andar em um fundo de um lago sem nenhuma luz… Sem fim… até que não sinta mais nem o passar do tempo"
        hide pao_de_viagem 

        show panetone safado at panetone_meio
        panetone "Meio sombrio não? Sabe qual a grande diferença entre o lago e a padaria afinal? É que na padaria assa pão, no lagoa há sapinho"
        hide panetone
        
        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Vão assar a gente?"
        hide pao_de_viagem

        show massa happy
        massa "Sim… mas talvez não seja tão ruim, chegou minha hora de crescer"
        hide massa

        show panetone at panetone_meio
        panetone "Ok… Sendo assim, prefiro pensar em algo mais feliz. Que tal um grande espetáculo? Com música, dança, e tudo que quiser? Merecemos algo assim depois disso aqui não é mesmo?"
        hide panetone

        show pizza flex at pizza_meio
        pizza "Não, porque nunca vou morrer! AH É! 37 jogos sem nenhuma derrota! segura o pai."
        hide pizza

        show massa at massa_meio
        massa "Do que você está falando? De que jogos?"
        hide massa

        show pizza smile at pizza_meio
        pizza "É isso aí pô, Só vitória atrás de vitória, segue o líder. Saindo dessa quem topa uma cerva? To louco pra festar ao som de mc bread! Mostrar como se faz nas quebrada família"
        hide pizza    

        # ================================== #
        #            ESCOLHA 1               #
        # ================================== #

        menu:
            "Acho que prefiro mesmo descansar, ainda mais depois de ter que escutar vocês por tanto tempo. ":
                $ contCalma += 1

            "Realmente, pizza bora curtir e deixar rolar.":
                $ contFesta += 1
        # ================================== #

        show cookie at cookie_meio
        cookie "Pena que ninguém nunca voltou para falar o que tinha lá do outro lado, se eu conseguir eu corro atrás de vocês"
        hide cookie

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Não deve ter coisa boa lá, deve ser ruim…"
        hide pao_de_viagem

        show cookie at cookie_meio
        cookie "Ou talvez eles gostem tanto de lá que não querem mais sair"
        hide cookie

        show pizza at pizza_meio
        pizza "Talvez não tivesse um forte igual eu pra conseguir voltar, segue o líder tropa *Grunhidos de poses*"
        hide pizza

        show cookie unhappy at cookie_meio
        cookie "Deve mesmo ser um trabalhão para fazer essa viagem né? Acho que euzinha ia preferir ficar por onde estivesse mesmo."
        hide cookie

        show panetone at panetone_meio
        panetone "Pelo menos se pararmos lá daria para… descansar… hã, hã? Tipo massa?"
        hide panetone

        # ================================== #
        #            ESCOLHA 2               #
        # ================================== #

        menu:
            "Acho que depois de me acostumar com o outro lado não teria porque voltar.":
                $ contCasa += 1

            "Se fosse possível eu iria e voltaria como se tivesse fazendo um passeio no parque ":
                $ contViagem += 1
        jump perguntar

    # ================================== #

    # ================================== #
    #                P2                  #
    # ================================== #

    label p2:
        show pizza at pizza_meio
        pizza "Conquistaria todos os reinos que não se curvarem em frente à minha força"
        hide pizza
        
        show massa at massa_meio
        massa "Isso foi um pouco rápido demais"
        hide massa

        show pizza flex at pizza_meio
        pizza "Assim como será minha campanha. vou controlar o mundo todo, VAPO. MUAHAHA"
        hide pizza

        show cookie at cookie_meio
        cookie "Para que isso, meu bom. Que tal fazer um grande jardim para o reino, onde todos possam cultivar trigo para ter sua própria farinha. Hmmmm, que delicinha :)"
        hide cookie

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Ah, se for pra trabalhar eu não quero não, ninguém me avisou que precisaria de tanto trabalho manual"
        hide pao_de_viagem

        show pizza at pizza_meio
        pizza "Vou pegar todos os trigos dos meus plebeus e fazer farinha pra crescer meus bíceps massudos"
        hide pizza

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Nãoooooo… mas e se quiserem fazer isso com a gente"
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Prefiro que venham até meu reino, muito mais fácil. Me agradem com seus ovos."
        hide panetone

        show massa at massa_meio
        massa "E porque eles fariam isso?"
        hide massa

        show panetone at panetone_meio
        panetone "Ah, porque… porque… eu mandei(?). Talvez eu não fosse o melhor rei, mas com certeza seria o mais satisfeito .( ͡° ͜ʖ ͡°)"
        hide panetone

        # ================================== #
        #            ESCOLHA 3               #
        # ================================== #
        
        menu:
            "Sendo rei, poderia conhecer todos e cada uma de suas histórias, desde que eram apenas massas como eu. ":
                $ contViagem += 1

            "Se eu fosse rei, não me preocuparia em sair por aí, por que conhecer outros lugares se tenho tudo o que preciso por aqui.":
                $ contCasa += 1

        # ================================== #

        show pizza at pizza_meio
        pizza "Como eu chegaria a ser rei? numa competição de levantamento de massa, óbvio!"
        hide pizza

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "O que isso tem a ver com qualquer coisa?"
        hide pao_de_viagem

        show pizza at pizza_meio
        pizza "(Cantando, sem ouvir) - EU SERIA O REI! CONQUISTADOR DOS INIMIGOS! COM GRANDES BÍCEPS!"
        hide pizza

        show panetone at panetone_meio
        panetone "Ah… Ok… (Cantando) ELE É O REI!!!"
        hide panetone

        # ================================== #
        #            ESCOLHA 4               #
        # ================================== #

        menu:
            "Ovos e especiarias… acho que como rei mereceria alguns luxos.":
                $ contFesta += 1

            "A primeira coisa que faria como rei seria distribuir uma chapa para cada pão, todos merecem uma tarde tranquila com manteiga e amendoim.":
                $ contFesta += 1

        # ================================== #

        show cookie at cookie_meio
        cookie "Talvez o melhor, meu bem, seja apenas não ser rei…?"
        hide cookie
        jump perguntar

    # ================================== #
    #                P3                  #
    # ================================== #

    label p3:
        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Acho que… acho que teletransporte. Eu poderia fugir de qualquer situação desagradável imediatamente. Uma vida sem pães amanhecidos(SUSPIRO)"
        hide pao_de_viagem

        show pizza at pizza_meio
        pizza "Isso é positivo para você? SUPER FORÇA, SUPER VELOCIDADE, SUPER RESISTÊNCIA. Posso lutar e sovar qualquer panificado."
        hide pizza

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Eu murcho só de pensar nisso."
        hide pao_de_viagem

        show cookie at cookie_meio
        cookie "Concordo. Muita bagunça! Por isso já sei que iria mover as coisas com a mente! Poderia trazer meus caros leite e bolo  para perto e levar os indesejados confetes para longe sem fazer força. "
        hide cookie

        show massa at massa_meio
        massa "Até você?"
        hide massa

        show cookie at cookie_meio
        cookie "Nunca disse que discordava do conflito, só discordo do método!"
        hide cookie

        show panetone at panetone_meio
        panetone "Para que se ocupar com brigas quando se tem o melhor poder logo a sua frente? Fazer cópias de mim mesmo! Poderia lotar qualquer lugar só comigo! Seria uma verdadeira “multipão”"
        hide panetone

        # ================================== #
        #            ESCOLHA 5               #
        # ================================== #

        menu:
            "Prefiro tirar o meu da reta, algo que me colocasse fora do perigo e amaciasse os ânimos seria muito melhor com certeza.":
                $ contCalma += 1
            "Do que adianta um poder se não posso aproveitar bem? Quero estar na ação, com a mão na massa… AHHH, FOI SEM QUERER":
                $ contFesta += 1

        # ================================== #

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Com a possibilidade de poderes assim, acho que a primeira coisa que faria seria ir para o mais longe daqui possível. Menos chance de problemas, menos incômodo para todo mundo."
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Como se incômodo não tivesse em todo lugar hehe Se fosse por isso seria melhor ir para onde não tem pessoa nenhuma"
        hide panetone

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Ah é?…"
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Por isso eu ficaria bem onde estivesse. Os incômodos seriam interceptados por meus fiéis clones. Ai eu poderia apenas aproveitar onde estivesse com toda paz do mundo e com as melhores companhias"
        hide panetone

        show cookie at cookie_meio
        cookie "Até que soa bem, boa idéia queridinho. Para que achar problemas por aí, quando posso alcançar tudo ao meu redor? Imagina só hihi. Sem mexer um dedinho"
        hide cookie

        show pizza at pizza_meio
        pizza "Não teria como ficar parado. COM MEUS INCRÍVEIS PODERES TODOS SERIAM DERROTADOS AONDE QUER QUE ESTIVESSE. Teria que sair para encontrar mais inimigos dignos."
        hide pizza

        # ================================== #
        #            ESCOLHA 6               #
        # ================================== #

        menu:
            "Fugir dos problemas raramente funciona, ainda mais em um mundo com super problemas. Prefiro ficar onde estou e usar meus poderes.":
                $ contCasa += 1

            "Viajar em super velocidade parece exatamente o que precisaria para resolver os problemas de longas distâncias. Acho que o problema ia ser a falta do que fazer depois de um tempo.":
                $ contViagem += 1
        jump perguntar

    # ================================== #

    # ================================== #
    #                P4                  #
    # ================================== #

    label p4:
        show panetone at panetone_meio
        panetone "Sempre se acha que não se teme nada até ficar de frente a isso, certo? hehe. "
        # mudar expressão
        show panetone at panetone_meio 
        panetone "De repente estar nesse caminho me fez sentir tanta falta das vozes, dos barulhos das pessoas. O silêncio é tão alto…"
        hide panetone

        show pizza at pizza_meio
        pizza "É difícil não ter uma platéia. É difícil saber que ninguém está ali para te ver, por mais INCRÍVEL que seja o que estiver fazendo. Me faz sentir tão pequeno."
        hide pizza

        show cookie at cookie_meio
        cookie "Ah benzinho, é nisso que acho conforto. Não consigo nem pensar em quando é demais. Até me desregula aqui. Tanta coisa, tanto peso. Não faz bem não."
        hide cookie

        show pizza at pizza_meio
        pizza "SIM, ISSO MESMO. PESO! É disso que preciso! Quanto mais melhor. Não quero ficar sem peso. Ai como sei que estou ali?"
        hide pizza

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Mas com mais e mais parece que se precisa fazer mais e mais. E se não conseguir? E se eu desapontar? Como vou aguentar isso… não vou…"
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Ei ei, não precisa… se acalme. Você sabe que estamos entre… amidos…"
        hide panetone

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "hehe, ok, acho que consigo me acalmar"
        hide pao_de_viagem

        # ================================== #
        #            ESCOLHA 7               #
        # ================================== #

        menu:
            "Ficar sozinho, sem ninguém. O silêncio, o escuro. Acho que estou vivendo meu maior medo agora mesmo.":
                $ contFesta += 1

            "Não conseguir aguentar a pressão e prejudicar os que estão ao meu redor. Isso sim é o fim. Prefiro distância do que essa chance. ":
                $ contCalma += 1

        # ================================== #

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Com a possibilidade de poderes assim, acho que a primeira coisa que faria seria ir para o mais longe daqui possível. Menos chance de problemas, menos incômodo para todo mundo."
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Como se incômodo não tivesse em todo lugar hehe Se fosse por isso seria melhor ir para onde não tem pessoa nenhuma"
        hide panetone

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Ah é?…"
        hide pao_de_viagem

        show panetone at panetone_meio
        panetone "Por isso eu ficaria bem onde estivesse. Os incômodos seriam interceptados por meus fiéis clones. Ai eu poderia apenas aproveitar onde estivesse com toda paz do mundo e com as melhores companhias"
        hide panetone

        show cookie at cookie_meio
        cookie "Até que soa bem, boa idéia queridinho. Para que achar problemas por aí, quando posso alcançar tudo ao meu redor? Imagina só hihi. Sem mexer um dedinho"
        hide cookie

        show pizza at pizza_meio
        pizza "Não teria como ficar parado. COM MEUS INCRÍVEIS PODERES TODOS SERIAM DERROTADOS AONDE QUER QUE ESTIVESSE. Teria que sair para encontrar mais inimigos dignos."
        hide pizza

        # ================================== #
        #            ESCOLHA 8               #
        # ================================== #

        menu:
            "O que tem além é um mistério. Pode ser bom, pode ser ótimo… mas pode ser  o pior possível. Muito já se tem de mistério na vida, melhor ficar com a pequena garantia do conhecido.":
                $ contCasa += 1

            "Preciso ao menos tentar. Se dar por vencido é até mais perigoso do que lutar. Se não, do que tudo adiantou? Para que foi tudo que me trouxe até aqui? ":
                $ contViagem += 1
        jump perguntar

    # ================================== #

    # ================================== #
    #                P5                  #
    # ================================== #

    label p5:
        show cookie at cookie_meio
        cookie "Que tal uma linda história de época? Um romance em uma pequena cidade?"
        hide cookie

        show pizza at pizza_meio
        pizza "E o que mais? O que de interessante acontece?"
        hide pizza

        show cookie at cookie_meio
        cookie "Como assim de interessante, queridinho? Essa é a história. E já é muito interessante, eu já te digo!"
        hide cookie

        show panetone at panetone_meio
        panetone "Um romance até pode ser interessante, mas se for um romance tem que pelo menos uma tensão! Tem que ter um drama! Se não, qual a graça? Quero alguma movimentação!"
        hide panetone

        pizza "Movimentação? VOCÊ QUER MOVIMENTAÇÃO? ENTÃO QUE TAL AÇÃO?!? Explosões, lutas, intrigas e um herói que acaba com todos pela frente!"

        show cookie at cookie_meio
        cookie "Nossa nossa, quanta coisa. Não tem um minuto de silêncio nisso aí?"
        hide cookie

        show pizza at pizza_meio
        pizza "NÃÃÃÃÃOOOOOOO!!!!!"
        hide pizza

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Então deveria… Qual o sentido de só ter rúido? Isso apenas o deixa amortecido. O que mais real do que o suspense, o incerto… até me faz sentir algo novamente"
        hide pao_de_viagem

        # ================================== #
        #            ESCOLHA 9               #
        # ================================== #

        menu:
            "Algo mais movimentado, com certeza. Se não, vou pegar no sono na minha própria história.":
                $ contFesta += 1
            "A vida já é movimentada o suficiente, gostaria de tirar o pé do acelerador. Uma história mais lento com certeza me faria melhor":
                $ contCalma += 1

        # ================================== #

        show cookie at cookie_meio
        cookie "Ahhhh, uma linda casa que marca a memória de quem vê. As redes de fofocas, encontros e desencontros do amor! Como seria bom viver algo assim!"
        hide cookie

        show pao_de_viagem at pao_de_viagem_meio
        pao_de_viagem "Mas… mas… isso só me deixaria mais tenso! Como garantir que não daria tudo errado? Que ambos acabariam com coração partido e com uma casa cheia de memórias ruins? Prefiro que nunca se espere nada de bom e que pelo menos o local onde o mal aconteça pode ser deixado para trás"
        hide pao_de_viagem

        show pizza at pizza_meio
        pizza "É claro que uma casa só não serve. PRECISAMOS MUITAS! PARA PODERMOS DESTRUÍ-LAS! E DEPOIS ACHAR MAIS E MAIS CASAS PARA DESTRUIR!"
        hide pizza

        show panetone at panetone_meio
        panetone "Se você andar tanto, irá perder todas as intrigas de uma família! Elas nem sempre aparecem de primeira. As melhores só surgem depois de que as tensões marinam muito tempo hehehe "
        hide panetone

        # ================================== #
        #            ESCOLHA 10              #
        # ================================== #

        menu:
            "Não podemos deixar para trás o que construímos na narrativa, o local é tão importante quanto os personagens. Se aqui chegamos aqui fico até o fim.":
                $ contCasa += 1
            "Temos tantos locais para explorar e tanto o que move na história, não se pode limitar a apenas um. Um é apenas uma parte de um todo. ":
                $ contViagem += 1
        jump perguntar
            
    # ================================== #

    # ================================== #
    #         DIRECIONA FINAL            #
    # ================================== #

    label decidirFinal:
        $ Final_Pizza = ["cena_1", "cena_2"]    # Festa & Viagem 
        $ Final_Panetone = ["cena_1", "cena_2"] # Festa e Casa
        $ Final_Cookie = ["cena_1", "cena_2"]   # Casa e Calma
        $ Final_Bolor =  ["cena_1", "cena_2"]   # Casa e Viagem

        if contFesta > contCalma and contViagem > contCasa:
            jump Final_Pizza
        elif contFesta > contCalma and contViagem < contCasa:
            jump Final_Panetone
        elif contFesta < contCalma and contViagem < contCasa:
            jump Final_Cookie
        elif contFesta < contCalma and contViagem > contCasa:
            jump Final_Bolor
        else:
            jump Final_Pizza

    # ================================= #
    #            FINAL PIZZA            #
    # ================================= #
        
    label Final_Pizza:
            window hide
            show fpizza
            pause
    return

    # ================================= #
    #          FINAL PANETONE           #
    # ================================= #
        
    label Final_Panetone:
            window hide
            show fpanetone at center
            pause
    return

    # ================================== #
    #           FINAL COOKIE             #
    # ================================== #
        
    label Final_Cookie:
            window hide
            show fbiscoito
            pause
    return 

    # ================================== #
    #             FINAL BOLOR            #
    # ================================== #

    label Final_Bolor:
            window hide
            show fbolor
            pause
    return 

# SO PRA LEMBRAR A SINTAXE !!!

#    if testeVariavel == 0:
#        cookie "LALALA"
#        $ testeLista.append("A")
#        cookie "[testeLista[0]]"
#    else :
#        narrador "XALALA"
#    
#    menu:
#        "FINAL A":
#            $ testeLista.append("A")
#        "FINAL B":
#            $ testeLista.append("B")
#
#    cookie "[testeLista[1]]"





    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#    show eileen happy at right
#    # These display lines of dialogue.
#
#
#    pao "eu sou um pão e voce?"
#    bolo "eu sou um bolo"
#    pao "POR QUE VOCE NAO VAI SE FUDER SEU VIADO DE MERDA EU TO FALANDO SERIO SEU BOSTA VAI TOMAR NO SEU CU"
#    show bolo sad at left 
#    bolo "ok :c"
#    narrador "voce ganhou um confete"
#    $ testeVariavel += 1
#    bolo "oiii agora eu tenho [testeVariavel] confetes"
#
#
#    menu:
#        "MATAR O BOLO?":
#            jump testePANETONE
#
#        "MATAR O PAO?":
#            hide eileen happy
#            bolo "NAAAAAAAAAAAAAAAAAAAAAAAAAAAO PAAAAAAAAAAAAAO"
#            show bolo sad at center
#            bolo "eu vou me matar"
#            hide bolo sad
#
#
#    transform midleft:
#        xalign 0.33 yalign 1.
#    # This ends the game.
#    label testePANETONE:
#        scene bg room
#        show panetone happy at midleft
#        bolo "oi"
#    return
#