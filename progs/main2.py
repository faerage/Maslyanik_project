from sys import path

path.append('D:\\faerage\\Phyton_edu\\Maslyanik_project\\packages')

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT
print(extra.good.best.sigma.FunS())
print(FunT())

path.append('D:\\faerage\\Phyton_edu\\Maslyanik_project\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
