# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    equationResolver.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/20 15:22:14 by lflandri          #+#    #+#              #
#    Updated: 2024/09/20 15:24:53 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.operation import  operation
from mathFunction import polynomialEquationResolver

SEEINVALIDSOLUTION = True

def getListPartOperation(ope):
    list = [0, 0, 0]
    sign = 1
    while ope != None:
        nb = 0
        if type(ope.left) != float :
            nb = 1 * sign
            countXPower = 1
        else :
            nb = ope.left * sign
            countXPower = 0
        while ope.operator == "*":
            countXPower += 1
            ope = ope.right
        while len(list) < countXPower + 1:
            list.append(0)
        list[countXPower] += nb
        # print(f"find {nb} * X ^ {countXPower} : new tab : {list}")
        if ope.operator == "+" :
            sign = 1
        else :
            sign = -1
        ope = ope.right
    return list

def printReducedForm(listPArtOperation):
    print("reduced form : ", end="")
    ap = False
    for i in range(len(listPArtOperation) - 1, -1, -1):
        if listPArtOperation[i] == 0 :
            continue
        if ap :
            print(" + ", end='')
        ap = True
        if listPArtOperation[i] < 0 :
            print(f"({listPArtOperation[i]})", end="")
        else : 
            print(f"{listPArtOperation[i]}", end="")
        if i == 1 :
             print(f" * x", end="")
        elif i != 0 :
             print(f" * x ^ {i}", end="")
    print(" = 0")

def equationResolve(entry):
    # if len(sys.argv) != 2:
    #         raise (BaseException("Wrong number of argument."))
    #     entry = sys.argv[1]
        p = entry.find("=")
        if p == -1 :
            raise BaseException("this isn't an equation.")
        # print(f"start to parse with : '{entry[:p]} = {entry[p + 1:]}'\n")
        ope1 = operation(entry[:p])
        ope2 = operation(entry[p + 1:])
        leftOpe = operation(ope1.__str__())
        rightOpe = operation(ope2.__str__())
        continueOpti = True
        while continueOpti :
            continueOpti = False
            # print(f"ope1 before operation : {ope1}")
            # print("__________________________________________")
            ope1.checkVariableForEquation()
            ope1.opti()
            # print("__________________________________________")
            # print(f"ope1 after operation : {ope1}")
            # print("__________________________________________")
            # print(f"ope2 before operation : {ope2}")
            # print("__________________________________________")
            ope2.checkVariableForEquation()
            ope2.opti()
            # print("__________________________________________")
            # print(f"ope2 after operation : {ope2}")
            # print("__________________________________________")
            # print(f"ope after operation : {ope1} = {ope2}")
            if ope1.hasPower() or ope2.hasPower():
                raise BaseException("This equation has x as exponent : can't be reslolve.")
            result = ope1.hasDivision()
            # print(f"Find '{result}' has result from ope1")
            if result != None:
                continueOpti = True
                ope1 = ope1 * result
                ope2 = ope2 * result
            else :
                result = ope2.hasDivision()
                # print(f"Find '{result}' has result from ope2")
                if result != None:
                    continueOpti = True
                    ope1 = ope1 * result
                    ope2 = ope2 * result
        finalOpe = operation(f"{ope1} - ({ope2})")
        finalOpe.opti()  
        # print("__________________________________________")
        # print(f"operation : {finalOpe} = 0")
        # print("__________________________________________")
        listPArtOperation = getListPartOperation(finalOpe)
        printReducedForm(listPArtOperation)
        equationdegree = 0
        for i in range(len(listPArtOperation) - 1, -1, -1):
            if listPArtOperation[i] != 0:
                equationdegree = i
                break
        print(f"Polynomial degree : {equationdegree}") 
        if equationdegree == 0:
            print("After simplification, we didn't have X remaining in this equation. This isn't an equation anymore.")
        elif equationdegree == 1:
            print(f"The solution is '{(listPArtOperation[0] * -1) / listPArtOperation[1]}'.")
        elif equationdegree == 2:
            listSolution = polynomialEquationResolver(listPArtOperation[2],listPArtOperation[1],listPArtOperation[0])
            listValideSolution = []
            listInvalideSolution = []
            for solutionTest in listSolution:
                if type(solutionTest) == str:
                    listValideSolution.append(solutionTest)
                else :
                    try :
                        copyLeft = operation(leftOpe.__str__())
                        copyRight = operation(rightOpe.__str__())
                        copyLeft.replaceVariableBy("X", solutionTest)
                        copyRight.replaceVariableBy("X", solutionTest)
                        copyLeft.opti()
                        copyRight.opti()
                        # print(f"try : {copyLeft} == {copyRight}")
                        if abs(copyLeft.left - copyRight.left) < 0.00000000000001:
                            listValideSolution.append(solutionTest)
                        else :
                            listInvalideSolution.append(solutionTest)
                    except :
                        listInvalideSolution.append(solutionTest)
            if (len(listValideSolution) == 0):
                print("There is no valide solution")
            else :
                if len(listValideSolution) > 1:
                    print(f"There are {len(listValideSolution)} solutions")
                else :
                    print(f"There are {len(listValideSolution)} solution")
                for solutionValide in listValideSolution :
                    print(solutionValide)
            if len(listInvalideSolution) > 0 and SEEINVALIDSOLUTION:
                if len(listInvalideSolution) > 1:
                    print(f"There are {len(listInvalideSolution)} invalides solutions")
                else :
                    print(f"There are {len(listInvalideSolution)} invalide solution")
                for solutionnotValide in listInvalideSolution :
                    print(solutionnotValide)
                
            
            
        else :
            raise BaseException(f"Equation of {equationdegree} degree can't be resolve.")
        
        # TODO : resolve équation