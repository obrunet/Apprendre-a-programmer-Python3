def read_file():
    print("read_file")


def fill_db():     
    print("fill_db")


def consult_db():
    print("consult_db")


def save_file():     
    print("save_file")


def print_menu():
    print('Choose between the folowing actions :', '\n', \
        '- (R)etrieve info from an existing db', '\n', \
        '- (F)ill in a new db','\n', \
        '- (C)onsult the default db','\n', \
        '- (S)ave to a db', '\n', \
        '- (Q)uit','\n')


def quit_menu():
    print("___ job done, exiting ___")
    return 1


if __name__ == "__main__":      
    user_choice_dict = {'R': read_file, 'F': fill_db, 'C': consult_db, 'S': save_file, 'Q': quit_menu}
    while 1:
        print_menu()
        user_answer = input("Enter your choice:")
        if (user_choice_dict.get(user_answer.upper(), print_menu)()):
            break


