# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define pao = Character("PAO")
define bolo = Character('bolo')
define narrador = Character('narrador')

# The game starts here.

label start:
    $ testeVariavel = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at right

    # These display lines of dialogue.

    pao "eu sou um pão e voce?"
    bolo "eu sou um bolo"
    pao "POR QUE VOCE NAO VAI SE FUDER SEU VIADO DE MERDA EU TO FALANDO SERIO SEU BOSTA VAI TOMAR NO SEU CU"
    show bolo sad at left 
    bolo "ok :c"
    narrador "voce ganhou um confete"
    $ testeVariavel += 1
    bolo "oiii agora eu tenho [testeVariavel] confetes"


    menu:
        "MATAR O BOLO?":
            hide bolo sad
            narrador "voce matou o bolo"
            pao "FINALMENTE ELE MORREU EU ODIAVA AQUELE CARA"
        "MATAR O PAO?":
            hide eileen happy
            bolo "NAAAAAAAAAAAAAAAAAAAAAAAAAAAO PAAAAAAAAAAAAAO"
            show bolo sad at center
            bolo "eu vou me matar"
            hide bolo sad
    narrador "e assim acaba a nossa historia, todo mundo morreu, agora vai fazer algo útil com a sua vida"

    # This ends the game.

    return
