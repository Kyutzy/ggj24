define cookie = Character("Cookie")
define panetone = Character("Panetone")
define massa = Character("Massa")
define pizza = Character("Pizza")
define pao_de_viagem = Character("Pão de Viagem")

define narrador = Character('Narrador')


label start:
    $ testeVariavel = 0
    $ testeLista = []

    # ================================== #
    #               CENA 1               #
    # ================================== #
    #scene bg room
    
    show cookie in_love at right


    if testeVariavel == 0:
        cookie "LALALA"
        $ testeLista.append("A")
        cookie "[testeLista[0]]"
    else :
        narrador "XALALA"
    
    menu:
        "FINAL A":
            $ testeLista.append("A")
        "FINAL B":
            $ testeLista.append("B")

    cookie "[testeLista[1]]"
    # ================================== #
    #               CENA 2               #
    # ================================== #


    # ================================== #
    #               CENA 3               #
    # ================================== #


    # ================================== #
    #               CENA 4               #
    # ================================== #




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