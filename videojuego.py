import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 144,fps=60, title="flecha en la cabeza")
        # pyxel.mouse(True)
        pyxel.images[0].load(0, 0, "bg1.png")
        pyxel.images[1].load(0, 0, "arr.png")
        pyxel.images[2].load(0, 0, "char.png")
        self.death = False
        self.x = 220
        self.dx = 0.06
        self.win = False
        self.question = [
            "Escribe texto y presiona ENTER.:",
            "?Cuentas personas hablan el zapoteco actualmente ?",
            "?En que paises se habla el zapoteco ?",
            "?Como se dice 'hola' en Quechua?",
            "",
            "",
            ""
        ]
        self.aide = [
            "",
            "1; 3    2; -5    3; 800000    4; 1000",
            "1; france    2; mexico    3; china    4; argentina",
            "1; rimaykullayki     2; hola    3; bonjour    4; hello",
            "",
            ""
            "",
        ]
        self.answers = [
            "",
            "800000",
            "mexico",
            "rimaykullayki",
            "",
            "u"
        ]
        self.in_game = None
        self.is_alive = 1
        self.input_text = ""  # Texte saisi par l'utilisateur
        self.is_typing = True  # Si la saisie est active
        self.lvl = 0
        self.start = True
        pyxel.run(self.update, self.draw)


    def update(self):
        if self.lvl > 0:
            self.x -= self.dx
        if -100 <= self.x <= 8:
            self.dx = 0
            self.is_alive = 0
        if self.is_typing and not(self.start):
            for key in range(pyxel.KEY_A, pyxel.KEY_Z + 1):
                if pyxel.btnp(key):
                    # Ajouter la lettre correspondante à la chaîne
                    self.input_text += chr(key)
            for key in range(pyxel.KEY_0, pyxel.KEY_9 + 1):
                if pyxel.btnp(key):
                    self.input_text += chr(key)
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                # Supprimer le dernier caractère
                self.input_text = self.input_text[:-1]
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.input_text += " "
            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.lvl >= 1:
                    App.verify(self)
                self.lvl += 1
                if self.death:
                    self.lvl = 5
                    self.dx = 3
                if self.lvl == 4:
                    self.win = True
                self.input_text = ''
    def verify(self):
        if not(self.input_text == self.answers[self.lvl] or self.input_text == 'u'):
            self.death = True
        else:
            self.dx *= 2

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 1600, 900)
        pyxel.rect(pyxel.width//2 - 140//2, 20, 140, 10, 1)  # Zone de saisie
        pyxel.blt(2,110,2,0+12*(pyxel.frame_count%80//20)*self.is_alive,0,12,25,10)
        pyxel.blt(240,109,2,9,25,12,25,10)
        if self.dx == 0:
            pyxel.rect(5,115,5,20,8)
        pyxel.blt(self.x,115,1,0,0,22,3,8)
        if self.start:
            pyxel.text(pyxel.width // 2 - 140 // 2, 10, "Presiona espacio (PRESS SPACE)", 7)
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.start = False
                self.in_game = True
        elif self.in_game:
            pyxel.text(pyxel.width//2 - 190//2, 10, self.question[self.lvl], 7)
            pyxel.text(pyxel.width//2 - 90, 35, self.aide[self.lvl], 7)
            pyxel.text(pyxel.width//2 - 140//2 + 2, 22, self.input_text, 7)
        if self.win:
            self.x = -500
            pyxel.text(pyxel.width//2 - 140//2 + 2, 22, "!Bravo, han ganado!", 7)
        if self.death:
            pyxel.text(pyxel.width//2 - 140//2 + 2, 22, "Que pena, han perdido.", 7)



App()
