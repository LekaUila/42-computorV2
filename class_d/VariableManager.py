# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    VariableManager.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/26 15:41:30 by lflandri          #+#    #+#              #
#    Updated: 2024/09/27 15:17:50 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.operation import operation, Complex

class VariableManager :
    
    def __init__(this) -> None:
        this.data = {"i":Complex(imaginary=1)}

    def addModifyVariable(this, name, value, parameter=None):
        if name == "i":
            raise ArithmeticError("\"i\" can't be modified")
        elif name == "X":
            raise BaseException("\"X\" can't be used as variable.")
        elif parameter == None :
            this.data[name] = operation(value)
        else :
            this.data[name] = [operation(value), parameter]
    
    def getVariable(this, name):
        if this.data.__contains__(name):
            if type(this.data[name]) == list:
                return [this.data[name][0].copy(), this.data[name][1]]
            return this.data[name].copy()
        return Complex(reel=0)
    
    def __str__(this) -> str:
        s = ""
        for item in this.data.items() :
            if item[0] != "i":
                if type(item[1]) == list :
                    parameter = ""
                    for i in item[1][1]:
                        parameter += i + ", "
                    s += f"{item[0]}({parameter[:-2]}) = {item[1][0]} \n"
                else :
                    s += f"{item[0]} = {item[1]} \n"
        if s == "":
            return "No data to print.\n"
        return s
  
    