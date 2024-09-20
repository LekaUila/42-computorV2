# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:04 by lflandri          #+#    #+#              #
#    Updated: 2024/07/26 13:41:17 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Vector import Vector, acceptedType, Complex

class Matrix:
    
    def __init__(this, listP=[], lenth=0, weith=0):
        if type(listP) != list or type(lenth) != int or type(weith) != int :
            raise TypeError()
        this.__list = list()
        if len(listP):
            test = len(listP[0])
            for i in listP:
                if test != len(i):
                    raise ArithmeticError("Can't create Matrix with different size of ligne")
                if type(i) == list:
                    this.__list.append(Vector(listP=i))
                else :
                    raise TypeError()
        else :
            for i in range(lenth):
                this.__list.append(Vector(lenP=weith))
                
    def __getitem__(this, key):
        if type(key) != int:
            raise TypeError()
        if len(this.__list) <= key:
            raise IndexError()
        return this.__list[key]
        
    def __setitem__(this, key, value):
        if type(key) != int or type(value) != Vector:
            raise TypeError()
        this.__list[key] = value
        
    def size(this):
        if len(this.__list):
            return (this.__list[0].size(),len(this.__list))
        return None
    def __len__(this):
            return len(this.__list)
    
    def isSquare(this):
        if len(this.__list):
            return this.__list[0].size() == len(this.__list)
        return False
        
    def __add__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't add two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] + other.__list[i]
        return cop
    
    def __radd__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't add two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] + other.__list[i]
        return cop

    def __sub__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't sub two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] - other.__list[i]
        return cop
    
    def __rsub__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't sub two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] - other.__list[i]
        return cop
        
            
    def __mul__(this, other):
        cop = 0
        if type(other) in acceptedType:
            cop = this.copy()
            for i in range(len(this.__list)):
                cop[i] = this.__list[i] * other
                
        elif type(other) == Vector:
            cop = Vector(lenP=this.size()[1])
            if this.size()[0] != other.size():
                raise ArithmeticError("Can't multiply Matrix with Vector : Size don't match.")
            for j in range(this.size()[1]):
                nb = 0
                for i in range(other.size()):
                    nb += this[j][i] * other[i]
                cop[j] = nb
        elif type(other) == Matrix:
            if this.size()[0] != other.size()[1]:
                raise ArithmeticError(f"Can't multiply matrix : size error")
            #max = this.size()[1] if this.size()[1] > this.size()[0] else this.size()[0]
            cop = Matrix(lenth=this.size()[1], weith=other.size()[0])
            for iMult in range(other.size()[0]):
                for jMult in range(this.size()[1]):
                    nb = 0
                    for i in range(this.size()[0]):
                        nb += this[jMult][i] * other[i][iMult]
                    cop[jMult][iMult] = nb
        else :
            raise TypeError()
        return cop
    
    def __rmul__(this, other):
        cop = 0
        if type(other) in acceptedType:
            cop = this.copy()
            for i in range(len(this.__list)):
                cop[i] = this.__list[i] * other
                
        elif type(other) == Vector:
            cop = Vector(lenP=this.size()[1])
            if this.size()[0] != other.size():
                raise ArithmeticError("Can't multiply Matrix with Vector : Size don't match.")
            for j in range(this.size()[1]):
                nb = 0
                for i in range(other.size()):
                    nb += this[j][i] * other[i]
                cop[j] = nb
        elif type(other) == Matrix:
            if this.size()[0] != other.size()[1]:
                raise ArithmeticError(f"Can't multiply matrix : size error")
            #max = this.size()[1] if this.size()[1] > this.size()[0] else this.size()[0]
            cop = Matrix(lenth=this.size()[1], weith=other.size()[0])
            for iMult in range(other.size()[0]):
                for jMult in range(this.size()[1]):
                    nb = 0
                    for i in range(this.size()[0]):
                        nb += this[jMult][i] * other[i][iMult]
                    cop[jMult][iMult] = nb
        else :
            raise TypeError()
        return cop
        
        
    def __str__(this):
        s = ""
        for i in this.__list:
            s += "|" + i.__str__() + "|\n"
        return s 
    
    def add(this, other):
        this.__list = this.__add__(other).__list


    def sub(this, other):
        this.__list = this.__sub__(other).__list
        
    def scl(this, other):
        this.__list = this.__mul__(other).__list
        
    def copy(this):
        newMatrix = Matrix(lenth=len(this.__list))
        for i in range(len(this.__list)):
            newMatrix[i] = this.__list[i].copy()
        return newMatrix
    
    def mulVec(this, vec):
        if type(vec) != Vector:
            raise TypeError()
        return this * vec
    
    def mulMat(this, mat):
        if type(mat) != Matrix:
            raise TypeError()
        return this * mat
    
    def trace(this):
        if this.__list[0].size() != len(this.__list):
            raise ArithmeticError("Can't calcul trace of non square matrix.")
        retValue = 0
        for i in range(len(this.__list)):
            retValue += this[i][i]
        return retValue
    
    def transpose(this):
        newMatrix = Matrix(lenth=this.__list[0].size(), weith=len(this.__list))
        for i in range(len(this.__list)):
            for j in range(this.__list[0].size()):
                newMatrix[j][i] = this[i][j]
        return newMatrix
    
    def getIndexZeroLine(this, start, end, nbZero):
        if start < 0 or end < 0 or start > len(this.__list) or end > len(this.__list):
            raise IndexError()
        for i in range(start, end):
            count = 0
            for test in this[i] :
                if test == 0:
                    count += 1
                else :
                    if count == nbZero:
                        return i
                    break
        return -1
    
    def rowEchelon(this):
        newMatrix = this.copy()
        ind = 0
        decX = 0
        while ind + decX < this.__list[0].size() and ind < len(this.__list):
            if newMatrix[ind][ind + decX] != 1 :
                newMatrix[ind] = newMatrix[ind] * (1 / newMatrix[ind][ind + decX])
            for i in range(ind + 1, len(this.__list)):
                if newMatrix[i][ind + decX] != 0:
                    newMatrix[i] = newMatrix[i] + newMatrix[ind] * (- newMatrix[i][ind + decX])
            for i in range(0, ind):
                if newMatrix[i][ind + decX] != 0.:
                    newMatrix[i] = newMatrix[i] + newMatrix[ind] * (- newMatrix[i][ind + decX])
            if ind + decX +1 >= this.__list[0].size() or ind + 1 >= len(this.__list):
                break
            if newMatrix[ind + 1][ind + decX + 1] == 0:
                newLigneInd = newMatrix.getIndexZeroLine(ind + 1, len(this.__list), ind + decX + 1)
                if newLigneInd != -1:
                    newMatrix[ind + 1], newMatrix[newLigneInd] = newMatrix[newLigneInd], newMatrix[ind + 1]
                else:
                    while ind + decX +1 < this.__list[0].size() and newMatrix[ind + 1][ind + decX + 1] == 0:
                        decX += 1
            ind += 1
        return newMatrix
            
    def determinant(this):
        if not this.isSquare():
            raise ArithmeticError('Need a square matrix to find a determinant')
        if len(this.__list) == 0:
            return 0
        if len(this.__list) == 1:
            return this[0][0]
        if len(this.__list) == 2:
            return this[0][0] * this[1][1] - this[1][0] * this[0][1]
        determinant = 0
        for i in range(len(this.__list)):
            coef = this[0][i]
            if i % 2 != 0:
                coef = coef * -1
            newMatrix = Matrix(lenth=len(this.__list) - 1, weith=len(this.__list) - 1)
            skip = 0
            for x in range(len(this.__list)):
                if x != i:
                    for y in range(1, len(this.__list)):
                        newMatrix[y - 1][x - skip] = this[y][x]
                else :
                    skip = 1
            determinant += coef * newMatrix.determinant()
        return determinant
    
    def cofactor(this):
        if not this.isSquare():
            raise ArithmeticError('Need a square matrix to create a cofactor Matrix')
        if len(this.__list) == 0:
            return 0
        if len(this.__list) == 1:
            return this[0][0]
        retMatrix = this.copy()
        for i in range(len(this.__list)):
            for j in range(len(this.__list)):
                coef = 1
                if (i + j) % 2 != 0:
                    coef = coef * -1
                newMatrix = Matrix(lenth=len(this.__list) - 1, weith=len(this.__list) - 1)
                skip = 0
                for x in range(len(this.__list)):
                    if x != i:
                        skip2 = 0
                        for y in range( len(this.__list)):
                            if y != j:
                                    newMatrix[y - skip2][x - skip] = this[y][x]
                            else :
                                skip2 = 1
                    else :
                        skip = 1
                retMatrix[j][i] = coef * newMatrix.determinant()
        return retMatrix
                
    def inverse(this):
        det = this.determinant()
        if det == 0:
            raise ArithmeticError("Can't inverse Matrix with null determinant.")
        return this.cofactor().transpose() * (1 / det)
    
    def rank(this):
        rank = 0
        newMatrix = this.rowEchelon()
        for vect in newMatrix:
            isOK = False
            for elt in vect:
                if elt != 0.0:
                    isOK = True
                    break
            if isOK:
                rank += 1
        return rank
    