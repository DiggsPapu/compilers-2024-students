from Stack import Stack
# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):
        
    def __init__(self):
        self.lastOp = None
        self.right = None
        self.left = None
        self.result = None
        self.stackOperation = Stack()
        self.stackNum = Stack()
        self.head = None
        self.value = None
        self.assigned = {}
        self.comparison = None
        self.string = None
    
    # Enter a parse tree produced by MiniLangParser#prog.
    def enterProg(self, ctx:MiniLangParser.ProgContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by MiniLangParser#prog.
    def exitProg(self, ctx:MiniLangParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printExpr.
    def enterPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by MiniLangParser#printExpr.
    def exitPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        self.right = None
        self.left = None
        self.result = None
        self.lastOp = self.stackOperation.pop()
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                # Asignacion
                if self.lastOp == 0:
                    print(self.assigned[self.head]," assigned in ",self.head)
                    self.head = None
                # Operaciones
                else:
                    print("Resultado: ", self.stackNum.pop())
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            # Asignacion
            if self.lastOp == 0:
                print(self.assigned[self.head]," assigned in ",self.head)
                command = f'global {self.head}\n{self.head}={self.assigned[self.head]}'
                # Create/update variables in the context
                exec(command)
                self.head = None
                self.lastOp = None
            elif self.stackOperation.stack.count(8)>0 or self.lastOp == 8:
                pass
            # Operaciones
            else:
                print("Resultado: ", self.stackNum.pop())
                self.lastOp = None
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        # Insert a assign operation -> 0
        self.stackOperation.push(0)
        self.head = ctx.getChild(0).getText()
        self.lastOp = 0
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                # En caso de que sea una operacion se asigna el valor de la operacion a la memoria 
                if self.lastOp != 0:
                    self.assigned[self.head] = self.stackNum.pop()
                # En caso de que solo sea una asignacion entonces se le asigna el valor a la memoria
                else:
                    self.assigned[self.head] = self.value
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            # En caso de que sea una operacion se asigna el valor de la operacion a la memoria 
            if self.lastOp != 0:
                self.assigned[self.head] = self.stackNum.pop()
            # En caso de que solo sea una asignacion entonces se le asigna el valor a la memoria
            else:
                self.assigned[self.head] = self.value
        self.lastOp = self.stackOperation.pop()
        print(self.assigned[self.head]," assigned in ",self.head)
        command = f'global {self.head} \n{self.head}={self.assigned[self.head]}'
            # Create/update variables in the context
        exec(command)
        self.value = None
        pass


    # Enter a parse tree produced by MiniLangParser#blank.
    def enterBlank(self, ctx:MiniLangParser.BlankContext):
        pass

    # Exit a parse tree produced by MiniLangParser#blank.
    def exitBlank(self, ctx:MiniLangParser.BlankContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparisonStmt.
    def enterComparisonStmt(self, ctx:MiniLangParser.ComparisonStmtContext):
        self.stackOperation.push(5)
        pass

    # Exit a parse tree produced by MiniLangParser#comparisonStmt.
    def exitComparisonStmt(self, ctx:MiniLangParser.ComparisonStmtContext):
        print(self.comparison)
        pass

    # Enter a parse tree produced by MiniLangParser#parens.
    def enterParens(self, ctx:MiniLangParser.ParensContext):
        pass

    # Exit a parse tree produced by MiniLangParser#parens.
    def exitParens(self, ctx:MiniLangParser.ParensContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv.
    def enterMulDiv(self, ctx:MiniLangParser.MulDivContext):
        if ctx.getChild(1).getText() == '*':
            self.stackOperation.push(3)
        elif ctx.getChild(1).getText() == '/':
            self.stackOperation.push(4)
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv.
    def exitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        self.lastOp = self.stackOperation.pop()
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                right = self.stackNum.pop()
                left = self.stackNum.pop()
                # operacion de salida del arbol
                if self.lastOp == 3:
                    self.stackNum.push( left * right )
                    
                elif self.lastOp == 4:
                    self.stackNum.push( left / right )
                print(self.stackNum.peek())
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            right = self.stackNum.pop()
            left = self.stackNum.pop()
            # operacion de salida del arbol
            if self.lastOp == 3:
                self.stackNum.push( left * right )
                
            elif self.lastOp == 4:
                self.stackNum.push( left / right )
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub.
    def enterAddSub(self, ctx:MiniLangParser.AddSubContext):
        if ctx.getChild(1).getText() == '+':
            self.stackOperation.push(1)
        elif ctx.getChild(1).getText() == '-':
            self.stackOperation.push(2)
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub.
    def exitAddSub(self, ctx:MiniLangParser.AddSubContext):
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                right = self.stackNum.pop()
                left = self.stackNum.pop()
                # operacion de salida del arbol
                if self.lastOp == 1:
                    self.stackNum.push( left + right )
                    
                elif self.lastOp == 2:
                    self.stackNum.push( left - right )
                print(self.stackNum.peek())
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            right = self.stackNum.pop()
            left = self.stackNum.pop()
            # operacion de salida del arbol
            self.lastOp = self.stackOperation.peek()
            if self.lastOp == 1:
                self.stackNum.push( left + right )
                
            elif self.lastOp == 2:
                self.stackNum.push( left - right )
        pass


    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                # Esta en una operacion
                if (len(self.stackOperation.stack)>0):
                    # En caso de que sea una operacion hay que ir a buscar a memoria para ver las variables
                    if self.stackOperation.peek() != 0:
                        # Si no se encuentra la variable entonces se lanza error
                        self.stackNum.push(self.assigned[ctx.getText()])
                    # En caso de que sea una asignacion
                    else:
                        # Si es el nombre de la variable
                        if self.head == None:
                            self.head = ctx.getText()
                        else:
                            self.value = ctx.getText()
                # es un valor ya definido
                else:
                    try:
                        variable = ctx.getText()
                        self.assigned[variable]
                        print("Variable value: ",self.assigned[variable])
                    except:
                        raise Exception(f"The variable {variable} is not defined")
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            # Esta en una operacion
            if (len(self.stackOperation.stack)>0):
                # En caso de que sea una operacion hay que ir a buscar a memoria para ver las variables
                if self.stackOperation.peek() != 0:
                    # Si no se encuentra la variable entonces se lanza error
                    self.stackNum.push(self.assigned[ctx.getText()])
                # En caso de que sea una asignacion
                else:
                    # Si es el nombre de la variable
                    if self.head == None:
                        self.head = ctx.getText()
                    else:
                        self.value = ctx.getText()
            # es un valor ya definido
            else:
                try:
                    variable = ctx.getText()
                    self.assigned[variable]
                    print("Variable value: ",self.assigned[variable])
                except:
                    raise Exception(f"The variable {variable} is not defined")
        pass

    # Exit a parse tree produced by MiniLangParser#id.
    def exitId(self, ctx:MiniLangParser.IdContext):
        pass


    # Enter a parse tree produced by MiniLangParser#int.
    def enterInt(self, ctx:MiniLangParser.IntContext):
        if (self.stackOperation.stack.count(6)>0 or self.stackOperation.stack.count(7))>0:
            if (self.comparison):
                # Si solo es una asignacion entonces solo se asigna al valor
                if self.stackOperation.peek() == 0:
                    self.value = int(ctx.getText())
                # Si es una operacion se va a poner en el stack de numeros para operar
                else:
                    self.stackNum.push(int(ctx.getText()))
        elif self.stackOperation.stack.count(8)>0:
            pass
        else:
            # Si solo es una asignacion entonces solo se asigna al valor
            if self.stackOperation.peek() == 0:
                self.value = int(ctx.getText())
            # Si es una operacion se va a poner en el stack de numeros para operar
            else:
                self.stackNum.push(int(ctx.getText()))
        pass

    # Exit a parse tree produced by MiniLangParser#int.
    def exitInt(self, ctx:MiniLangParser.IntContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comment.
    def enterComment(self, ctx:MiniLangParser.CommentContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comment.
    def exitComment(self, ctx:MiniLangParser.CommentContext):
        pass

    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
        pass
    
    # Enter a parse tree produced by MiniLangParser#comparation.
    def enterComparation(self, ctx:MiniLangParser.ComparationContext):
        for variable in list(self.assigned.keys()):
            command = f'global {variable}\n{variable}={self.assigned[variable]}'
            # Create/update variables in the context
            exec(command)
        self.comparison = exec(ctx.getText())
        pass

    # Exit a parse tree produced by MiniLangParser#comparation.
    def exitComparation(self, ctx:MiniLangParser.ComparationContext):
        pass
    
        # Enter a parse tree produced by MiniLangParser#condStmt.
    def enterCondStmt(self, ctx:MiniLangParser.CondStmtContext):
        # Indica que tipo de statement es if o while
        if ctx.getChild(0).getChild(0).getText()=="if":
            self.stackOperation.push(6)
        else:
            self.stackOperation.push(7)
            text = ctx.getText()
            values = text.split(':')
            text = values[0]+':\n'
            for index in range(1, len(values)):
                text+=f' {values[index]}\n'
            funName = ctx.getChild(1)
            exec(f'global {funName}')
            exec(text)
        pass

    # Exit a parse tree produced by MiniLangParser#condStmt.
    def exitCondStmt(self, ctx:MiniLangParser.CondStmtContext):
        # En caso de que sea un while entonces hay que ejecutario muchas veces.
        operation = self.stackOperation.pop()
        pass
    
    # Enter a parse tree produced by MiniLangParser#stmt.
    def enterStmt(self, ctx:MiniLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stmt.
    def exitStmt(self, ctx:MiniLangParser.StmtContext):
        pass
    
    # Enter a parse tree produced by MiniLangParser#defunStmt.
    def enterDefunStmt(self, ctx:MiniLangParser.DefunStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#defunStmt.
    def exitDefunStmt(self, ctx:MiniLangParser.DefunStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#funStmt.
    def enterFunStmt(self, ctx:MiniLangParser.FunStmtContext):
        value = ctx.getText()
        pass

    # Exit a parse tree produced by MiniLangParser#funStmt.
    def exitFunStmt(self, ctx:MiniLangParser.FunStmtContext):
        pass
# Enter a parse tree produced by MiniLangParser#defFun.
    def enterDefFun(self, ctx:MiniLangParser.DefFunContext):
        st = ctx.getText()[3:]
        st = st.split(":")
        name = st[0][0:st[0].index('(')]
        statement = f'global {name}\ndef {st[0]}:\n    {st[1]}'
        exec(statement)
        self.stackOperation.push(8)
        pass

    # Exit a parse tree produced by MiniLangParser#defFun.
    def exitDefFun(self, ctx:MiniLangParser.DefFunContext):
        pass


    # Enter a parse tree produced by MiniLangParser#fun.
    def enterFun(self, ctx:MiniLangParser.FunContext):
        print(f"executed: {ctx.getText()}")
        exec(ctx.getText())
        pass

    # Exit a parse tree produced by MiniLangParser#fun.
    def exitFun(self, ctx:MiniLangParser.FunContext):
        pass
    
    # Enter a parse tree produced by MiniLangParser#strExp.
    def enterStrExp(self, ctx:MiniLangParser.StrExpContext):
        self.stackNum.push(ctx.getText().replace("\"",""))
        pass

    # Exit a parse tree produced by MiniLangParser#strExp.
    def exitStrExp(self, ctx:MiniLangParser.StrExpContext):
        pass
    
    # Enter a parse tree produced by MiniLangParser#string.
    def enterString(self, ctx:MiniLangParser.StringContext):
        pass

    # Exit a parse tree produced by MiniLangParser#string.
    def exitString(self, ctx:MiniLangParser.StringContext):
        pass
del MiniLangParser