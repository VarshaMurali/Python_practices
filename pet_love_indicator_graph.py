import pygal
print("Welcome to the Pet love Indicator\n")
print("Give rating out of 10 for each of the pets, based on your love towards it.\n")
dog=0
cat=0
rabbit=0
bird=0
cow=0
fish=0
my_data={'Dogs':input("Your rating for dog"),'Cats':input("Your rating for cat"),'Rabbits':input("Your rating for rabbit"),'Birds':input("Your rating for bird"),'Cows':input("Your rating for cow"),'Fishes':input("Your rating for fish")}
dog+=int(my_data['Dogs'])
cat+=int(my_data['Cats'])
rabbit+=int(my_data['Rabbits'])
cow+=int(my_data['Cows'])
bird+=int(my_data['Birds'])
fish+=int(my_data['Fishes'])

mychart=pygal.Pie()
mychart.title="Your Pet Love Indicator"
mychart.add('Dogs',dog)
mychart.add('Cats',cat)
mychart.add('Rabbits',rabbit)
mychart.add('Cows',cow)
mychart.add('Birds',bird)
mychart.add('Fishes',fish)
mychart.render_to_file('out_chart.svg')