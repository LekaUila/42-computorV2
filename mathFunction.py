# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mathFunction.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 20:35:34 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 12:22:55 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def power(flt1, flt2) -> float:
    if (flt2 - float(int(flt2)) != 0.0):
        print(f"WARNING : find {flt2} as exponent (can only have integer exponent) -> {flt2} will be considert as {int(flt2)}")
    result = flt1
    flt2 = int(flt2)
    if flt2 == 0.0 :
        return 1
    if flt2 == 1.0 :
        return flt1
    if flt2 == -1.0 :
        return 1 / flt1
    if flt2 < 0 :
        for i in range(int(flt2 * -1) - 1):
            result *= flt1
        return 1 / result        
    for i in range(int(flt2) - 1):
        result *= flt1
    return result

def sqrt(n):
    i = 0
    result = 1
    if n == 0.0:
        return 0.0
    while i < 50:
        result = (result + (n / result)) / 2
        i+=1
    return result

def abs(flt):
    return flt *-1 if flt < 0 else flt

def polynomialEquationResolver(a, b, c):
    d = (b * b) - (4 * a * c)
    print(f"Discriminant is {d}")
    if d == 0:
        return [-b / (2 * a)]
    elif d > 0 :
        return [(-b - sqrt(d))/ (2 * a), (-b + sqrt(d))/ (2 * a)]
    else :
        return [f"{-b / (2 * a)} - {sqrt(d)/ (2 * a)}i", f"{-b / (2 * a)} + {sqrt(d)/ (2 * a)}i"]
        