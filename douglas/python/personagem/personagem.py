class Mercs:
    def __init__(self, nome, time, tipo, vida):
        self.nome = nome
        self.time = time
        self.vida = vida
        self.tipo = tipo
        self.armas = []
        self.acessorio = []

    def add_item_acessorio(self, nome, efeito):
        item = {"nome": nome, "efeito": efeito}
        self.acessorio.append(item)

    def list_acessorio(self):
        if not self.acessorio:
            return "Sem acessórios"
        item = self.acessorio[0]
        return f"{item['nome']}: {item['efeito']}"

    def status(self):
        print("-" * 40)
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"Vida: {self.vida}")
        print("Armas", ", ".join(self.armas))
        print("Acessórios:\n")
        print(self.list_acessorio())
        print("-" * 40)

soldier = Mercs("Soldier", "Red", "Ataque", 200)
heavy = Mercs("Heavy", "Blue", "Defesa", 300)

heavy.armas.extend(["Minigun", "Punho"])
soldier.armas.extend(["Lança-Foguetes", "Escopeta"])

soldier.add_item_acessorio("Botas", "Resistência a Explosão")
heavy.add_item_acessorio("Sanduíche", "Cura a sua vida ou cure aliados")

soldier.status()
heavy.status()
