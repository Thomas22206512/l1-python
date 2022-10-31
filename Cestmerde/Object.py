from model import Player
knife = Weapon("Knife", 20)
bombe = Weapon("Bombe", 15)

player1 = Player("Renard", 50, 5)
player1.damage(3)
print(player1.get_speudo(), "possède", player1.get_health(), "Points de vies")
player2 = Player("Bob", 10, 1)

player1.attack_player(player2)
print(player1.get_speudo(), "attaque", player2.get_speudo())