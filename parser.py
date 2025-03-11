class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def analisar(self):
        while self.pos < len(self.tokens):
            print(self.tokens[self.pos].__str__())
            self.comando()

    def comando(self):
        if self.tokens[self.pos].tipo == "palavras_reservadas":
            if self.tokens[self.pos].valor == "if":
                self.condicional()
            elif self.tokens[self.pos].valor == "while":
                self.repeticao()
            elif self.tokens[self.pos].tipo == "variavel" or self.tokens[self.pos].valor == "var":
                self.atribuicao()
        elif self.tokens[self.pos].tipo == "nova_linha":
            self.consumir("nova_linha")
        else:
            raise SyntaxError("Erro de sintaxe: comando inválido")

    def condicional(self):
        self.consumir("palavras_reservadas")  # confirma se recebe o if e passa para o próximo token
        self.expressao_if_while()
        self.consumir("nova_linha")  # quebra de linha obrigatória
        self.bloco()

    def repeticao(self):
        self.consumir("palavras_reservadas")  # while
        self.expressao_if_while()
        self.consumir("nova_linha")  # quebra de linha obrigatória
        self.bloco()

    def bloco(self):
        while self.pos < len(self.tokens) and self.tokens[self.pos].tipo != "nova_linha":
            self.comando()

    def atribuicao(self):
        if self.tokens[self.pos].valor == "var" and self.tokens[self.pos].tipo == "palavras_reservadas":
            self.consumir("palavras_reservadas")

        self.consumir("variavel")
        self.consumir("operador_definicao")
        self.expressao()

    def expressao(self):
        self.termo()
        while self.pos < len(self.tokens) and self.tokens[self.pos].tipo == "operador":
            self.consumir("operador")
            self.termo()

    def expressao_if_while(self):
        self.termo()
        while self.pos < len(self.tokens) and (self.tokens[self.pos].tipo == "operador_logico" or
                                               self.tokens[self.pos].tipo == "operador_relacionais"):
            self.consumir_if_while()
            self.termo()

    def termo(self):
        if self.tokens[self.pos].tipo in ("numero", "variavel"):
            self.consumir(self.tokens[self.pos].tipo)
        else:
            raise SyntaxError("Erro de sintaxe: termo inválido")

    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos].tipo == tipo_esperado:
            self.pos += 1
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {tipo_esperado}, encontrado {self.tokens[self.pos].tipo}")

    def consumir_if_while(self):
        tipo_esperado = ("operador_logico", "operador_relacionais")
        if self.pos < len(self.tokens) and self.tokens[self.pos].tipo in tipo_esperado:
            self.pos += 1
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {tipo_esperado}, encontrado {self.tokens[self.pos].tipo}")
