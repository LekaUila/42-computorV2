# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/19 16:39:00 by lflandri          #+#    #+#              #
#    Updated: 2024/09/20 15:56:37 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from class_d.operation import  operation
from equationResolver import  equationResolve



def __main__() -> int:
    sys.setrecursionlimit(2000)
    programmRunning = True
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
            elif command == "save":
                #TODO create save command
                print("save commande")
            elif command == "equa":
                #TODO to replacement before 
                equationResolve(entry[4:])
            else :
                #TODO normal calculation
                print(entry)  
    except BaseException as exeption :
        # lol = 1/0
        print(f"Error : {exeption.args[0]} ")
        return 1
    return 0

if __name__ == '__main__':
    exit( __main__())