util
 
def printer(hp, loss):
    print 'Starting Health: ',hp
    print 'Taking away ',loss,' coins'
 
def speed(to_print):
    try:
        starting_health = inGame.bridge.simulation.lastSetHealth
        current_health = inGame.bridge.simulation.Health
        delta = starting_health - current_health
 
        ## Changing this value will effect how much you lose per bloon leak
        ## It is a power power function so the smaller the number the easier it will be 
        # [Default is 0, 1 leak == 1 coin]
        # [It is a power function so whatever round will be raised to the Difficulty Power]
        # [ie. Difficulty of .5 = current round raised to the .5 (or the square root of the round)]
	# [ie2. Difficulty of 1 = current round raised to the 1 (or the same as the round number, 1 leak = 1 * round number lost)]
        # [ie3. Difficulty of 2 = current round raised the the 2 (or the square of the round)]
 
        Difficulty = 0
        if delta > 0:
            curr_round = inGame.bridge.simulation.map.spawner.CurrentRound
            curr_round = curr_round**Difficulty
            inGame.instance.bridge.SetCash(inGame.instance.bridge.GetCash(-1) - (delta*curr_round), -1)
            inGame.bridge.simulation.Shield = 0
            if inGame.instance.bridge.GetCash(-1) < 1:
                inGame.instance.bridge.Lose()
 
            if to_print:
                printer(starting_health,delta*curr_round)
 
    except Exception as e:
        pass
 
# the variable inside must be either 'True' or 'False'
# T/F determines whether or not you get output to the console. True = print to console, False = print nothing
speed(False)
