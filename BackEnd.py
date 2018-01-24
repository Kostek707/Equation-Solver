#Imports libraries
import sympy
import numpy as np
from numpy.linalg import inv

class SystemOfEquationSolver:
    """
    Initializes the parameters that must be entered to create the object.
    They are both sides of both equations
    """
    def __init__(self,first_equation_left,first_equation_right,second_equation_left,second_equation_right):
        self.a=first_equation_left
        self.b=first_equation_right
        self.c=second_equation_left
        self.d=second_equation_right
    def solve(self):
        x=sympy.symbols('x')
        y=sympy.symbols('y')
        #A function that checks whether a given part of the list is x
        def is_x(part_of_list):
            try:
                float(part_of_list)
                return False
            except:
                return True
        """
        First is a variable that checks which equation is currently being processed
        """
        First=True
        while True:
            if First is False:
                a=self.c
                b=self.d
            if First is True:
                a=self.a
                b=self.b
            #Checks whether it is possible to simplify algebraic expressions in parentheses
            try:
                #Simplifies algebraic expressions in parentheses
                a=sympy.expand(a)
                b=sympy.expand(b)
            except:
                pass
            """
            Simplifies the algebraic expression on both sides of the equation and
            removes blank characters from the string
            """
            try:
                a=str(sympy.sympify(a)).replace(' ','')
                b=str(sympy.sympify(b)).replace(' ','')
            except:
                a=str(sympy.sympify(a))
                b=str(sympy.sympify(b))

            #Turns both sides of the equation into two lists
            list_a1=list(a)
            list_b1=list(b)
            #Creates empty lists
            list_a2=[]
            list_b2=[]

            list_a3=[]
            list_b3=[]

            c1=0
            c2=0
            x=0
            y=0
            """
            Combines numbers in a list, for example it converts ['1', '0'] to ['10']
            or combines the number of x, for example, converts ['2', '*', 'x'] to ['2 * x']
            """
            for new_a in list_a1:
                now=""
                if x >> 0:
                    x=x-1
                    c1=c1+1
                    continue
                now=now+new_a
                if new_a.isdigit() is True:
                    x=1
                    while True:
                        try:
                            if list_a1[c1+x].isdigit() is True:
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="x":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="y":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]==".":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="*":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="/":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            x=x-1
                            break
                        except:
                            break
                if new_a == "x":
                    x=1
                    while True:
                        try:
                            if list_a1[c1+x].isdigit() is True:
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]==".":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="*":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            if list_a1[c1+x]=="/":
                                now=now+list_a1[c1+x]
                                x=x+1
                                continue
                            x=x-1
                            break
                        except:
                            break
                if new_a == "y":
                     x=1
                     while True:
                         try:
                             if list_a1[c1+x].isdigit() is True:
                                 now=now+list_a1[c1+x]
                                 x=x+1
                                 continue
                             if list_a1[c1+x]==".":
                                 now=now+list_a1[c1+x]
                                 x=x+1
                                 continue
                             if list_a1[c1+x]=="*":
                                 now=now+list_a1[c1+x]
                                 x=x+1
                                 continue
                             if list_a1[c1+x]=="/":
                                 now=now+list_a1[c1+x]
                                 x=x+1
                                 continue
                             x=x-1
                             break
                         except:
                             break

                list_a2.append(now)
                c1=c1+1

            for new_b in list_b1:
                now=""
                if y >> 0:
                    y=y-1
                    c2=c2+1
                    continue
                now=now+new_b
                if new_b.isdigit() is True:
                    y=1
                    while True:
                        try:
                            if list_b1[c2+y].isdigit() is True:
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="y":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]==".":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="*":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="/":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            y=y-1
                            break
                        except:
                            break
                if new_b == "x":
                    y=1
                    while True:
                        try:
                            if list_b1[c2+y].isdigit() is True:
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]==".":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="*":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="/":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            y=y-1
                            break
                        except:
                            break
                if new_b == "y":
                    y=1
                    while True:
                        try:
                            if list_b1[c2+y].isdigit() is True:
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]==".":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="*":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            if list_b1[c2+y]=="/":
                                now=now+list_b1[c2+y]
                                y=y+1
                                continue
                            y=y-1
                            break
                        except:
                            break
                list_b2.append(now)
                c2=c2+1



            c1=0
            c2=0
            x=0
            y=0
            wait=False
            """
            Moves x and y to the left side of the equation and numbers to the right side
            """
            for final_a in list_a2:

                if wait is True:
                    wait=False
                    c1=c1+1
                    continue

                if final_a =="-":
                    if is_x(list_a2[c1+1]) is True:
                        list_a3.append("-")
                        list_a3.append(list_a2[c1+1])
                        wait=True
                    if is_x(list_a2[c1+1]) is False:
                        list_b3.append("+")
                        list_b3.append(list_a2[c1+1])
                        wait=True
                    c1=c1+1
                    continue

                if final_a == "+":
                    if is_x(list_a2[c1+1]) is True:
                        list_a3.append("+")
                        list_a3.append(list_a2[c1+1])
                        wait=True
                    if is_x(list_a2[c1+1]) is False:
                        list_b3.append("-")
                        list_b3.append(list_a2[c1+1])
                        wait=True
                    c1=c1+1
                    continue

                if c1==0:
                    if is_x(list_a2[c1]) is True:
                        list_a3.append("+")
                        list_a3.append(list_a2[c1])
                    if is_x(list_a2[c1]) is False:
                        list_b3.append("-")
                        list_b3.append(list_a2[c1])
                c1=c1+1

            wait=False

            for final_b in list_b2:

                if wait is True:
                    wait=False
                    c2=c2+1
                    continue

                if final_b =="-":
                    if is_x(list_b2[c2+1]) is True:
                        list_a3.append("+")
                        list_a3.append(list_b2[c2+1])
                        wait=True
                    if is_x(list_b2[c2+1]) is False:
                        list_b3.append("-")
                        list_b3.append(list_b2[c2+1])
                        wait=True
                    c2=c2+1
                    continue

                if final_b == "+":
                    if is_x(list_b2[c2+1]) is True:
                        list_a3.append("-")
                        list_a3.append(list_b2[c2+1])
                        wait=True
                    if is_x(list_b2[c2+1]) is False:
                        list_b3.append("+")
                        list_b3.append(list_b2[c2+1])
                        wait=True
                    c2=c2+1
                    continue

                if c2==0:
                    if is_x(list_b2[c2]) is True:
                        list_a3.append("-")
                        list_a3.append(list_b2[c2])
                    if is_x(list_b2[c2]) is False:
                        list_b3.append("+")
                        list_b3.append(list_b2[c2])

                c2=c2+1

            #Adds 0 to the list that is the right side of the equation if it is empty
            if not list_b3:
                list_b3.append('0')
            #Simplifies both sides of the equation
            left_first=str(sympy.sympify(''.join(list_a3)))
            right_first=str(sympy.sympify(''.join(list_b3)))

            #Converts the left side to the list and the right one to the float
            right_first=float(right_first)
            left_first=list(left_first)

            c1=0
            x=0
            left_second=[]
            #Combines numbers in a list, for example, it converts ['2', '0', '*', 'x'] to ['20', '*', 'x']
            for final in left_first:
                now=""
                if x >> 0:
                    x=x-1
                    c1=c1+1
                    continue
                now=now+final
                if final.isdigit() is True:
                    x=1
                    while True:
                        try:
                            if left_first[c1+x].isdigit() is True:
                                now=now+left_first[c1+x]
                                x=x+1
                                continue
                            if left_first[c1+x]==".":
                                now=now+left_first[c1+x]
                                x=x+1
                                continue
                            x=x-1
                            break
                        except:
                            break
                left_second.append(now)
                c1=c1+1
            #Creates variables that are both sides of both equations
            if First is True:
                first_equation=left_second
                result1=[right_first]
                First=False
                continue
            if First is False:
                second_equation=left_second
                result2=[right_first]
                break
        first=[]
        second=[]
        unkown=[]
        repeat=False
        #Removes unnecessary strings from the list
        for i in range(0,first_equation.count(' ')):
            first_equation.remove(' ')
        for i in range(0,second_equation.count(' ')):
            second_equation.remove(' ')
        i=0
        """
        It looks at the amount of x and y and makes a list of them, for example,
        from "2x + 3y" it will make a list[2,3]. He does so in both equations
        """
        for x in first_equation:
            if repeat is True:
                repeat = False
                i=i+1
                continue

            if x=='-':
                if first_equation[i+1].isdigit() is True:
                    first.append(float(first_equation[i+1])*-1)
                    i=i+1
                    repeat=True
                    continue
                if first_equation[i+1] == "x" or first_equation[i+1] == "y":
                    first.append(-1)
                    repeat=True
                    i=i+1
                    continue
            if x.isdigit() is True and first_equation[i+1]=="*":
                first.append(float(x))
            if x=="*" or x=="/":
                repeat=True
            if x == "x" or x=="y":
                try:
                    if first_equation[i+1]=='/':
                        first.append(1/float(first_equation[i+2]))
                    else:
                        first.append(1)
                except:
                    first.append(1)
            i=i+1
        i=0
        repeat=False
        for x in second_equation:
            if repeat is True:
                repeat = False
                i=i+1
                continue

            if x=='-':
                if second_equation[i+1].isdigit() is True:
                    second.append(float(second_equation[i+1])*-1)
                    i=i+1
                    repeat=True
                    continue
                if second_equation[i+1] == "x" or second_equation[i+1] == "y":
                    second.append(-1)
                    repeat=True
                    i=i+1
                    continue
            if x.isdigit() is True and second_equation[i+1]=="*":
                second.append(float(x))
            if x=="*" or x=="/":
                repeat=True
            if x == "x" or x=="y":
                try:
                    if second_equation[i+1]=='/':
                        second.append(1/float(second_equation[i+2]))
                    else:
                        second.append(1)
                except:
                    second.append(1)
            i=i+1
        #Creates matrices
        list_y=[[first[0],result1[0]],[first[1],result2[0]]]
        list_x=[[result1[0],second[0]],[result2[0],second[1]]]
        list_w=[first,second]

        matrix1=np.array([first,second])
        matrix2=np.array([result1,result2])

        Wy=np.array(list_y)
        Wx=np.array(list_x)
        W=np.array(list_w)
        """
        He looks at the determinants of the three matrices.
        A matrix consisting o famount of x and y.
        A matrix consisting of the right side of both equations and the amount of y.
        A matrix consisting of the amount of x and the right side of both equations.
        If the value of these three determinants equals zero, this system is unmarked.
        If the second and third determinants are not equal to zero and
        the first equals 0 this system is contradictory.
        Otherwise, this system is marked and the inverse of the first matrix
        multiplies by the matrix created from the right sides of equations. A matrix
        that has been created consists of x and y values.
        """
        if np.linalg.det(W)==0 and np.linalg.det(Wy)==0 and np.linalg.det(Wx)==0:
            return("The system is unmarked")
        elif np.linalg.det(W)==0 and np.linalg.det(Wy)!=0 and np.linalg.det(Wx)!=0:
            return("The system is contradictory")
        else:
            final_result=inv(matrix1)@matrix2
        return("x="+str(final_result[0,0])+'\n'+"y="+str(final_result[1,0]))

class EquationSolver:
    """
    Initializes the parameters that must be entered to create the object.
    They are both sides of the equation
    """
    def __init__(self,left_side,right_side):
        self.a=left_side
        self.b=right_side

    def solve(self):
        #Ustala symbol niewiadomej
        x=sympy.symbols('x')
        #Sprawdza czy da się uprościć nawiasy
        try:
            #Uproszczenie nawiasów
            self.a=sympy.expand(self.a)
            self.b=sympy.expand(self.b)
        except:
            pass
        """
        Simplifies algebraic expression on both sides of the equation and
        removes empty characters from the string
        """
        try:
            self.a=str(sympy.sympify(self.a)).replace(' ','')
            self.b=str(sympy.sympify(self.b)).replace(' ','')
        except:
            self.a=str(sympy.sympify(self.a))
            self.b=str(sympy.sympify(self.b))

        #A function that checks whether a given part of the list is x
        def is_x(part_of_list):
            try:
                float(part_of_list)
                return False
            except:
                return True

        #Turns both sides of the equation into two lists
        list_a1=list(self.a)
        list_b1=list(self.b)

        #Creates empty lists
        list_a2=[]
        list_b2=[]

        list_a3=[]
        list_b3=[]

        c1=0
        c2=0
        x=0
        y=0
        """
        It combines numbers in a list, for example it converts ['1', '0'] to ['10']
         or combines the number of x, for example, converts ['2', '*', 'x'] to ['2 * x']
        """
        for new_a in list_a1:
            now=""
            if x >> 0:
                x=x-1
                c1=c1+1
                continue
            now=now+new_a
            if new_a.isdigit() is True:
                x=1
                while True:
                    try:
                        if list_a1[c1+x].isdigit() is True:
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]=="x":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]==".":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]=="*":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]=="/":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        x=x-1
                        break
                    except:
                        break
            if new_a == "x":
                x=1
                while True:
                    try:
                        if list_a1[c1+x].isdigit() is True:
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]==".":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]=="*":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        if list_a1[c1+x]=="/":
                            now=now+list_a1[c1+x]
                            x=x+1
                            continue
                        x=x-1
                        break
                    except:
                        break

            list_a2.append(now)
            c1=c1+1

        for new_b in list_b1:
            now=""
            if y >> 0:
                y=y-1
                c2=c2+1
                continue
            now=now+new_b
            if new_b.isdigit() is True:
                y=1
                while True:
                    try:
                        if list_b1[c2+y].isdigit() is True:
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]=="x":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]==".":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]=="*":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]=="/":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        y=y-1
                        break
                    except:
                        break
            if new_b == "x":
                y=1
                while True:
                    try:
                        if list_b1[c2+y].isdigit() is True:
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]==".":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]=="*":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        if list_b1[c2+y]=="/":
                            now=now+list_b1[c2+y]
                            y=y+1
                            continue
                        y=y-1
                        break
                    except:
                        break
            list_b2.append(now)
            c2=c2+1

        c1=0
        c2=0
        x=0
        y=0
        wait=False
        """
        Moves x to the left side of the equation and numbers to the right side
        """
        for final_a in list_a2:

            if wait is True:
                wait=False
                c1=c1+1
                continue

            if final_a =="-":
                if is_x(list_a2[c1+1]) is True:
                    list_a3.append("-")
                    list_a3.append(list_a2[c1+1])
                    wait=True
                if is_x(list_a2[c1+1]) is False:
                    list_b3.append("+")
                    list_b3.append(list_a2[c1+1])
                    wait=True
                c1=c1+1
                continue

            if final_a == "+":
                if is_x(list_a2[c1+1]) is True:
                    list_a3.append("+")
                    list_a3.append(list_a2[c1+1])
                    wait=True
                if is_x(list_a2[c1+1]) is False:
                    list_b3.append("-")
                    list_b3.append(list_a2[c1+1])
                    wait=True
                c1=c1+1
                continue

            if c1==0:
                if is_x(list_a2[c1]) is True:
                    list_a3.append("+")
                    list_a3.append(list_a2[c1])
                if is_x(list_a2[c1]) is False:
                    list_b3.append("-")
                    list_b3.append(list_a2[c1])
            c1=c1+1

        wait=False

        for final_b in list_b2:

            if wait is True:
                wait=False
                c2=c2+1
                continue

            if final_b =="-":
                if is_x(list_b2[c2+1]) is True:
                    list_a3.append("+")
                    list_a3.append(list_b2[c2+1])
                    wait=True
                if is_x(list_b2[c2+1]) is False:
                    list_b3.append("-")
                    list_b3.append(list_b2[c2+1])
                    wait=True
                c2=c2+1
                continue

            if final_b == "+":
                if is_x(list_b2[c2+1]) is True:
                    list_a3.append("-")
                    list_a3.append(list_b2[c2+1])
                    wait=True
                if is_x(list_b2[c2+1]) is False:
                    list_b3.append("+")
                    list_b3.append(list_b2[c2+1])
                    wait=True
                c2=c2+1
                continue

            if c2==0:
                if is_x(list_b2[c2]) is True:
                    list_a3.append("-")
                    list_a3.append(list_b2[c2])
                if is_x(list_b2[c2]) is False:
                    list_b3.append("+")
                    list_b3.append(list_b2[c2])

            c2=c2+1

        #Adds 0 to the list that is the right side of the equation if it is empty
        if not list_b3:
            list_b3.append('0')

        #Simplifies both sides of the equation
        left_first=str(sympy.sympify(''.join(list_a3)))
        right_first=str(sympy.sympify(''.join(list_b3)))

        #Converts the left sied to the list and the right one to the float
        right_first=float(right_first)
        left_first=list(left_first)

        c1=0
        x=0
        left_second=[]
        #Combines numbers in a list, for example, it converts ['2', '0', '*', 'x'] to ['20', '*', 'x']
        for final in left_first:
            now=""
            if x >> 0:
                x=x-1
                c1=c1+1
                continue
            now=now+final
            if final.isdigit() is True:
                x=1
                while True:
                    try:
                        if left_first[c1+x].isdigit() is True:
                            now=now+left_first[c1+x]
                            x=x+1
                            continue
                        if left_first[c1+x]==".":
                            now=now+left_first[c1+x]
                            x=x+1
                            continue
                        x=x-1
                        break
                    except:
                        break
            left_second.append(now)
            c1=c1+1
        """
        If x cancels out then program checks whether both sides of the equation are equal.
        if they are this equation is indeterminate, if they are not equal,
        then the equation is contradictory
        """
        if not left_second or left_second[0]=='0':
            if right_first > 0:
                return("This is a\ncontradictory equation")
            if right_first == 0:
                return("This is an \n indeterminate equation")
        else:
            c1=0
            """
            Multiplies both sides of the equation so that only one x remains on the left
            side and it gives it its value. Unless there is an inverse of x on the left side,
            which is multiplied by some number, then it multiplies both sides so that there is
            only an inverse of x on the left side, then it inverts the result so that the result is x
            """
            for result in left_second:
                if is_x(result) is False:
                    if left_second[c1+1] == "/":
                         right_first=1/(right_first*(1/float(result)))
                         break
                    if left_second[c1+1] == "*":
                         right_first=right_first/float(result)
                         break
                if result == "x":
                    try:
                        if left_second[c1+1] == "/":
                            right_first=right_first*float(left_second[c1+2])
                            break
                        if left_second[c1+1] == "*":
                            right_first=right_first/float(left_second[c1+2])
                            break
                    except:
                        break
                c1=c1+1
            #Checks whether the result is -x
            is_minus=False
            for minus in left_second:
                if minus == "-":
                    is_minus=True
            #If it is false it returns result
            if is_minus is False:
                return("x="+str(right_first))
            #If it is true it returns result multiplied by -1
            if is_minus is True:
                return("x="+str(right_first * -1))
