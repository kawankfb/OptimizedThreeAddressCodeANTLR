"""
Example of three address code generator with listener

"""

__version__ = '0.1.0'
__author__ = 'Morteza'

from gen.Expr2Parser import Expr2Parser
from gen.Expr2Listener import Expr2Listener


class ThreeAddressCode(Expr2Listener):
    """
        Generate three address code for part of expression rule of CPP14 grammar
    """

    def __init__(self):
        self.temp_counter = 0
        # self.value = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    # Rule: #fact1
    def exitFact1(self, ctx: Expr2Parser.Fact1Context):
        ctx.code = ctx.getText()

    def exitFact2(self, ctx: Expr2Parser.Fact2Context):
        ctx.code = ctx.getText()

    def exitFact3(self, ctx: Expr2Parser.Fact3Context):
        ctx.code = ctx.expr().code

    def exitTerm1(self, ctx: Expr2Parser.Term1Context):
        if str.startswith(ctx.term().code,"T"):
            print(ctx.term().code, '=', ctx.term().code, '*', ctx.fact().code)
            ctx.code = ctx.term().code
        else:
            temp = self.create_temp()
            print(temp, '=', ctx.term().code, '*', ctx.fact().code)
            ctx.code = temp

    def exitTerm2(self, ctx: Expr2Parser.Term2Context):
        if str.startswith(ctx.term().code, "T"):
            print(ctx.term().code, '=', ctx.term().code, '/', ctx.fact().code)
            ctx.code = ctx.term().code
        else:
            temp = self.create_temp()
            print(temp, '=', ctx.term().code, '/', ctx.fact().code)
            ctx.code = temp

    def exitTerm3(self, ctx: Expr2Parser.Term3Context):
        ctx.code = ctx.fact().code

    def exitExpr1(self, ctx: Expr2Parser.Expr1Context):
        if str.startswith(ctx.expr().code, "T"):
            print(ctx.expr().code, '=', ctx.expr().code, '+', ctx.term().code)
            ctx.code = ctx.expr().code
        else:
            temp = self.create_temp()
            print(temp, '=', ctx.expr().code, '+', ctx.term().code)
            ctx.code = temp


    def exitExpr2(self, ctx: Expr2Parser.Expr2Context):
        if str.startswith(ctx.expr().code, "T"):
            print(ctx.expr().code, '=', ctx.expr().code, '-', ctx.term().code)
            ctx.code = ctx.expr().code
        else:
            temp = self.create_temp()
            print(temp, '=', ctx.expr().code, '-', ctx.term().code)
            ctx.code = temp

    def exitExpr3(self, ctx: Expr2Parser.Expr3Context):
        ctx.code = ctx.term().code

    def exitStart(self, ctx: Expr2Parser.StartContext):
        # pass
        print(ctx.Id(), '=', ctx.expr().code)
        # print(ctx.Id(), '=', self.value)
