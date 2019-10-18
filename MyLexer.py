import ply.lex as lex
import os


def make_lexer():
    lexer = myLexer()
    lexer.build()
    return lexer


class myLexer(object):
    # List of token names.
    reserved = {
        'snd': 'SND',
        'set': 'SET',
        'add': 'ADD',
        'mul': 'MUL',
        'mod': 'MOD',
        'rcv': 'RCV',
        'jgz': 'JGZ',
    }

    tokens = [
        'NUMBER',
        'LETTER',
    ] + list(reserved.values())

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'-?\d+'
        t.value = int(t.value)
        return t

    def t_LETTER(self, t):                       # TODO: check for one letter id
        r'[a-zA-Z_]+'
        if t.value in self.reserved:            # Check for reserved words
            t.type = self.reserved[t.value]
        else:
            if(len(t.value) > 1):
                self.t_error(t)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value)
        #print(t.lexer.lineno)
        t.lexer.skip(len(t.value))
        input()
        # os.system('pause')

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
