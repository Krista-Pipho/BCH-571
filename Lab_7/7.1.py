import time

def HanoiTowers(n,fromPeg,toPeg):
   if n == 1:
      print("Move disk from peg " + str(fromPeg) + " to peg " + str(toPeg))
      return
   unusedPeg = 6 - fromPeg - toPeg
   HanoiTowers(n-1,fromPeg,unusedPeg)
   print("Move disk from peg " + str(fromPeg) + "to peg " + str(toPeg))
   HanoiTowers(n-1,unusedPeg,toPeg)
   return

Timer = []
i = 0
while (i < 23) == True:
    T1 = time.time()
    HanoiTowers(i+1,1,3)
    T2 = time.time()
    Timer.append(T2-T1)
    i += 1

print(Timer)