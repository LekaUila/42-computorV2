# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    VariableManager.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/26 15:41:30 by lflandri          #+#    #+#              #
#    Updated: 2024/09/26 16:36:04 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.operation import operation, Complex

class VariableManager :
    
    def __init__(this) -> None:
        this.data = {"i":Complex(imaginary=1)}

    def addModifyVariable(this, name, value):
        if name == "i":
            raise ArithmeticError("\"i\" can't be modified")
        elif name == "X":
            raise BaseException("\"X\" can't be used as variable.")
        else :
            this.data[name] = operation(value)
    
    def getVariable(this, name):
        if this.data.__contains__(name):
            return this.data[name].copy()
        return Complex(reel=0)
    
    def __str__(this) -> str:
        s = ""
        for item in this.data.items() :
            if item[0] != "i":
                s += f"{item[0]} = {item[1]} \n"
        if s == "":
            return "No data to print.\n"
        return s
  
    