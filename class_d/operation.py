# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 13:34:57 by lflandri          #+#    #+#              #
#    Updated: 2024/09/24 18:52:11 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mathFunction import power, abs
from class_d.Matrix import Matrix, acceptedType
from class_d.Complex import Complex
# Utils fonction

def createMatrix(str):
    i = 0
    matrixConstructor = []
    while i < len(str):
        if i < len(str) and (str[i] == '(' or str[i] == '[') :
            newTab = []
            save = i
            startContent = i + 1
            tabcheck = [str[i]]
            i+=1
            while i < len(str) and len(tabcheck) != 0:
                if str[i] == '(' or str[i] == '[' :
                    tabcheck += [str[i]]
                elif str[i] == ')' :
                    if tabcheck[-1] == '(' :
                        tabcheck.pop()
                    else :
                        raise BaseException(f"No end to paranthese init in '{str}' string")
                elif str[i] == ']' :
                    if tabcheck[-1] == '[':
                        tabcheck.pop()
                    else :
                        raise BaseException(f"No end to matrix constructor init in '{str}' string")
                elif str[i] == ',' and len(tabcheck) == 1:
                    newTab.append(operation(str[startContent : i]))
                    startContent = i + 1
                i += 1
            if (len(tabcheck) != 0):
                raise BaseException(f"No end to paranthese init at {save} index of '{str}' string")
            else :
                newTab.append(operation(str[startContent : i - 1]))
                matrixConstructor += [newTab]
        else :
            i += 1
    return Matrix(listP=matrixConstructor)

def parseValueOperation(str):
    i = 0
    result = None
    while i < len(str) and str[i] == ' ' :
        i += 1
    if i == len(str):
        raise BaseException("Inexistant Value In Operation.")
    elif str[i] in "0123456789-" :
        try :
            result = Complex(reel=int(str))
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
            elif type(ope.left) == Complex :
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
    if type(elt1) == Complex and type(elt2) != Complex:
        return False
    elif type(elt2) == Complex and type(elt1) != Complex:
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












# CLASS DEFINITION

class operation:
    
    def __init__(this, str) -> None:
        this.left = None
        this.operator = None
        this.right = None
        if len(str) == 0:
            return
        # print(f"Need to parse {str}")
        i = 0
        try :
            save = -1
            count = 0
            while i < len(str) and str[i] == ' ':
                i+=1
            hasValueExistent = False
            if i < len(str) and (str[i] == '(' or str[i] == '[') :
                save = i
                tabcheck = [str[i]]
                i+=1
                while i < len(str) and len(tabcheck) != 0:
                    if str[i] == '(' or str[i] == '[' :
                        tabcheck += [str[i]]
                    elif str[i] == ')' :
                        if tabcheck[-1] == '(' :
                            tabcheck.pop()
                        else :
                            raise BaseException(f"No end to paranthese initin '{str}' string")
                    elif str[i] == ']' :
                        if tabcheck[-1] == '[':
                            tabcheck.pop()
                        else :
                            raise BaseException(f"No end to matrix constructor initin '{str}' string")
                    i+=1
                if (len(tabcheck) != 0):
                    raise BaseException(f"No end to paranthese init at {save} index of '{str}' string")
                else :
                    if str[save] == '(' :
                        this.left = operation(str[save + 1 : i - 1])
                        if this.left.left == None :
                            raise BaseException(f"Need a value at {save + 1} index of '{str}' string")
                    elif str[save] == '[' :
                        this.left = createMatrix(str[save + 1 : i - 1])
                    hasValueExistent = True

            
            while i < len(str):
                if str[i] not in " 0123456789.abcdefghijclmnopqrstuvwxyzAZERTYUIOPQSDFGHJKLMWXCVBN_":
                    if str[i] in "+-*/^":
                        if not(hasValueExistent) and str[i] == "-" :
                            hasValueExistent = True
                        else :
                            if save == -1 :
                                this.left = parseValueOperation(str[0: i])
                            this.operator = str[i]
                            this.right = operation(str[i + 1:])
                            if this.right.left == None :
                                raise BaseException(f"Need a value at {i + 1} index of '{str}' string")
                            break
                    else :
                        raise BaseException(f"Unknow caracter '{str[i]}' at {i} index of '{str}' string")
                elif save != -1 and str[i] != " ":
                    raise BaseException(f"Need Operator at {i} index of '{str}' string (find '{str[i]}')")
                elif str[i] != " " :
                    hasValueExistent = True
                    
                i+=1
            if this.left == None:
                this.left = parseValueOperation(str)
        except BaseException as exeption :
            raise exeption

    def __eq__(this, other):
        if other == None or type(other) != operation:
            return False
        return (type(this.left) == type(other.left) and this.left == other.left and this.operator == other.operator and type(this.right) == type(other.right) and this.right == other.right)
    
    def opti(this):
        nbGlobalModif = 42
        # print(f"start: {this}")
        while nbGlobalModif > 0:
            nbGlobalModif = 0
            nbModif = 42
            while nbModif > 0:
                nbModif = this.selfOptiSign()
                # print(f"OS  : {this}")
                nbGlobalModif += nbModif
            nbModif = 42
            while nbModif > 0:
                nbModif = this.selfOptiNumberAndNumber()
                # print(f"ONaN: {this}")
                nbGlobalModif += nbModif
            nbModif = 42
            while nbModif > 0:
                nbModif = this.selfOptiNumberAndOperation()
                # print(f"ONaO: {this}")
                nbModif += this.selfOptiVariableAndOperation()
                # print(f"OVaO: {this}")
                nbModif += this.selfOptiOperationAndOperation()
                # print(f"OOaO: {this}")
                nbModif += this.selfOptiNumberAndVariable()
                # print(f"ONaV: {this}")
                nbModif += this.destroyParenthese()
                # print(f"DP  : {this}")
                this.setFormat()
                # print(f"SF  : {this}")
                this.simplify()
                # print(f"SIMP: {this}")
                nbGlobalModif += nbModif
            
    def checkVariableForEquation(this):
        if type(this.left) == str and this.left !="X":
            raise BaseException(f"The only variable name autorised for this equation is 'X' ('{this.left}' is not valable)")
        elif type(this.left) == operation and this.right != None:
            this.left.checkVariableForEquation()
            this.right.checkVariableForEquation()
        elif type(this.left) == operation :
            this.left.checkVariableForEquation()
        elif this.right != None :
            this.right.checkVariableForEquation()
            
            
    def destroyParenthese(this):
        while (type(this.left) == operation and this.operator == None):
            this.operator = this.left.operator
            this.right = this.left.right
            this.left = this.left.left
        opera = this
        modifNb = 0
        if (opera.right != None and type(opera.left) == operation and opera.operator in "-+"):
            modifNb += 1
            child = opera.left
            while child.right != None :
                child = child.right
            child.operator = opera.operator
            child.right= opera.right
            opera.right = opera.left.right
            opera.operator = opera.left.operator
            opera.left = opera.left.left
        while opera != None :
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.destroyParenthese()
                # print("Exit other branch")
            if (opera.right != None and type(opera.right.left) == operation and opera.operator in "-+" and (opera.right.operator == None or opera.right.operator in "-+")):
                modifNb += 1
                # print(f"try type of : {type(opera.right.left)}")
                if opera.operator == "+" :
                    child = opera.right.left
                    while child.right != None :
                        child = child.right
                    child.operator = opera.right.operator
                    child.right= opera.right.right
                    opera.right = opera.right.left
                else :
                    child = opera.right.left
                    while child.right != None :
                        if child.operator == "-" :
                            child.operator = "+"
                        elif child.operator == "+":
                            child.operator = "-"
                        child = child.right
                    child.operator = opera.right.operator
                    child.right= opera.right.right
                    opera.right = opera.right.left
            elif type(opera.left) == operation and opera.operator == None and opera.left.operator == None :
                opera.left = opera.left.left
            opera = opera.right
        return modifNb

    def setFormat(this):
        opera = this
        degre = 0
        modifNb = 0
        # Regrouping Number between Variable
        while opera != None :
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.setFormat()
                # print("Exit other branch")
            if opera.right != None  and (opera.operator == "*" or opera.operator == "/") and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                numberSave = None
                if type(opera.left) == Complex:
                    numberSave = opera
                while opera != None and opera.right != None  and opera.operator == "*" or opera.operator == "/" and (opera.right.operator == None or opera.right.operator != "^") :
                    if opera.operator == "/":
                        opera = opera.right
                    elif numberSave == None and type(opera.right.left) == Complex and  opera.right.operator != "/":
                        numberSave == opera
                        opera = opera.right
                    elif type(opera.right.left) == Complex and  opera.right.operator != "/" :
                        numberSave.left *= opera.right.left
                        opera.operator = opera.right.operator
                        opera.right = opera.right.right
                        modifNb += 1
                    else :
                        opera = opera.right
                    if type(opera.left) == operation:
                        # print(f"Enter other branch {opera.left}")
                        modifNb += opera.left.setFormat()
                        # print("Exit other branch")
            elif opera.right != None  and opera.operator == "+" and degre < 1 and (opera.right.operator == None or opera.right.operator != "^"):
                numberSave = None
                if type(opera.left) == Complex:
                    numberSave = opera
                while opera != None  and opera.operator == "+" and (opera.right.operator == None or opera.right.operator not in "*/^"):
                    if numberSave == None and type(opera.right.left) == Complex :
                        numberSave == opera
                        opera = opera.right
                    elif type(opera.right.left) == Complex :
                        numberSave.left += opera.right.left
                        opera.operator = opera.right.operator
                        opera.right = opera.right.right
                        modifNb += 1
                    else :
                        opera = opera.right
                    if type(opera.left) == operation:
                        # print(f"Enter other branch {opera.left}")
                        modifNb += opera.left.setFormat()
                        # print("Exit other branch")
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                 degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        # Ordering Number before Variable
        opera = this
        while opera != None :
            if opera.right != None  and (opera.operator == "*" or opera.operator == "/") and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                start = opera
                modifHere = 42
                while modifHere :
                    modifHere = 0
                    opera = start
                    while opera != None and opera.right != None  and (opera.operator == "*" or opera.operator == "/") and (opera.right.operator == None or opera.right.operator != "^") :
                        if opera.operator == "/":
                            if opera.right.operator != None and opera.right.operator == "*" and (opera.right.right.operator == None or opera.right.right.operator != "^") :
                                tempV = opera.right.right.left
                                opera.right.right.left = opera.right.left
                                opera.right.left = tempV
                                opera.operator = "*"
                                opera.right.operator = "/"
                            elif opera.right.operator != None and opera.right.operator == "/" and (opera.right.right.operator == None or opera.right.right.operator != "^") :
                                opeTemp = opera
                                while opeTemp != None and opeTemp.right != None  and opeTemp.operator == "/" and (opeTemp.right.operator == None or opeTemp.right.operator != "^"):
                                    opeTemp = opeTemp.right
                                if opeTemp.operator == "*":
                                    opeTemp.operator = "/"
                                    opera.operator = "*"
                                    replaceV = opeTemp.right.left
                                    while opera != opeTemp:
                                        replaceV, opera.right.left = opera.right.left, replaceV
                                        opera = opera.right
                                    replaceV, opera.right.left = opera.right.left, replaceV
                                else :
                                    break
                            else :
                                break
                            continue
                        if compareToFormatOperation(opera.left, opera.right.left):
                            opera.left, opera.right.left = opera.right.left, opera.left
                            modifNb+=1
                            modifHere+=1
                        opera = opera.right
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                 degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb

    def simplify(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.simplify()
                # print("Exit other branch")
            if opera.right != None and opera.right.left == opera.left and opera.operator == "/" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                result = 1.0
            elif opera.right != None and  ((type(opera.right.left) == Complex and opera.right.left == 1.0) or (type(opera.left) == Complex and opera.left == 1.0)) and opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                if type(opera.right.left) == Complex and opera.right.left == 1.0:
                   result = opera.left
                else :
                    result = opera.right.left
            if result != None :
                # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                opera.operator = opera.right.operator
                opera.right = opera.right.right
                opera.left = result
                modifNb += 1
            else :
                if opera.operator != None and opera.operator == "^":
                    degre = 3
                elif opera.operator != None and opera.operator == "/":
                    degre = 2
                elif opera.operator != None and opera.operator == "*":
                    degre = 1
                else :
                    degre = 0
                opera = opera.right
        return modifNb
    
    def selfOptiSign(this):
        opera = this
        modifNb = 0
        while opera != None :
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiSign()
                # print("Exit other branch")
            if (opera.right != None and opera.operator == "-" and type(opera.right.left) == Complex and (opera.right.operator == None or opera.right.operator not in "/*^")):
                opera.right.left = -opera.right.left
                opera.operator = "+"
                modifNb += 1
            opera = opera.right
        return modifNb
   
    def selfOptiNumberAndVariable(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiNumberAndVariable()
                # print("Exit other branch")
            if (type(opera.left) == str and opera.right != None and type(opera.right.left) == Complex):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if opera.operator == "^" and (opera.right.operator == None or opera.right.operator != "^"):
                    if opera.right.left == 0:
                        result = 1
                    elif opera.right.left == 1:
                        result = opera.left
                    else :
                        if (opera.right.left - Complex(int(opera.right.left)) != 0.0):
                            print(f"WARNING : find {opera.right.left} as exponent (can only have integer exponent) -> {opera.right.left} will be considert as {int(opera.right.left)}")
                        result = operation(f"{opera.left}" + (str([f"* {opera.left}" for i in range(int(abs(opera.right.left)) - 1)])[1:-1].replace("'", "").replace(",", "")))
                        if (opera.right.left < 0):
                            result = operation(f"1 / ({result})")
                elif opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^") and opera.right.left == 0:
                    raise BaseException("can't divise by 0.")
                elif opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    opera.operator = "*"
                    opera.right.left = 1.0 / opera.right.left
                    modifNb += 1
                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = result
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb
    
    def selfOptiOperationAndOperation(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiOperationAndOperation()
                # print("Exit other branch")
            if (type(opera.left) == operation and opera.right != None and type(opera.right.left) == operation):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addOMultToOperation(opera.left, opera.right.left, False)
                elif type(opera.right.left) == str and opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addOMultToOperation(opera.left,opera.right.left, True)

                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = opera.left
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb
         
    def selfOptiVariableAndOperation(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiVariableAndOperation()
                # print("Exit other branch")
            if (type(opera.left) == str and opera.right != None and type(opera.right.left) == operation) or (type(opera.left) == operation and opera.right != None and type(opera.right.left) == str):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if type(opera.left) == str:
                    nb = opera.left
                    ope = opera.right.left
                else :
                    nb = opera.right.left
                    ope = opera.left
                if opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addVMultToOperation(ope, nb, False)
                elif type(opera.right.left) == str and opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addVMultToOperation(ope,nb, True)

                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = ope
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb
            
    def selfOptiNumberAndOperation(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiNumberAndOperation()
                # print("Exit other branch")
            if (type(opera.left) == Complex and opera.right != None and type(opera.right.left) == operation) or (type(opera.left) == operation and opera.right != None and type(opera.right.left) == Complex):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if type(opera.left) == Complex:
                    nb = opera.left
                    ope = opera.right.left
                else :
                    nb = opera.right.left
                    ope = opera.left
                if opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addMultToOperation(ope, nb)
                elif type(opera.right.left) == Complex and opera.operator == "/" and opera.right.left == 0.0 and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    raise BaseException("can't divise by 0.")
                elif type(opera.right.left) == Complex and opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addMultToOperation(ope, 1 / nb)
                elif opera.operator == "^" and type(opera.left) == operation  and (opera.right.operator == None or opera.right.operator != "^"):
                    opera.left = opera.left.power(opera.right.left)
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = ope
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb

        
    def selfOptiNumberAndNumber(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiNumberAndNumber()
                # print("Exit other branch")
                if opera.left.operator == None:
                    opera.left = opera.left.left
            elif type(opera.left) == Complex and opera.right != None and type(opera.right.left) == Complex:
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if opera.operator == "/" and opera.right.left == 0.0 and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    raise BaseException("can't divise by 0.")
                elif opera.operator == "/" and degre < 3 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = opera.left / opera.right.left
                elif opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = opera.left * opera.right.left
                elif opera.operator == "+" and degre < 1 and (opera.right.operator == None or opera.right.operator not in "*/^"):
                    result = opera.left + opera.right.left
                elif opera.operator == "-" and degre < 1 and (opera.right.operator == None or opera.right.operator not in "*/^"):
                    result = opera.left - opera.right.left 
                elif opera.operator == "^" and (opera.right.operator == None or opera.right.operator != "^"):
                    result = power(opera.left, opera.right.left)
                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = result
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 3
            elif opera.operator != None and opera.operator == "/":
                degre = 2
            elif opera.operator != None and opera.operator == "*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb
    
    def __mul__(this, mult):
        isPower = False
        # print("enter")
        opera = operation(this.__str__())
        ope = opera
        while ope != None :
            if ope.operator == "^":
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
                    return opera
            elif isPower :
                isPower = False
            else :
                if ope.operator == "/" and mult == ope.right.left :
                    ope.operator = ope.right.operator
                    ope.right = ope.right.right
                    while ope != None and ope.operator != None  and ope.operator in "*/^" :
                        ope = ope.right
                    if ope == None :
                        return opera
                elif ope.right == None or (ope.right.operator == None or ope.right.operator not in "*/^"):
                    newOpe = operation("")
                    newOpe.left = operation(mult.__str__())
                    newOpe.operator = ope.operator
                    ope.operator = "*"
                    newOpe.right = ope.right
                    ope.right = newOpe
                    while ope != None and ope.operator != None  and ope.operator in "*/^" :
                        ope = ope.right
                    if ope == None :
                        return opera
            if ope.operator != "^":
                ope = ope.right
        return opera
    
    def __rmul__(this, other):
        return this.__mult__(other, this)
            
    def __repr__(this):
        returnValue = ""
        opera = this
        while opera != None :
            if (opera.operator != None) :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left}) {opera.operator} "
                else :
                    returnValue += f"{opera.left} {opera.operator} "  
            else :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left})"
                else :
                    returnValue += f"{opera.left}"
            opera = opera.right 
        return returnValue

    def __str__(this):
        returnValue = ""
        opera = this
        while opera != None :
            if (opera.operator != None) :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left}) {opera.operator} "
                else :

                    returnValue += f"{opera.left} {opera.operator} "  
            else :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left})"
                else :
                    returnValue += f"{opera.left}"
            opera = opera.right
        return returnValue

    def hasPower(this):
        opera = this
        while opera != None :
            if (opera.operator == "^" and (type(opera.right.left) == operation or type(opera.right.left) == str)):
                return True
            opera = opera.right
        return False
    
    def hasDivision(this):
        opera = this
        while opera != None :
            if (opera.operator == "/" and (type(opera.right.left) == operation or type(opera.right.left) == str)):
                return operation(opera.right.left.__str__())
            opera = opera.right
        return None
    
    def replaceVariableBy(this,V, nb):
        opera = this
        while opera != None :
            if type(opera.left) == operation:
                opera.left.replaceVariableBy(V, nb)
            elif type(opera.left) == str and opera.left == V:
                opera.left = nb
            opera = opera.right

    def power(this, flt):
        if (flt - Complex(int(flt)) != 0.0): #TODO rework this
            print(f"WARNING : find {flt} as exponent (can only have integer exponent) -> {flt} will be considert as {int(flt)}")
        flt = int(flt)
        if flt == 1:
            return operation(this.__str__())
        if flt == 0:
            newOpe = operation("")
            newOpe.left = 1.0
            return newOpe
        newOpe = operation("")
        newOpe.left = operation(this.__str__())
        OpeEnd = newOpe
        for i in range(abs(flt) - 1):
            addingOpe = operation(this.__str__())
            multOpe = operation("")
            multOpe.left = addingOpe
            while OpeEnd.right != None:
                OpeEnd = OpeEnd.right
            OpeEnd.operator = "*"
            OpeEnd.right = multOpe
        if flt > 0:
            # print (f"newOpe = {newOpe}")
            return newOpe
        opeSpe = operation("")
        opeSpe.left = 1
        opeSpe.operator = "/"
        opeSpe.right = operation("")
        opeSpe.right.left = newOpe
        return opeSpe
            
            
        
