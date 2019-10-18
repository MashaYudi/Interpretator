import myParser
import myLexer
import inner_state
def main():
    # Initialise inner state
    inner_state.initialize()

    #build lexer
    lexer = myLexer.make_lexer()

    #build parser
    parser = myParser.make_parser()
    

    while True:     #parsing cycle
        try:
            file_name = input('file > ')
        except EOFError:
             break
        if not file_name:
            continue

        try:
            with open(file_name) as f:
                lines = f.readlines()
        
            while inner_state.command_counter != len(lines):        #line by line parsing
                print((lines[inner_state.command_counter])[:-1])
                parser.parse(lines[inner_state.command_counter])
                #print(myParser.mem.regs)
                inner_state.command_counter += 1

        except IOError:
            print (f"Could not read file: {file_name}")
            continue

if __name__ == "__main__":
    main()
