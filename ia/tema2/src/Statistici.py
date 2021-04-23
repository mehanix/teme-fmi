import statistics
import time
class Statistici:
    timpiGandirePc = []
    timpiGandireUser = []
    nrNoduriGenerate = []
    nrMutariJMIN = 0
    nrMutariJMAX = 0
    timpStartJoc = 0

    @classmethod
    def showFinalStats(cls):
        timpEndJoc = time.time()
        print()
        print("Statistici joc")
        print("========================")
        print("Timp gandire calculator:")
        print(f"Timp minim: {min(cls.timpiGandirePc)}ms")
        print(f"Timp maxim: {max(cls.timpiGandirePc)}ms")
        print(f"Timp mediu: {round(statistics.mean(cls.timpiGandirePc))}ms")
        print(f"Mediana: {statistics.median(cls.timpiGandirePc)}ms")
        print("========================")
        print(f"Numar noduri generate: {sum(cls.nrNoduriGenerate)}")
        print(f"Numar minim generat/mutare: {min(cls.nrNoduriGenerate)}ms")
        print(f"Numar maxim generat/mutare: {max(cls.nrNoduriGenerate)}ms")
        print(f"Numar mediu generat/mutare: {round(statistics.mean(cls.nrNoduriGenerate))}ms")
        print(f"Mediana pe mutari: {statistics.median(cls.nrNoduriGenerate)}ms")
        print("========================")
        print("Durata joc: " + str(round(timpEndJoc - cls.timpStartJoc)) + " secunde")
        print(f"Numar mutari jucator:{cls.nrMutariJMIN}")
        print(f"Numar mutari calculator:{cls.nrMutariJMAX}")



