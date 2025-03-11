class Nodo:
    def print_ast(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent}{self.__class__.__name__}: {vars(self) if vars(self) else ''}")

        for atributo in vars(self).values():
            if isinstance(atributo, Nodo):
                atributo.print_ast(nivel + 1)
            elif isinstance(atributo, list):
                for item in atributo:
                    if isinstance(item, Nodo):
                        item.print_ast(nivel + 1)


class Programa(Nodo):
    def __init__(self, comandos):
        self.comandos = comandos  # Lista de comandos

    def __str__(self):
        return f'{self.comandos}'


class Atribuicao(Nodo):
    def __init__(self, variavel, expressao):
        self.variavel = variavel
        self.expressao = expressao

    def __str__(self):
        return f"{self.variavel} {self.expressao}"


class If(Nodo):
    def __init__(self, condicao, corpo):
        self.condicao = condicao
        self.corpo = corpo

    def __str__(self):
        return f"{self.condicao} {self.corpo}"


class While(Nodo):
    def __init__(self, condicao, corpo):
        self.condicao = condicao
        self.corpo = corpo

    def __str__(self):
        return f"{self.condicao} {self.corpo}"


class OperacaoBinaria(Nodo):
    def __init__(self, esquerda, operador, direita):
        self.esquerda = esquerda
        self.operador = operador
        self.direita = direita

    def __str__(self):
        return f"{self.operador} {self.direita} {self.esquerda}"
    
class OperacaoLogica(Nodo):
    def __init__(self, esquerda, operador, direita):
        self.esquerda = esquerda
        self.operador = operador
        self.direita = direita

    def __str__(self):
        return f"{self.operador} {self.direita} {self.esquerda}"


class Variavel(Nodo):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"


class Numero(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"{self.valor}"

class Literal(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"{self.valor}"
