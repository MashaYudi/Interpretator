import os
from myLexer import myLexer
import ply.yacc as yacc
import inner_state

tokens = myLexer.tokens
mem = inner_state.memory()


def p_SND(p):
    'line : SND evalue'
    global last_sound
    last_sound = p[2]
    print(f"sound of frequency {p[2]} played")


def p_SET(p):
    'line : SET reg evalue'
    mem.regs[p[2]] = p[3]


def p_JGZ(p):
    'line : JGZ evalue evalue'
    global command_counter
    if (p[2] > 0):
        inner_state.command_counter += p[3]
        inner_state.command_counter -= 1
        # print(f"p comm_count {inner_state.command_counter}")


def p_ADD(p):
    'line : ADD reg evalue'
    mem.check(p[2])
    mem.regs[p[2]] += p[3]


def p_RCV(p):
    'line : RCV evalue'
    if (p[2] != 0):
        print(f"frequency of last played sound: {last_sound}")


def p_MUL(p):
    'line : MUL reg evalue'
    mem.check(p[2])
    mem.regs[p[2]] *= p[3]


def p_MOD(p):
    'line : MOD reg evalue'
    mem.check(p[2])
    mem.regs[p[2]] = mem.regs[p[2]] % p[3]


def p_reg_let(p):
    'reg : LETTER'
    p[0] = p[1]


def p_eval_reg(p):
    'evalue : reg'
    mem.check(p[1])
    p[0] = mem.regs[p[1]]


def p_eval_num(p):
    'evalue : NUMBER'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    input()
    # os.system('pause')


def make_parser():
    parser = yacc.yacc()
    return parser
