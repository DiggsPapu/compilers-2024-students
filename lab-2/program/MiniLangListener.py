from Stack import Stack
# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
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
        # Asignacion
        if self.lastOp == 0:
            print(self.assigned[self.head]," assigned in ",self.head)
            self.head = None
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
        # En caso de que sea una operacion se asigna el valor de la operacion a la memoria 
        if self.lastOp != 0:
            self.assigned[self.head] = self.stackNum.pop()
        # En caso de que solo sea una asignacion entonces se le asigna el valor a la memoria
        else:
            self.assigned[self.head] = self.value
        self.lastOp = self.stackOperation.pop()
        print(self.assigned[self.head]," assigned in ",self.head)
        self.value = None
        pass


    # Enter a parse tree produced by MiniLangParser#blank.
    def enterBlank(self, ctx:MiniLangParser.BlankContext):
        pass

    # Exit a parse tree produced by MiniLangParser#blank.
    def exitBlank(self, ctx:MiniLangParser.BlankContext):
        pass


    # Enter a parse tree produced by MiniLangParser#commentStmt.
    def enterCommentStmt(self, ctx:MiniLangParser.CommentStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#commentStmt.
    def exitCommentStmt(self, ctx:MiniLangParser.CommentStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparisonStmt.
    def enterComparisonStmt(self, ctx:MiniLangParser.ComparisonStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparisonStmt.
    def exitComparisonStmt(self, ctx:MiniLangParser.ComparisonStmtContext):
        print(self.comparison)
        pass


    # Enter a parse tree produced by MiniLangParser#defFunStmt.
    def enterDefFunStmt(self, ctx:MiniLangParser.DefFunStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#defFunStmt.
    def exitDefFunStmt(self, ctx:MiniLangParser.DefFunStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#callFunStmt.
    def enterCallFunStmt(self, ctx:MiniLangParser.CallFunStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#callFunStmt.
    def exitCallFunStmt(self, ctx:MiniLangParser.CallFunStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#stmt.
    def enterStmt(self, ctx:MiniLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stmt.
    def exitStmt(self, ctx:MiniLangParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#stringExpr.
    def enterStringExpr(self, ctx:MiniLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stringExpr.
    def exitStringExpr(self, ctx:MiniLangParser.StringExprContext):
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
        self.lastOp = self.stackOperation.pop()
        right = self.stackNum.pop()
        left = self.stackNum.pop()
        # operacion de salida del arbol
        if self.lastOp == 1:
            self.stackNum.push( left + right )
            
        elif self.lastOp == 2:
            self.stackNum.push( left - right )
        pass


    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
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


    # Enter a parse tree produced by MiniLangParser#comparison.
    def enterComparison(self, ctx:MiniLangParser.ComparisonContext):
        self.lastOp = self.stackOperation.push(5)
        pass

    # Exit a parse tree produced by MiniLangParser#comparison.
    def exitComparison(self, ctx:MiniLangParser.ComparisonContext):
        self.comparison = eval(ctx.getText())
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#defFunction.
    def enterDefFunction(self, ctx:MiniLangParser.DefFunctionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#defFunction.
    def exitDefFunction(self, ctx:MiniLangParser.DefFunctionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#callFunction.
    def enterCallFunction(self, ctx:MiniLangParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#callFunction.
    def exitCallFunction(self, ctx:MiniLangParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#string.
    def enterString(self, ctx:MiniLangParser.StringContext):
        pass

    # Exit a parse tree produced by MiniLangParser#string.
    def exitString(self, ctx:MiniLangParser.StringContext):
        self.string = ctx.getText()
        pass



del MiniLangParser