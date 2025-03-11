from ast import Programa, Atribuicao, Numero, If, While, Variavel, OperacaoBinaria, OperacaoLogica, Booleano, Literal


class Interpretador:
    def __init__(self):
        self.variaveis = {}

    def executar(self, nodo):
        if isinstance(nodo, Programa):
            for comando in nodo.comandos:
                self.executar(comando)

        elif isinstance(nodo, Atribuicao):
            self.variaveis[nodo.variavel.nome] = self.executar(nodo.expressao)

        elif isinstance(nodo, OperacaoBinaria):
            esquerda = self.executar(nodo.esquerda)
            direita = self.executar(nodo.direita)
            if nodo.operador == "+":
                return esquerda + direita
            elif nodo.operador == "-":
                return esquerda - direita
            elif nodo.operador == "*":
                return esquerda * direita
            elif nodo.operador == "/":
                return esquerda / direita

        elif isinstance(nodo, OperacaoLogica):
            esquerda = self.executar(nodo.esquerda)
            direita = self.executar(nodo.direita)
            if nodo.operador == ">":
                return esquerda > direita
            elif nodo.operador == "<":
                return esquerda < direita
            elif nodo.operador == ">=":
                return esquerda >= direita
            elif nodo.operador == "<=":
                return esquerda <= direita
            elif nodo.operador == "==":
                return esquerda == direita
            elif nodo.operador == "<>":
                return esquerda != direita
            elif nodo.operador == "AND":
                return esquerda and direita
            elif nodo.operador == "OR":
                return esquerda or direita

        elif isinstance(nodo, Numero):
            return nodo.valor

        elif isinstance(nodo, Booleano):
            return nodo.valor

        elif isinstance(nodo, Literal):
            return nodo.valor

        elif isinstance(nodo, Variavel):
            return self.variaveis.get(nodo.nome, 0)

        elif isinstance(nodo, If):
            if self.executar(nodo.condicao):
                self.executar(nodo.corpo)

        elif isinstance(nodo, While):
            while self.executar(nodo.condicao):
                self.executar(nodo.corpo)

        else:
            raise RuntimeError(f"Nó desconhecido: {nodo}")
