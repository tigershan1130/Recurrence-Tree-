# Recursion Tree Method 
# Accepting Divide-and-Conquer: T(n) = aT(n/b) + f(n)
# where a is an integer such that a >= 1
# where b > 1, and b is a rational number
# Accepting Chip-and-Be-Conquered: T(n) = aT(n-b) + f(n)
# a is an integer bigger or equal to 1
# b is greater than 0 and b is also an integer
# 
# f(n) must be accept in two forms: Polynomial and Logarithmic
# Polynomial: cn^d
# Logarithmic: clog based e to the d of n 
# where c is a rational number
# where d is a rational number
# where e is a rational number

import tkinter as tk
import TreeStructure as ts
import TsRationalNumber as rn

class RecursionTreeUIAPP():
    
    def __init__(self, master):        
        
        self.recurrenceType = tk.IntVar()
        self.fnType = tk.IntVar()
        self.labelC = tk.StringVar()
        self.labelD = tk.StringVar()
        self.labelE = tk.StringVar()
        self.warning = tk.StringVar()
        self.master = master

        tk.Radiobutton(master, text='Divide-And-Conquer', variable= self.recurrenceType, value = 1, command =self.CheckRecurrenceTreeValues).grid(column = 0, row = 0)
        tk.Radiobutton(master, text= 'Chip-And-Be-Conquered', variable = self.recurrenceType, value =2, command =self.CheckRecurrenceTreeValues).grid(column = 0, row = 1)   

        tk.Radiobutton(master, text='f(n) Type: Polynomial', variable = self.fnType, value = 1, command = self.DisplayInputForFn).grid(column = 1, row = 0)
        tk.Radiobutton(master, text='f(n) Type: Logarithmic', variable = self.fnType, value = 2, command = self.DisplayInputForFn).grid(column = 1, row = 1) 


        self.labelA = tk.Label(self.master, text ="Enter Integer a(>=1): ")
        self.labelB = tk.Label(self.master, text ="Enter Integer for b(>0):")
        self.fieldA = tk.Entry(self.master)
        self.fieldB = tk.Entry(self.master)
        self.labelA.grid(row =2, column = 0)
        self.labelB.grid(row =3, column = 0)
        self.fieldA.grid(row = 2, column = 1)
        self.fieldB.grid(row = 3, column = 1)

        self.recurrenceType.set(1)
        self.CheckRecurrenceTreeValues()

        self.labelCObj = tk.Label(self.master, textvariable = self.labelC)
        self.labelDObj = tk.Label(self.master, textvariable = self.labelD)
        self.labelEObj = tk.Label(self.master, textvariable = self.labelE)
        self.fieldC = tk.Entry(self.master)
        self.fieldD = tk.Entry(self.master)
        self.fieldE = tk.Entry(self.master)

        self.labelCObj.grid(row = 4, column = 0)
        self.labelDObj.grid(row = 5, column = 0)
        self.labelEObj.grid(row = 6, column = 0)
        self.fieldC.grid(row = 4, column = 1)
        self.fieldD.grid(row = 5, column = 1)
        self.fieldE.grid(row = 6, column = 1)

        self.fnType.set(1)        
        self.DisplayInputForFn()
        
        tk.Label(self.master,textvariable = self.warning).grid(column = 0, row = 7)
        tk.Button(self.master, text ='Calculate Recurrence', command= self.CheckValidation).grid(column = 1, row = 7)

    def CheckRecurrenceTreeValues(self):
        print(self.recurrenceType.get())
        if (self.recurrenceType.get() == 1):
            print("Choosed recurrenceType 1")
        elif(self.recurrenceType.get() == 2): 
            print("Choosed recurrenceType 2")    
        else:
            print("Error in Recurrence type")

    def DisplayInputForFn(self):

        if(self.fnType.get() == 2):            
            if not (self.labelEObj.winfo_exists()):
                self.labelEObj = tk.Label(self.master, textvariable = self.labelE)

            if not (self.fieldE.winfo_exists()):
                self.fieldE = tk.Entry(self.master)

            self.labelCObj.grid(row = 4, column = 0)
            self.labelDObj.grid(row = 5, column = 0)
            self.labelEObj.grid(row = 6, column = 0)
            self.fieldC.grid(row = 4, column = 1)
            self.fieldD.grid(row = 5, column = 1)
            self.fieldE.grid(row = 6, column = 1)

            self.labelC.set("Enter Constant C(RationalNumber): ")
            self.labelD.set("Enter n^(Power of) D(Rational Number): ")
            self.labelE.set("Enter log base of E(Rational Number): ")
           
        elif(self.fnType.get() ==1):            

            self.labelCObj.grid(row = 4, column = 0)
            self.labelDObj.grid(row = 5, column = 0)
            self.fieldC.grid(row = 4, column = 1)
            self.fieldD.grid(row = 5, column = 1)
            
            self.labelC.set("Enter Constant C(RationalNumber): ")
            self.labelD.set("Enter n^(Power of) D(Rational Number): ")
           
            if(self.labelEObj.winfo_exists()):
                self.labelEObj.destroy()
            if(self.fieldE.winfo_exists()):
                self.fieldE.destroy()

        else:
            print("Invalid Type")


    def CheckValidation(self):
        print("check for all inputs if they are valid")

        integerA = 0
        integerB = 0
        rationalC = 0
        rationalD = 0
        rationalE = 0

        try:
            integerA = int(self.fieldA.get())
            integerB = int(self.fieldB.get())
            rationalC = float(self.fieldC.get())
            rationalD = float(self.fieldD.get())

            if(self.fieldE.winfo_exists()):
                rationalE = float(self.fieldE.get())
            
        except ValueError:
            self.warning.set("Error in value input")
            return

        if(integerA < 1):
            self.warning.set("invalid a")
            return
        
        if(integerB <= 0):
            self.warning.set("invalid b")
            return

        if(rationalC <= 0):
            self.warning.set("invalid c")
            return
        
        if(rationalD <= 0):
            self.warning.set("invalid d")
            return

        if(rationalE <= 0 and self.fnType == 2):
            self.warning.set("invalid e")
            return 

        # initialize our tree structure.
        self.tree = ts.TsTree(None, [1])    

        if(self.recurrenceType.get() == 1):
            self.CalculateRecurrenceDAC(3, self.tree, integerA, integerB)
        elif(self.recurrenceType.get() == 2):
            self.CalculateRecurrenceCABC(3, self.tree, integerA, integerB)

        DebugDict= {}
        self.tree.PushTreeDataToHash(DebugDict)

        # print(DebugDict)

        for key in DebugDict:

            sum = rn.TsRationalNumber(0,1) # 0/1
            data = DebugDict[key]

            for i in range (len(data)):
                #print(data[i][0])
                rationalNumber =  rn.TsRationalNumber(1, data[i][0])
                #print(rationalNumber.__str__())
                sum = sum + rationalNumber

            rationalSum = sum.__str__() 
            print(f'depth at {key} total cost is: {rationalSum}, {data}')
            
        return

    # for divide and conquer
    def CalculateRecurrenceDAC(self, maxDepth, tree, a, b):
        # print("calcuate divide and conquer recurrence tree: " , a, " ", b, " ", maxDepth)

        # a is the subdivision of n
        # b is the divisor of n, how many times do we split n

        if(maxDepth <= 0):
            return tree

        # let's do subdivision
        # each tree should have a number of subdivision, so iterate loop for that amount
        i = 0
            
        newSubdivision = tree.data[0] * b

        # keep going on depth
        while(i < a):
        
            childTree = tree.AddChildren([newSubdivision])
            self.CalculateRecurrenceDAC(maxDepth-1, childTree, a, b)    
            i = i+1

        return

    def CalculateRecurrenceCABC(self, maxDepth, tree, a, b):
        print("calculate chip and be conqured recurrence tree")

# ================== main app execution ====================
main = tk.Tk()
main.title('Recursion Tree Setup')
main.geometry('500x300')

app = RecursionTreeUIAPP(main)

main.mainloop()


