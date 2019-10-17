import ply.lex as lex

class MyLexer(object):
    # List of token names.   This is always required

    reserved = {
    'snd' : 'SND',
    'set' : 'SET',
    'add' : 'ADD',
    'mul' : 'MUL',
    'mod' : 'MOD',
    'rcv' : 'RCV',
    'jgz' : 'JGZ',
    }

    tokens = [
        'NUMBER',
        'LETTER',
     ] + list(reserved.values())
 
    # Regular expression rules for simple tokens
    #t_SND    = r'snd'
    #t_LETTER = r'[a-z_]'


    def t_LETTER(self,t): #TODO: check for one letter id
        r'[a-zA-Z_]+'
        #r'[a-z_]' 
        if t.value in self.reserved:
            t.type = self.reserved[ t.value ]
        #t.type = reserved.get(t.value,'LETTER')    # Check for reserved words
        return t
    
 
    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self,t):
        r'-?\d+'
        t.value = int(t.value)    
        return t
 
    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
 
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'
 
    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
 
    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
     
    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)


    #EOF handling rule
    #def t_eof(t):
    # Get more input (Example)
     #   more = input('... ')
      #  if more:
       #     self.lexer.input(more)
        #    return self.lexer.token()
        #return None
 
# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
m.test("snd -12")     # Test it