class Player:
    team_run = 0  # static or class  varibale

    def __init__(self, run):
        self.run = run  # instance varibale

    def hit_four(self):
        self.run += 4  # instance method
        Player.team_run += 4

    def hit_six(self):
        self.run += 6
        Player.team_run += 6


Shakib = Player(0)
Tamim = Player(0)

Shakib.hit_six()
Shakib.hit_six()
Tamim.hit_four()
Tamim.hit_four()

print("Team run:", Player.team_run)
print("Shakib:", Shakib.run)
print("Tamim:", Tamim.run)

print("Tamim", Tamim.__dict__)
print("Shakib", Shakib.__dict__)
