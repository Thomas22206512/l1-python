class Player:
    def __init__(self, speudo, health, attack, weapon):
        self.speudo = speudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", self.speudo, "/ Points de vie:", self.health, "/ Attaque:", self.attack)

    def get_speudo(self):
        return self.speudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack 

    def get_weapon(self):
        return self.weapon

    def damage(self, damage):
        self.health -= damage
        print(self.get_speudo(), "Vien de subir", damage, "dégats")

    def attack_player(self, target_player):
        target_player.damage(self.attack)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage