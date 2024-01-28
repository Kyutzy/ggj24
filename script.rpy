define cookie = Character("Cookie")
define panetone = Character("Panetone")
define massa = Character("Massa")
define pizza = Character("Pizza")
define pao_de_viagem = Character("Pão de Viagem")

define todos = Character("Todos")
define narrador = Character("Narrador")


label start:
    $ testeVariavel = 0
    $ testeLista = []

    # ================================== #
    #            INICIO                  #
    # ================================== #
    scene entrada_forno
    
    narrador "O barulho de massa atingiu uma superfície dura. Lentamente, o mundo parece se mover em uma direção. Ao fundo, um barulho do crepitar das chamas pode ser ouvido. Está tudo muito escuro."

    show pao_de_viagem scared at left
    pao_de_viagem "Essa não… morremos…"
    hide pao_de_viagem scared
    
    show pizza scared at left
    pizza "NÃÃÃÃÃÃOOOOOO, eu sou lindo demais para morrer"
    hide pizza scared

    show panetone happy at left
    panetone "Não sei o que está acontecendo mas sei que isso com certeza nos amassou :D"
    hide panetone happy

    narrador "A MASSA se levanta da superfície gelada, ainda um pouco confusa pela queda"

    show massa impressed at left
    massa "A gente não morreu, pessoal. A gente chegou na ESTEIRA"
    hide massa

    todos "Ahhhhhhhhhhhh…"

    narrador "As luzes se acendem. A MASSA se vê dentro de um espaço amplo, cercado de paredes de metal. O fogo está à espreita, aquecendo o ambiente cada vez mais."

    show pizza happy at left
    pizza "Então é aqui que vou pegar um ótimo dourado! Mal posso esperar"1

    show pao_de_viagem sad at right
    pao_de_viagem "Não é assim que funciona… aqui é nosso fim. Não tem mais para onde ir"
    
    hide pizza happy
    show cookie happy at left
    cookie "Não fique tristinho, pelo menos ainda somos um"

    show massa indifferent at right
    massa "É verdade, vocês ainda são parte de mim, saco"
    cookie "hihihihihi"
    hide cookie happy
    hide massa indifferent

    show pizza confident at center
    pizza "Vocês acham que parte dele conseguiria fazer isso?"
    hide pizza confident


    narrador "MASSA ouve sons que soam como grunhidos de esforço de alguém fazendo várias poses de musculação."
    show massa sombrancelha_levantada_kk at center
    hide massa sombrancelha_levantada_kk

    show pao_de_viagem sad at left
    pao_de_viagem "Estamos prestes a deixar de existir e é isso é isso que escolhe fazer?"

    show pizza confident at right
    pizza "Pelo menos eu não fico choramingando por um calorzinho"

    hide pao_de_viagem sad
    hide pizza confident

    show massa angry at center 
    massa "Ei, sem brigas por aqui"
    hide massa angry
    show massa indifferent at center 

    show panetone laughing at right
    panetone "É isso aí! Se não vou sovar vocês!"

    show 
    pizza "Se for sovar eu quero ajudar!"

    narrador "(Silêncio)"

    massa "É difícil aceitar que você é parte de mim…"    

    hide panetone laughing

    narrador "Olhando ao redor, A MASSA percebe que está sozinha, e não tem muito como escapar. As paredes de sua plataforma de metal que lentamente avança no caminho são altas demais para que consiga escalar."

    massa "A jornada parece ser longa… e agora? Só eu por um tempo?"

    massa "O que será que está por vir"

    show cookie happy at left
    cookie "Ah, talvez nós iremos para uma linda fazenda onde vão todas as massas que caíram no chão. E podemos andar pelos campos e nadar nas lagoas"

    massa "Isso não soa nada ruim, na verdade."

    show pao_de_viagem sad at right
    pao_de_viagem "Sempre achei que seria como andar em um fundo de um lago sem nenhuma luz… Sem fim… até que não sinta mais nem o passar do tempo"

    hide pao_de_viagem sad
    hide cookie happy

    show panetone laughing
    panetone "Meio sombrio não? Sabe qual a grande diferença entre o lago e a padaria afinal? É que na padaria assa pão, no lagoa há sapinho"
    hide massa indifferent
    show massa sombrancelha_levantada_kk at center
    hide massa sombrancelha_levantada_kk
    show massa indifferent at center

    pao_de_viagem "Vão assar a gente?"

    massa "Sim… mas talvez não seja tão ruim, chegou minha hora de crescer"

    panetone "Ok… Sendo assim, prefiro pensar em algo mais feliz. Que tal um grande espetáculo? Com música, dança, e tudo que quiser? Merecemos algo assim depois disso aqui não é mesmo?"

    hide massa indifferent
    hide panetone laughing
    
    show pizza confident at right
    pizza "Não, porque nunca vou morrer! AH É! 37 jogos sem nenhuma derrota! segura o pai."
    
    show massa    
    massa "Do que você está falando? De que jogos?"

    pizza "É isso aí pô, Só vitória atrás de vitória, segue o líder. Saindo dessa quem topa uma cerva? To louco pra festar ao som de mc bread! Mostrar como se faz nas quebrada família"

    # ================================== #
    #            ESCOLHA 1               #
    # ================================== #

    menu:
        "Acho que prefiro mesmo descansar, ainda mais depois de ter que escutar vocês por tanto tempo. ":
            #CALMA 

        "Realmente, pizza bora curtir e deixar rolar.":
            #FESTA

    # ================================== #


    cookie "Pena que ninguém nunca voltou para falar o que tinha lá do outro lado, se eu conseguir eu corro atrás de vocês"


    pao_de_viagem "Não deve ter coisa boa lá, deve ser ruim…"


    cookie "Ou talvez eles gostem tanto de lá que não querem mais sair"


    pizza "Talvez não tivesse um forte igual eu pra conseguir voltar, segue o líder tropa *Grunhidos de poses*"


    cookie "Deve mesmo ser um trabalhão para fazer essa viagem né? Acho que euzinha ia preferir ficar por onde estivesse mesmo."


    panetone "Pelo menos se pararmos lá daria para… descansar… hã, hã? Tipo massa?"


    # ================================== #
    #            ESCOLHA 2               #
    # ================================== #

    menu:
        "Acho que depois de me acostumar com o outro lado não teria porque voltar.":
            #CASA

        "Se fosse possível eu iria e voltaria como se tivesse fazendo um passeio no parque ":
            #VIAGEM

    # ================================== #


    pizza "Conquistaria todos os reinos que não se curvarem em frente à minha força"
    
    massa "Isso foi um pouco rápido demais"

    pizza "Assim como será minha campanha. vou controlar o mundo todo, VAPO Irei dominar o mundo inteiro. MUAHAHA"

    cookie "Para que isso, meu bom. Que tal fazer um grande jardim para o reino, onde todos possam cultivar trigo para ter sua própria farinha. Hmmmm, que delicinha :)"

    pao_de_viagem "Ah, se for pra trabalhar eu não quero não, ninguém me avisou que precisaria de tanto trabalho manual"

    pizza "Vou pegar todos os trigos dos meus plebeus e fazer farinha pra crescer meus bíceps massudos"

    pao_de_viagem "Nãoooooo… mas e se quiserem fazer isso com a gente"

    panetone "Prefiro que venham até meu reino, muito mais fácil. Me agradem com seus ovos."

    massa "E porque eles fariam isso?"

    panetone "Ah, porque… porque… eu mandei(?). Talvez eu não fosse o melhor rei, mas com certeza seria o mais satisfeito .( ͡° ͜ʖ ͡°)"

    # ================================== #
    #            ESCOLHA 3               #
    # ================================== #
    
    menu:
        "Sendo rei, poderia conhecer todos e cada uma de suas histórias, desde que eram apenas massas como eu. ":
            #VIAGEM

        "Se eu fosse rei, não me preocuparia em sair por aí, por que conhecer outros lugares se tenho tudo o que preciso por aqui.":
            #CASA

    # ================================== #



    pizza "Como eu chegaria a ser rei? numa competição de levantamento de massa, óbvio!"

    pao_de_viagem "O que isso tem a ver com qualquer coisa?"

    pizza "(Cantando, sem ouvir) - EU SERIA O REI! CONQUISTADOR DOS INIMIGOS! COM GRANDES BÍCEPS!"

    panetone "Ah… Ok… (Cantando) ELE É O REI!!!"

    # ================================== #
    #            ESCOLHA 4               #
    # ================================== #

    menu:
        "Ovos e especiarias… acho que como rei mereceria alguns luxos."
            #FESTA

        "A primeira coisa que faria como rei seria distribuir uma chapa para cada pão, todos merecem uma tarde tranquila com manteiga e amendoim."
            #CALMA

    # ================================== #

    cookie "Talvez o melhor, meu bem, seja apenas não ser rei…?"

    pao_de_viagem "Acho que… acho que teletransporte. Eu poderia fugir de qualquer situação desagradável imediatamente. Uma vida sem pães amanhecidos(SUSPIRO)"

    pizza "Isso é positivo para você? SUPER FORÇA, SUPER VELOCIDADE, SUPER RESISTÊNCIA. Posso lutar e sovar qualquer panificado."

    pao_de_viagem "Eu murcho só de pensar nisso."

    cookie "Concordo. Muita bagunça! Por isso já sei que iria mover as coisas com a mente! Poderia trazer meus caros leite e bolo  para perto e levar os indesejados confetes para longe sem fazer força. "

    massa "Até você?"

    cookie "Nunca disse que discordava do conflito, só discordo do método!"

    panetone "Para que se ocupar com brigas quando se tem o melhor poder logo a sua frente? Fazer cópias de mim mesmo! Poderia lotar qualquer lugar só comigo! Seria uma verdadeira “multipão”"

    # ================================== #
    #            ESCOLHA 5               #
    # ================================== #

    menu:
        "Prefiro tirar o meu da reta, algo que me colocasse fora do perigo e amaciasse os ânimos seria muito melhor com certeza."
            #CALMA
        "Do que adianta um poder se não posso aproveitar bem? Quero estar na ação, com a mão na massa… AHHH, FOI SEM QUERER"
            #FESTA

    # ================================== #



    pao_de_viagem "Com a possibilidade de poderes assim, acho que a primeira coisa que faria seria ir para o mais longe daqui possível. Menos chance de problemas, menos incômodo para todo mundo."

    panetone "Como se incômodo não tivesse em todo lugar hehe Se fosse por isso seria melhor ir para onde não tem pessoa nenhuma"

    pao_de_viagem "Ah é?…"

    panetone "Por isso eu ficaria bem onde estivesse. Os incômodos seriam interceptados por meus fiéis clones. Ai eu poderia apenas aproveitar onde estivesse com toda paz do mundo e com as melhores companhias"

    cookie "Até que soa bem, boa idéia queridinho. Para que achar problemas por aí, quando posso alcançar tudo ao meu redor? Imagina só hihi. Sem mexer um dedinho"

    pizza "Não teria como ficar parado. COM MEUS INCRÍVEIS PODERES TODOS SERIAM DERROTADOS AONDE QUER QUE ESTIVESSE. Teria que sair para encontrar mais inimigos dignos."

    # ================================== #
    #            ESCOLHA 6               #
    # ================================== #

        menu:
            "Fugir dos problemas raramente funciona, ainda mais em um mundo com super problemas. Prefiro ficar onde estou e usar meus poderes."
                #CASA

            "Viajar em super velocidade parece exatamente o que precisaria para resolver os problemas de longas distâncias. Acho que o problema ia ser a falta do que fazer depois de um tempo." 
                #VIAGEM

    # ================================== #


    panetone "Sempre se acha que não se teme nada até ficar de frente a isso, certo? hehe. De repente estar nesse caminho me fez sentir tanta falta das vozes, dos barulhos das pessoas. O silêncio é tão alto…"

    pizza "É difícil não ter uma platéia. É difícil saber que ninguém está ali para te ver, por mais INCRÍVEL que seja o que estiver fazendo. Me faz sentir tão pequeno."

    cookie "Ah benzinho, é nisso que acho conforto. Não consigo nem pensar em quando é demais. Até me desregula aqui. Tanta coisa, tanto peso. Não faz bem não."

    pizza "SIM, ISSO MESMO. PESO! É disso que preciso! Quanto mais melhor. Não quero ficar sem peso. Ai como sei que estou ali?"

    pao_de_viagem "Mas com mais e mais parece que se precisa fazer mais e mais. E se não conseguir? E se eu desapontar? Como vou aguentar isso… não vou…"

    panetone "Ei ei, não precisa… se acalme. Você sabe que estamos entre… amidos…"

    pao_de_viagem "hehe, ok, acho que consigo me acalmar"

    # ================================== #
    #            ESCOLHA 7               #
    # ================================== #

    menu:
        "Ficar sozinho, sem ninguém. O silêncio, o escuro. Acho que estou vivendo meu maior medo agora mesmo."
            #FESTA

        "Não conseguir aguentar a pressão e prejudicar os que estão ao meu redor. Isso sim é o fim. Prefiro distância do que essa chance. "
            #CALMA

    # ================================== #



    pao_de_viagem "Com a possibilidade de poderes assim, acho que a primeira coisa que faria seria ir para o mais longe daqui possível. Menos chance de problemas, menos incômodo para todo mundo."

    panetone "Como se incômodo não tivesse em todo lugar hehe Se fosse por isso seria melhor ir para onde não tem pessoa nenhuma"

    pao_de_viagem "Ah é?…"

    panetone "Por isso eu ficaria bem onde estivesse. Os incômodos seriam interceptados por meus fiéis clones. Ai eu poderia apenas aproveitar onde estivesse com toda paz do mundo e com as melhores companhias"

    cookie "Até que soa bem, boa idéia queridinho. Para que achar problemas por aí, quando posso alcançar tudo ao meu redor? Imagina só hihi. Sem mexer um dedinho"

    pizza "Não teria como ficar parado. COM MEUS INCRÍVEIS PODERES TODOS SERIAM DERROTADOS AONDE QUER QUE ESTIVESSE. Teria que sair para encontrar mais inimigos dignos."

    # ================================== #
    #            ESCOLHA 8               #
    # ================================== #

    menu:
        "O que tem além é um mistério. Pode ser bom, pode ser ótimo… mas pode ser  o pior possível. Muito já se tem de mistério na vida, melhor ficar com a pequena garantia do conhecido."
            #CASA

        "Preciso ao menos tentar. Se dar por vencido é até mais perigoso do que lutar. Se não, do que tudo adiantou? Para que foi tudo que me trouxe até aqui? "
            #VIAGEM

    # ================================== #


    cookie "Que tal uma linda história de época? Um romance em uma pequena cidade?"

    pizza "E o que mais? O que de interessante acontece?"

    cookie "Como assim de interessante, queridinho? Essa é a história. E já é muito interessante, eu já te digo!"

    panetone "Um romance até pode ser interessante, mas se for um romance tem que pelo menos uma tensão! Tem que ter um drama! Se não, qual a graça? Quero alguma movimentação!"

    pizza "Movimentação? VOCÊ QUER MOVIMENTAÇÃO? ENTÃO QUE TAL AÇÃO?!? Explosões, lutas, intrigas e um herói que acaba com todos pela frente!"

    cookie "Nossa nossa, quanta coisa. Não tem um minuto de silêncio nisso aí?"

    pizza "NÃÃÃÃÃOOOOOOO!!!!!"

    pao_de_viagem "Então deveria… Qual o sentido de só ter rúido? Isso apenas o deixa amortecido. O que mais real do que o suspense, o incerto… até me faz sentir algo novamente"

    # ================================== #
    #            ESCOLHA 9               #
    # ================================== #

    menu:
        "Algo mais movimentado, com certeza. Se não, vou pegar no sono na minha própria história."
            #FESTA
        "A vida já é movimentada o suficiente, gostaria de tirar o pé do acelerador. Uma história mais lento com certeza me faria melhor"
            #CALMA

    # ================================== #

    cookie "Ahhhh, uma linda casa que marca a memória de quem vê. As redes de fofocas, encontros e desencontros do amor! Como seria bom viver algo assim!"

    pao_de_viagem "Mas… mas… isso só me deixaria mais tenso! Como garantir que não daria tudo errado? Que ambos acabariam com coração partido e com uma casa cheia de memórias ruins? Prefiro que nunca se espere nada de bom e que pelo menos o local onde o mal aconteça pode ser deixado para trás"

    pizza "É claro que uma casa só não serve. PRECISAMOS MUITAS! PARA PODERMOS DESTRUÍ-LAS! E DEPOIS ACHAR MAIS E MAIS CASAS PARA DESTRUIR!"

    panetone "Se você andar tanto, irá perder todas as intrigas de uma família! Elas nem sempre aparecem de primeira. As melhores só surgem depois de que as tensões marinam muito tempo hehehe "

    # ================================== #
    #            ESCOLHA 10              #
    # ================================== #

    menu:
        "Não podemos deixar para trás o que construímos na narrativa, o local é tão importante quanto os personagens. Se aqui chegamos aqui fico até o fim."
            # CONTA PONTO PRA QUAL FINAL?
        "Temos tantos locais para explorar e tanto o que move na história, não se pode limitar a apenas um. Um é apenas uma parte de um todo. "
            # CONTA PONTO PRA QUAL FINAL?
            
    # ================================== #






    # ================================== #
    # ================================== #
    #              FINAIS                #
    # ================================== #
    # ================================== #



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
#
#    # These display lines of dialogue.
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