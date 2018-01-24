#Imports the class to solve linear equations
from BackEnd import EquationSolver
#Imports the class to solve system of linear equations
from BackEnd import SystemOfEquationSolver

#Imports the TKinter library
from tkinter import *

def equation_title():
    #Removes the first window
    window1.destroy()
    #Globalizes window1 variable to be able to close it with another function
    global window2
    #Opens the window
    window2=Tk()
    #Sets window title to empty, because the title is visible in the window
    window2.title('')
    #Sets the size of the window
    window2.geometry('350x200')

    def execute():
        #Creates an object and enters parameters that are two sides of the equation
        solver=EquationSolver(left.get(),right.get())
        #Changes the variable X to the output of the solve function
        X.configure(text=solver.solve())
        #Clears text widgets
        left_side.delete(0,END)
        right_side.delete(0,END)

    #Creates the title label
    title=Label(text="Single Linear\nEquation",font=("Phosphate Inline", 32))
    title.grid(row=0,column=0,columnspan=3)

    #Creates a button that allows you to go back to the first window
    back=Button(text="Main Menu",command=title_screen)
    back.grid(row=4,column=0,sticky='W')

    #Creates text widget
    left=StringVar()
    left_side=Entry(width=15,textvariable=left)
    left_side.grid(row=1,column=0)

    #Creates label
    equal=Label(text='=')
    equal.grid(row=1,column=1,sticky='W')

    #Creates text widget
    right=StringVar()
    right_side=Entry(width=15,textvariable=right)
    right_side.grid(row=1,column=2)

    #Creates a button that activates the "execute" function and solves the equation
    executor=Button(text='Solve',command=execute)
    executor.grid(row=2,column=0,columnspan=3)

    #Creates label
    X=Label(text='x=',font=("Marker Felt Wide", 20))
    X.grid(row=3,column=0,sticky='W',columnspan=3)

    window2.mainloop()

def SystemOfEquations_title():
    #Closes the previous window
    window1.destroy()
    #Globalizes the window3 variable to be able to close it with another function
    global window3
    #Opens window
    window3=Tk()
    #Sets the window title to empty, because the title is visible in the window
    window3.title('')
    #Sets the size of the window
    window3.geometry('350x280')

    def execute():
        #Globalizes the window2 variable to be able to close it with another function
        solver=SystemOfEquationSolver(left1.get(),right1.get(),left2.get(),right2.get())
        #Changes the variable XY to the output of the solve function
        XY.configure(text=solver.solve())

        #Clears widgets

        left_side1.delete(0,END)
        right_side1.delete(0,END)

        left_side2.delete(0,END)
        right_side2.delete(0,END)
    #Creates a title label
    title=Label(text="System of \nLinear Equations",font=("Phosphate Inline", 32))
    title.grid(row=0,column=0,columnspan=3)

    #Creates a button that allows you to go back to the first window
    back=Button(text="Main Menu",command=title_screen)
    back.grid(row=5,column=0,sticky='W')

    #Creates a widgets and labels that allows you to enter equations
    left1=StringVar()
    left_side1=Entry(width=15,textvariable=left1)
    left_side1.grid(row=1,column=0)

    equal1=Label(text='=')
    equal1.grid(row=1,column=1,sticky='W')

    right1=StringVar()
    right_side1=Entry(width=15,textvariable=right1)
    right_side1.grid(row=1,column=2)

    left2=StringVar()
    left_side2=Entry(width=15,textvariable=left2)
    left_side2.grid(row=2,column=0)

    equal2=Label(text='=')
    equal2.grid(row=2,column=1,sticky='W')

    right2=StringVar()
    right_side2=Entry(width=15,textvariable=right2)
    right_side2.grid(row=2,column=2)

    #Creates a button that activates the "execute" function and solves the system of equations
    executor=Button(text='Solve',command=execute)
    executor.grid(row=3,column=0,columnspan=3)

    #Creates a label
    XY=Label(text='x=\ny=',font=("Marker Felt Wide", 20))
    XY.grid(row=4,column=0,sticky='W',columnspan=3)


    window3.mainloop()


def title_screen():
    #Closes previous windows that may have been opened
    try:
        window2.destroy()
    except:
        pass
    try:
        window3.destroy()
    except:
        pass
    #Globalizes the window1 variable to be able to close it with another function
    global window1
    #Opens the window
    window1=Tk()
    #Sets the window title to empty, because the title is visible in the window
    window1.title('')
    #Sets the size of the window
    window1.geometry('350x200')

    #Creates a label that names the window and sets its parameters
    title=Label(text="Equation Solver",font=("Phosphate Inline", 32)).pack()
    """
     Creates a button that takes the user to the window
     solving linear equations and sets its parameters
     """
    first_option=Button(text="Single Linear Equation",
    height = 3, width = 20, font=("Marker Felt Wide", 20),command=equation_title).pack()
    """
    Creates a button that takes the user to the window
    solving system of linear equations and sets its parameters
    """
    second_option=Button(text="System of Linear Equations",
    height = 3, width = 20,font=("Marker Felt Wide", 20),command=SystemOfEquations_title).pack()

    window1.mainloop()
title_screen()
