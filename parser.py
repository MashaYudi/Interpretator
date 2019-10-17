
from main import command_counter
# Get the token map from the lexer.  This is required.
from MyLexer import MyLexer
tokens = MyLexer.tokens

regs = {'a': 0, 'b': 0}
last_sound = 0



def p_SND(p):
    'line : SND evalue'
    global last_sound
    last_sound = p[2]
    print(f"sound played: {p[2]}")


def p_SET(p):
    'line : SET reg evalue'
    regs[p[2]] = p[3]


def p_JGZ(p):
    'line : JGZ evalue evalue'
    global command_counter
    if (p[2] > 0):
        command_counter += p[3]
        command_counter -= 1
        print(command_counter)


def p_ADD(p):
    'line : ADD reg evalue'
    regs[p[2]] += p[3]


def p_RCV(p):
    'line : RCV evalue'
    if (p[2] > 0):
        print(f"last sound played: {last_sound}")


def p_MUL(p):
    'line : MUL reg evalue'
    regs[p[2]] *= p[3]


def p_MOD(p):
    'line : MOD reg evalue'
    regs[p[2]] = regs[p[2]] % p[3]


def p_reg_let(p):
    'reg : LETTER'
    p[0] = p[1]


def p_eval_reg(p):
    'evalue : reg'
    p[0] = regs[p[1]]


def p_eval_num(p):
    'evalue : NUMBER'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")



