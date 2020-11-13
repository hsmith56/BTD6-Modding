util
 
for tower in gameModel.towers:
    for b in tower.behaviors:
        if 'Dart' in tower.name and 'AttackModel' in b.name:
            attackModel = util.BehaviorToAttackModel(b)
            attackModel.weapons[0].rateFrames = 1/((1+tower.tier)*1.5)
            attackModel.weapons[0].rate = 1/((1+tower.tier)*1.5)
            attackModel.range = 16 * (tower.tier + 1)
            attackModel.weapons[0].projectile.pierce = 1.25 + .866*tower.tier
            tower.range = attackModel.range