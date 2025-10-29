class Imprimivel:
    def imprimir(self):
        pass

class Exportavel:
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório sendo impresso...")
    
    def exportar(self):
        print("Relatório sendo exportado...")

relatorio = Relatorio()
relatorio.imprimir()
relatorio.exportar()