class Token:
    




    TT_INT = "INT"
    TT_PLUS = "PLUS"
    TT_MINUS = "MINUS"
    TT_FLOAT = "FLOAT"
    TT_MUL = "MUL"
    TT_DIV = "DIV"
    TT_LPAREN = "LPAREN"
    TT_RPAREN = "RPAREN"





    def token(self, type_, value):
        self.type_ = self.type_
        self.value = self.value 
    def __repr__(self):
        if self.value: 
            return f'{self.type}:{self.value}'
        return  f'self.type'
    



class lexershi:
    def __init__(self, text):
        self.text = text
        self.currentpos = -1
        self.currentchar = None 
    def advancepos(self):
        currentpos+=1
        if self.pos<len(self.text):
            self.currentchar = self.text[currentpos]
        else:
            None 
    def newtoken(self):
        tokens =[]
        while self.currentchar != None: 
            if self.currentchar in " \t":
                self.advance()
            elif self.currentchar == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.currentchar == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.currentchar == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.currentchar == "/":
                tokens.append(Token(TT_DIV))
                self.advance()

        return tokens 