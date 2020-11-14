class estudante:
    def getnome(self):
        return self.nome

    def setnome(self,nome):
        self.nome = nome

    def gettia(self):
        return self.tia

    def settia(self,tia):
        self.tia = tia

aluno = estudante()
print(type(aluno))

aluno.setnome('Igor')
aluno.settia('42021723')

print(aluno.getnome())
print(aluno.gettia())

class boletim:
    def getestudante(self):
        return self.estudante
    def setestudante(self,estudante):
        self.estudante = estudante

    def getdisciplina(self):
        return self.disciplina
    def setdisciplina(self,disciplina):
        self.disciplina = disciplina

    def getnota(self):
        return self.nota
    def setnota(self,nota):
        self.nota = nota

    boletim = boletim()
    print(type(boletim))

    aluno.setnome('Igor')
    aluno.settia('42021723')
    boletim.setnota('10')

    print(aluno.getnome())
    print(aluno.gettia())
    print((boletim.setnota()))











