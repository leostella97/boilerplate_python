# Classe exemplo
class MinhaClasse:
    """
    Essa é uma classe de exemplo que ilustra a estrutura básica de uma classe em Python.
    """

    def __init__(self, parametro1, parametro2):
        """
        Método construtor da classe. Recebe dois parâmetros e os atribui às variáveis de instância.
        """
        self.parametro1 = parametro1
        self.parametro2 = parametro2

    def metodo1(self):
        """
        Exemplo de um método da classe.
        """
        # Realize alguma operação aqui
        print("Método 1 sendo executado.")

    def metodo2(self):
        """
        Exemplo de outro método da classe.
        """
        # Realize alguma operação aqui
        print("Método 2 sendo executado.")


# Código principal
if __name__ == "__main__":
    # Cria uma instância da classe MinhaClasse
    minha_instancia = MinhaClasse("valor1", "valor2")

    # Chama os métodos da instância
    minha_instancia.metodo1()
    minha_instancia.metodo2()
