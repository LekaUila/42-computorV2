# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    class_utils.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 19:00:50 by lflandri          #+#    #+#              #
#    Updated: 2024/05/07 19:41:23 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class operation:
    def __init__(this, str) -> None:
        pass
    def __eq__(this, other):
        pass
    def opti(this):
        pass   
    def checkVariableForEquation(this):
        pass    
    def destroyParenthese(this):
        pass
    def setFormat(this):
        pass
    def simplify(this):
        pass
    def selfOptiSign(this):
        pass
    def selfOptiNumberAndVariable(this):
        pass
    def selfOptiOperationAndOperation(this):
        pass 
    def selfOptiVariableAndOperation(this):
        pass    
    def selfOptiNumberAndOperation(this):
        pass
    def selfOptiNumberAndNumber(this):
        pass
    def __repr__(this):
        pass
    def __str__(this):
        pass
    def power(this, flt):
        pass

def parseValueOperation(str):
    i = 0
    result = None
    while i < len(str) and str[i] == ' ' :
        i += 1
    if i == len(str):
        raise BaseException("Inexistant Value In Operation.")
    elif str[i] in "0123456789-" :
        try :
            result = float(str)
        except :
            raise BaseException(f"{str} cannot be convert to number")
    else :
        save = i
        while i < len(str) and str[i] != ' ' :
            if str[i] not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN_":
                raise BaseException(f"'{str[i]}' cannot be a caracter for variable name.")
            i+= 1
        result = str[save : i]
        while i < len(str) and str[i] == ' ' :
            i += 1
        if i != len(str):
            raise BaseException(f"'{str}' cannot be variable name.")
    return result

def addMultToOperation(ope, mult):
        isPower = False
        while ope != None :
            if ope.operator == "^":
                isPower = True
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            elif isPower :
                isPower = False
            elif type(ope.left) == float :
                ope.left *= mult
                while ope != None  and ope.operator != None and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            else :
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            if ope.operator != "^":
                ope = ope.right
        return "Done"
    
def addVMultToOperation(ope, mult, isReverse):
        isPower = False
        while ope != None :
            if ope.operator == "^" and not isReverse:
                isPower = True
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            elif isPower :
                isPower = False
            elif isReverse :
                while ope.right != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                # print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = mult
                newOpe.operator = ope.operator
                ope.operator = "/"
                newOpe.right = ope.right
                ope.right = newOpe
                # print(f"result {ope} ")
                ope = ope.right
                if ope == None :
                    return "Done"
            else :
                # print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                # print(f"result {ope} ")
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            if ope.operator != "^":
                ope = ope.right
        return "Done"

def addOMultToOperation(ope, mult, isReverse):
        isPower = False
        # print("enter")
        while ope != None :
            if ope.operator == "^" and not isReverse:
                isPower = True
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = operation(mult.__str__())
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            elif isPower :
                isPower = False
            elif isReverse :
                while ope.right != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                # print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = operation(mult.__str__())
                newOpe.operator = ope.operator
                ope.operator = "/"
                newOpe.right = ope.right
                ope.right = newOpe
                # print(f"result {ope} ")
                ope = ope.right
                if ope == None :
                    return "Done"
            else :
                # print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = operation(mult.__str__())
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                # print(f"result {ope} ")
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            if ope.operator != "^":
                ope = ope.right
        return "Done"
    
def compareToFormatOperation(elt1, elt2):
    if type(elt1) == float and type(elt2) != float:
        return False
    elif type(elt2) == float and type(elt1) != float:
        return True
    if type(elt1) == operation and type(elt2) != operation:
        return False
    elif type(elt2) == operation and type(elt1) != operation:
        return True
    elif type(elt2) == operation and type(elt1) == operation:
        return elt2.__str__() < elt1.__str__()
    elif type(elt2) == str and type(elt1) == str:
        return elt2 < elt1
    else : return False
