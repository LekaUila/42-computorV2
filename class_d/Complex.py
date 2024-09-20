# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Complex.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/17 15:53:22 by lflandri          #+#    #+#              #
#    Updated: 2024/07/26 13:53:39 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Complex :
    
    def __init__(this, reel, imaginary):
        this.reel = reel
        this.imaginary = imaginary
        
    
    def __str__(this) -> str:
        if this.imaginary == 0:
            return f"{this.reel}"
        if this.reel == 0:
            return f"{this.imaginary}i"
        if this.imaginary < 0 :
            return f"{this.reel} {this.imaginary}i"
        return f"{this.reel} + {this.imaginary}i"
    
    def __repr__(this) -> str:
        if this.imaginary < 0 :
            return f"{this.reel} {this.imaginary}i"
        return f"{this.reel} + {this.imaginary}i"        
        
    def __add__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel + other, this.imaginary)
        elif type(other) == Complex :
            return Complex(this.reel + other.reel, this.imaginary + other.imaginary)
        
    def __radd__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel + other, this.imaginary)
        elif type(other) == Complex :
            return Complex(this.reel + other.reel, this.imaginary + other.imaginary)
    
    def __sub__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel - other, this.imaginary)
        elif type(other) == Complex :
            return Complex(this.reel - other.reel, this.imaginary - other.imaginary)
        
    def __rsub__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel - other, this.imaginary)
        elif type(other) == Complex :
            return Complex(this.reel - other.reel, this.imaginary - other.imaginary)
    
    def __mul__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel * other, this.imaginary * other)
        elif type(other) == Complex :
            return Complex((this.reel * other.reel) - (this.imaginary * other.imaginary), (this.reel * other.imaginary) + (this.imaginary * other.reel))
        
    def __rmul__(this, other):
        if type(other) == int or type(other) == float:
            return Complex(this.reel * other, this.imaginary * other)
        elif type(other) == Complex :
            return Complex((this.reel * other.reel) - (this.imaginary * other.imaginary), (this.reel * other.imaginary) + (this.imaginary * other.reel))
    
    def __truediv__(this, other):
        if type(other) == int or type(other) == float:
            if other == 0:
                raise ZeroDivisionError()
            return Complex(this.reel / other, this.imaginary / other)
        elif type(other) == Complex :
            numerateur = this.copy()
            denominateur = other.copy()
            conjugue = Complex(denominateur.reel, - denominateur.imaginary)
            numerateur = numerateur * conjugue
            denominateur = denominateur * conjugue
            if denominateur.reel == 0:
                raise ZeroDivisionError()
            return Complex(numerateur.reel / denominateur.reel, numerateur.imaginary / denominateur.reel)
        
    def __rtruediv__(this, other):
        if type(other) == int or type(other) == float:
            if other == 0:
                raise ZeroDivisionError()
            return Complex(this.reel / other, this.imaginary / other)
        elif type(other) == Complex :
            numerateur = this.copy()
            denominateur = other.copy()
            conjugue = Complex(denominateur.reel, - denominateur.imaginary)
            numerateur = numerateur * conjugue
            denominateur = denominateur * conjugue
            if denominateur.reel == 0:
                raise ZeroDivisionError()
            return Complex(numerateur.reel / denominateur.reel, numerateur.imaginary / denominateur.reel)
    def __pow__(this, other):
        if type(other) != int or other < 0:
            raise TypeError()
        if other == 0:
            return Complex(1, 0)
        new = this.copy()
        if other == 1:
            return new
        new = this.copy()
        for i in range(other - 1):
            new = new * this
        return new
    
    def __eq__(this, other):
        if type(other) == int or type(other) == float:
            if this.imaginary != 0:
                return False
            return (this.reel == other)
        elif type(other) == Complex :
            return (this.reel == other.reel and this.imaginary == other.imaginary)
        
    def __ne__(this, other):
        if type(other) == int or type(other) == float:
            if this.imaginary != 0:
                return True
            return not(this.reel == other)
        if type(other) == Complex :
            return not(this.reel == other.reel and this.imaginary == other.imaginary)
        
    def copy(this):
        return Complex(this.reel, this.imaginary)
    
        
        