from collections import namedtuple

startTime = 0
ballsHeld = 3
points = 0
cycle = 0
ballsScored = 0
attemptCollect = 0
broken = False
auto = True

#"Average" odds 
oddsOfBreakingLineUpAvg = 2.5
oddsOfBreakingLiftAvg = 10.0
lineUpOddsAvg = 90
oddsOfClimbAvg = 80
levelOddsAvg = 25
oddsInInnerAvg = 20
oddsHighShotAvg = 90
oddsToCollectAvg = 90.0
oddsToCollectAutoAvg = 75.0
odds_of_breakingAvg = 2.0

#"mean" times
driveToCollect6AutoTimeAvg = 4.5
driveToShoot6AutoTimeAvg = 1
driveToCollect5AutoTimeAvg = 1
driveToShoot5AutoTimeAvg = 4
driveToCollectTimeAvg = 4.5
driveToShootTimeAvg = 1
lineUpTimeAvg = 7 
shootHighTimeAvg = 0.75
collectTimeAvg = 1
aimTimeAvg = 2.5
liftTimeAvg = 4.5

#"SD" of times
driveToCollect6AutoSD = 0.25
driveToShoot6AutoSD = 0.2
driveToCollect5AutoSD = .1
driveToShoot5AutoSD = .5
driveToCollectSD = .75
driveToShootSD = .75
lineUpSD = 1.5
shootHighSD = 0.1
collectSD = 0.25
aimSD = 1
liftSD = 1.5

#Point = namedtuple("Point", "x y")
#gameOdds = {
#  'odds_of_breaking': ()
#}
#
#def odds_of_breaking(attribs):
#  delta = attribs.setdefault('riskiness',50) - 50
#  delta += attribs['robotReliblity'] - 50
#  delta += attribs['programming'] - 50
#  return odds_of_breakingAvg + delta * (odds_of_breakingAvg / 2)
#
#odds_of_breaking = calcOdds("odds_of_breaking",[[riskiness,1],[robotReliblity,1],[programming,1]])
#oddsToCollect = calcOdds("oddsToCollect",[[collector,2],[driverPercisionSkill,1],[robotDexterity,1]])
#oddsToCollectAuto = calcOdds("oddsToCollectAuto",[[collector,1],[programming,1]])
#oddsOfBreakingLineUp = calcOdds("oddsOfBreakingLineUp",[[driverPercisionSkill,1],[[robotReliblity,1],[climber,1]])
#oddsOfBreakingLift = calcOdds("oddsOfBreakingLift",[[robotReliblity,1],[climber,2]])
#lineUpOdds = calcOdds("lineUpOdds",[[driverPercisionSkill,1],[[robotReliblity,1],[climber,1]],[robotDexterity,1])
#climbOdds = calcOdds("climbOdds",[[robotReliblity,1],[climber,2]])
#levelOdds = calcOdds("levelOdds",[[stratagy,1],[riskiness,1],[driverPercisionSkill,1]])
#oddsInInner = calcOdds("oddsInInner",[[vision,2],[shooter,3],[programming,1],[robotReliblity,1]])
#oddsHighShot = calcOdds("oddsHighShot",[[vision,2],[shooter,3],[programming,1],[robotReliblity,1]])
#driveToCollect6AutoTime = calcTime("driveToCollect6AutoTime",[[programming,1],[robotSpeed,1],[robotReliblity,1]])
#driveToShoot6AutoTime = calcTime("driveToShoot6AutoTime",[[programming,1],[robotSpeed,1],[robotReliblity,1]])
#driveToCollect5AutoTime = calcTime("driveToCollect5AutoTime",[[programming,1],[robotSpeed,1],[robotReliblity,1]])
#driveToShoot5AutoTime = calcTime("driveToShoot5AutoTime",[[programming,1],[robotSpeed,1],[robotReliblity,1]])
#driveToCollectTime = calcTime("driveToCollectTime",[[driverSpeedSkill,1],[robotSpeed,1],[robotReliblity,1]])
#driveToShootTime = calcTime("driveToShootTime",[[driverSpeedSkill,1],[robotSpeed,1],[robotReliblity,1]])
#lineUpTime = calcTime("lineUpTime",[[driverPercisionSkill,1],[robotDexterity,1],[robotReliblity,1]])
#shootHighTime = calcTime("shootHighTime",[[indexer,1.5],[shooter,2],[programming,1],[robotReliblity,1]])
#collectTime = calcTime("shootHighTime",[[indexer,1.5],[collector,2],[driverPercisionSkill,1.5],[robotDexterity,1.25],[robotReliblity,1]])
#aimTime = calcTime("aimTime",[[driverPercisionSkill,.25],[driverSpeedSkill,.25],[programming,1],[vision,2.5],[robotDexterity,1],[robotReliblity,1]])
#liftTime = calcTime("shootHighTime",[[climber,2.5],[shooter,2],[-robotWeight,.3],[robotReliblity,1]])
#
#def calcTime(name, att):
#  changes = 0
#  for attrubutes in att:
#    changes -= (attrubutes[0] - 50)*attrubutes[1]
#  mean = eval(f"{name}Avg") + (eval(f"{name}SD") * (changes/100))
#  return mean
#
#def calcOdds(name, att):
#  changes = 0
#  for attrubutes in att:
#    changes += (attrubutes[0] - 50)*attrubutes[1]
#  mean = eval(f"{name}Avg") + ((eval(f"{name}Avg")/2) * (changes/100))
#  mean = min(mean,99)
#  mean = max(mean,1)
#  return mean
#