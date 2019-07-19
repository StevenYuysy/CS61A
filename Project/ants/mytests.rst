This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5

Suite 2
	>>> from ants import *
	>>> hive, layout = Hive(AssaultPlan()), dry_layout
	>>> dimensions = (1, 9)
	>>> colony = AntColony(None, hive, ant_types(), layout, dimensions)

	Case OPTIONAL
		>>> laser = LaserAnt()
		>>> ant1 = HarvesterAnt(2)
		>>> ant2 = BodyguardAnt(2)
		>>> bee1 = Bee(2)
		>>> bee2 = Bee(2)
		>>> bee3 = Bee(2)
		>>> bee4 = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(laser)
		>>> colony.places["tunnel_0_0"].add_insect(bee4)
		>>> colony.places["tunnel_0_3"].add_insect(bee1)
		>>> colony.places["tunnel_0_3"].add_insect(bee2)
		>>> colony.places["tunnel_0_4"].add_insect(ant1)
		>>> colony.places["tunnel_0_4"].add_insect(ant2)
		>>> colony.places["tunnel_0_5"].add_insect(bee3)
		>>> laser.action(colony)
		>>> round(bee4.armor, 2)
		0.0
		>>> round(bee1.armor, 2)
		0.65
		>>> round(bee2.armor, 2)
		0.7
		>>> round(ant1.armor, 2)
		1.0
		>>> round(ant2.armor, 2)
		0.95
		>>> round(bee3.armor, 2)
		1.25