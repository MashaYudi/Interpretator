import ply.yacc as yacc
def main():
    # Build the parser
    parser = yacc.yacc()

command_counter = 0
while True:
    file_name = input('file > ')
    with open(file_name) as f:
        lines = f.readlines()

    while command_counter != len(lines):
        print(f"comm_count {command_counter}")
        print(lines[command_counter])
        parser.parse(lines[command_counter])
        command_counter += 1

    print(lines)
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)

if __name__ == "__main__":
    main()
