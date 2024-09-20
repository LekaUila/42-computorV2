# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:10 by lflandri          #+#    #+#              #
#    Updated: 2024/09/20 15:12:05 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Complex import Complex
acceptedType = [int, float, Complex]

from mathFunction import abs, sqrt

class Vector:
    
    
    def __init__(this, listP=[], lenP=0, value=0,):
        if type(listP) != list or type(lenP) != int or type(value) not in acceptedType:
            raise TypeError()
        this.__list = list()
        if len(listP):
            for i in listP:
                if type(i) == int:
                    this.__list.append(float(i))
                elif type(i) == float:
                    this.__list.append(i)
                elif type(i) in acceptedType:
                    this.__list.append(i)
                else :
                    raise TypeError()
        elif lenP :
            for i in range(lenP):
                this.__list.append(value)
                
    def push(this, toAppend):
        if type(toAppend) not in acceptedType:
            raise TypeError()
        this.__list.append(toAppend)
        
    def size(this):
        return len(this.__list)
    
    def __len__(this):
        return len(this.__list)
                
    def __getitem__(this, key):
        if type(key) != int:
            raise TypeError()
        if len(this.__list) <= key:
            raise IndexError()
        return this.__list[key]
        
    def __setitem__(this, key, value):
        if type(key) != int or type(value) not in acceptedType:
            raise TypeError()
        if type(value) == int:
            this.__list[key] = float(value)        
        else :
            this.__list[key] = value
            
    def __add__(this, other):
        if type(other) != Vector:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't add two Vector of two different size.")
        cop = this.copy()
        for i in range(this.size()):
            cop[i] = this.__list[i] + other.__list[i]
        return cop

    def __sub__(this, other):
        if type(other) != Vector:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't add two Vector of two different size.")
        cop = this.copy()
        for i in range(this.size()):
            cop[i] = this.__list[i] - other.__list[i]
        return cop
        
            
    def __mul__(this, other):
        cop = this.copy()
        if type(other) in acceptedType:
            for i in range(this.size()):
                cop[i] = this.__list[i] * other
        else :
            raise TypeError()
        return cop
        
        
    def __str__(this) -> str:
        return this.__list.__str__()
            
    def copy(this):
        return Vector(listP=this.__list)
    
    def add(this, other):
        this.__list = this.__add__(other).__list


    def sub(this, other):
        this.__list = this.__sub__(other).__list
        
    def scl(this, other):
        this.__list = this.__mul__(other).__list
            
    def dot(this, v):
        if type(v) != Vector :
            raise TypeError()
        if this.size() != v.size():
            raise ArithmeticError("Can't use dot on vector of different size.")
        retValue = 0
        for i in range(len(this.__list)):
            retValue += (this.__list[i] * v[i])
        return retValue
    
    def norm1(this):
        retValue = 0.0
        for i in this.__list:
            retValue += abs(i)
        return retValue
        
    def norm(this):
        retValue = 0.0
        for i in this.__list:
            retValue += abs(i) * abs(i)
        return sqrt(retValue)
            
    def normInf(this):
        retValue = 0.0
        for i in this.__list:
            retValue = abs(i) if abs(i) > retValue else retValue
        return retValue            