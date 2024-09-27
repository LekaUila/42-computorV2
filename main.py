# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/19 16:39:00 by lflandri          #+#    #+#              #
#    Updated: 2024/09/27 14:51:47 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from class_d.operation import  operation, acceptedType
from equationResolver import  equationResolve
from class_d.VariableManager import VariableManager

def getNameValueSaveCommand(s):
    start = 4
    while s[start] == " ":
        start += 1
    end = start
    while s[end] != " ":
        end += 1
    print (f" test {start} {end} \n")
    name = s[start: end]
    while s[end] == " ":
        end += 1
    if s[end: end + 3] != "as ":
        raise SyntaxError(f"\"{s}\" isn't a correct command.")
    value = s[end + 3:]
    return name, value

def assignation(entry, data, separation):
    func = False
    start = 0
    while entry[start] == " ":
        start += 1
    end = start
    while end < len(entry) and  entry[end] != " ":
        if entry[end] in "+-*/?=1234567890^[])":
            raise SyntaxError(f"Invalid caractere \"{entry[end]}\" for variable/function name.")
        elif entry[end] == "(":
            func = True
            end += 1
            break
        else :
            end += 1
    name = entry[start:end]
    if func : #TODO
        pass
    else :
        while end < len(entry) and  entry[end] != "=":
            if  entry[end] != " ":
                raise SyntaxError(f"Inccorect variables name {entry[:separation]}.")
            end += 1
        #TODO add convertion here
        data.addModifyVariable(name, entry[separation + 1:])
    # print (f" test {start} {end} \n")
    print(f"Assignation for {entry[separation + 1:]} :")
    print(operation(entry[separation + 1:])) 
    
def calculation(entry, data, separation):
    print(f"Calculation for {entry[:separation]} :")
    print(operation(entry[:separation]))  

def __main__() -> int:
    acceptedType.append(complex)
    acceptedType.append(operation)
    sys.setrecursionlimit(2000)
    programmRunning = True
    data = VariableManager()
    try :
        while programmRunning:
            entry = input("Tape your commande (tape help to see option) :\n")
            command = entry[0:4]
            if command == "exit":
                programmRunning = False
                print("! Quiting Programm !")
            elif command == "help":
                print("Command list :\n\n")
                print("equa :\n   Resolve a second degree polynomial equation.\n   Format : \"equa part1 = part2\"\n\n")
                print("exit :\n   Quit the programm.\n\n")
                print("help :\n   Give the command list.\n\n")
                print("save :\n   Save a functionn or a variable.\n   \"i\" and \"X\" can't be a variable name.\n   Format : \"save variableName as toSave\"\n\n")
            elif command == "data":
                print(data)
            elif command == "equa":
                #TODO to replacement before 
                equationResolve(entry[4:])
            else :
                #TODO normal calculation
                separation = entry.find("=")
                print(f"test : {entry[separation + 1: ]}")
                if separation == -1 or separation >= len(entry) - 1:
                    raise SyntaxError("Your entry cannot be interpreted.")
                elif entry[separation + 1 ].find("=") != -1:
                    raise SyntaxError("Your entry cannot be interpreted.")
                elif entry[separation + 1: ].find("?") != -1 :
                    i = separation + 1
                    check = False
                    while i < len(entry[separation + 1 ]):
                        if entry[i] != " ":
                            if (not check) and entry[i] == "?":
                                check = True
                            else :
                                raise SyntaxError("Your entry cannot be interpreted.")
                    calculation(entry, data, separation)
                else :
                    assignation(entry, data, separation)
                    
  
    except BaseException as exeption :
        lol = 1/0
        print(f"Error : {exeption.args[0]} ")
        return 1
    return 0

if __name__ == '__main__':
    exit( __main__())