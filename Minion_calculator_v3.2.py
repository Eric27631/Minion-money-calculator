def Get_input(msg, in_type):
    try:
        in_ = in_type(input(msg))
    except ValueError:
        print('Sorry, invalid please try again')
    else:
        return in_


print('I got all info from: https://hypixel-skyblock.fandom.com/wiki/Minions')
print('Please provide feedback')

Fuels = (
        'None',
        'Coal or Block of coal or enchanted bread',
        'Enchanted coal', 'Enchanted charcoal',
        'Enchanted lava bucket',
        'Magma bucket',
        'Plasma bucket',
        'Hamster wheel',
        'Foul flesh',
        "Catalyst, note: doesn't decrease the time between actions but triples output",
        'Hyper catalyst, note: catalyst but increases minion output by 4x instead of 3x'
)

Upgrades = (
        'None',
        'Minion Expander',
        'Flycatcher',
        'Diamond spreading',
        'Other(Compacter, flint shovel, etc)'
)

Unit_price = Get_input('Unit price: ', float)
Items_per_action = Get_input('Items per action: ', float)
Default_action_time = Get_input('Default action time: ', float)

Fuel = 0
for i, j in enumerate(Fuels, 1):
    print(f"{i}. {j}")
while True:
    Fuel = Get_input('Fuel(put number associated with the fuel you are using): ', int)
    if Fuel in range(1, 12):
        break
    else:
        print('Sorry, invalid please try again')

if Fuel == 10:
    Items_per_action *= 3
    Fuel = 0
elif Fuel == 11:
    Items_per_action *= 4
    Fuel = 0
else:
    Fuel = (0, 5, 10, 20, 25, 30, 35, 50, 90)[Fuel - 1]

Upgrade_1 = 0
for i, j in enumerate(Upgrades, 1):
    print(f"{i}. {j}")
while True:
    Upgrade_1 = Get_input('Upgrade #1(put number associated with the upgrade you are using): ', int)
    if Upgrade_1 in range(1, 6):
        break
    else:
        print('Sorry, invalid please try again')

Upgrade_2 = 0
while True:
    Upgrade_2 = Get_input('Upgrade #2(put number associated with the upgrade you are using): ', int)
    if Upgrade_2 in range(1, 6):
        break
    else:
        print('Sorry, invalid please try again')

Bonus_speed = (Get_input('Bonus speed(ex: farm crystal): ', float) + Fuel) / 100
Action_time = Default_action_time * (1 - (Bonus_speed / (Bonus_speed + 1)))
Earnings_per_minion = 86400 / Action_time * Items_per_action * Unit_price

if Upgrade_1 == 4 or Upgrade_2 == 4:
    Earnings_per_minion += 138240 / Action_time

if Upgrade_1 == 2:
    Bonus_speed += 0.05

if Upgrade_1 == 3:
    Bonus_speed += 0.20

Minions = Get_input('Minions: ', int)


print(round(Earnings_per_minion * Minions / 24), 'per hour')
print(round(Earnings_per_minion * Minions), 'per day')
print(round(Earnings_per_minion * Minions * 7), 'per week')
print(f"Time between actions: {Action_time}")
print(f"Total bonuses(including fuel): {Bonus_speed * 100}%")
