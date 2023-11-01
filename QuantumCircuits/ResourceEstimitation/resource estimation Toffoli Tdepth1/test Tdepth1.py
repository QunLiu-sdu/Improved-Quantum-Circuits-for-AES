from projectq import MainEngine
from projectq.backends import ResourceCounter, _resource, ClassicalSimulator, CommandPrinter
from projectq.meta import Uncompute, Compute, Dagger
from projectq.ops import H, Tdag, CNOT, T, X, S, Sdag, Toffoli, Measure, All, Allocate

def Toffoli_gate(eng, a, b, c, resource_check):

    thisqubit = eng.allocate_qureg(4)
    a0 = thisqubit[0]
    a1 = thisqubit[1]
    a2 = thisqubit[2]
    a3 = thisqubit[3]

    if (resource_check):
        H | c

        CNOT | (b, a2)
        CNOT | (a, a0)
        CNOT | (b, a1)
        CNOT | (c, a2)
        CNOT | (a0, a3)
        CNOT | (a, a1)
        CNOT | (c, a3)
        CNOT | (a2, a0)

        T | a
        T | b
        T | c
        T | a0
        Tdag | a1
        Tdag | a2
        Tdag | a3

        CNOT | (a2, a0)
        CNOT | (c, a3)
        CNOT | (a, a1)
        CNOT | (a0, a3)
        CNOT | (c, a2)
        CNOT | (b, a1)
        CNOT | (a, a0)
        CNOT | (b, a2)

        H | c
        return thisqubit

    else:
        Toffoli | (a, b, c)

def And(qubit1, qubit2, target):

    newqubit = eng.allocate_qureg(1)
    ancilla = newqubit[0]
    H | target
    CNOT | (qubit2, ancilla)
    CNOT | (target, qubit1)
    CNOT | (target, qubit2)
    CNOT | (qubit1, ancilla)
    Tdag | qubit1
    Tdag | qubit2
    T | target
    T | ancilla
    CNOT | (qubit1, ancilla)
    CNOT | (target, qubit2)
    CNOT | (target, qubit1)
    CNOT | (qubit2, ancilla)
    H | target
    S | target
    return ancilla

eng=MainEngine()

Qureg=eng.allocate_qureg(3)

qubit1 = Qureg[0]
qubit2 = Qureg[1]
target = Qureg[2]

# X | qubit1
# X | qubit2

thisqubit = Toffoli_gate(eng, qubit1, qubit2, target, 1)
# anc = And(qubit1, qubit2, target)

eng.flush()

Measure | target
print("Measure: {}".format(int(target)))

All(Measure) | thisqubit
print("Measure: {}".format(int(thisqubit[0])))
print("Measure: {}".format(int(thisqubit[1])))
print("Measure: {}".format(int(thisqubit[2])))
print("Measure: {}".format(int(thisqubit[3])))


