import copy

from projectq import MainEngine
from projectq.backends import ResourceCounter, _resource, ClassicalSimulator, CommandPrinter
from projectq.meta import Uncompute, Compute, Dagger
from projectq.ops import H, Tdag, CNOT, T, X, S, Sdag, Toffoli, Measure, All, Allocate

# from eprint 2022/683
def CNOT2_mc(eng, a, b, c):
    CNOT | (b, a)
    CNOT | (c, a)

# from eprint 2022/683
def XOR105(x0, x1, x2, x3, y0, y1, y2, y3):
    t = eng.allocate_qureg(105)
    x = []
    for i in range(8):
        x.append(x0[i])
    for i in range(8):
        x.append(x1[i])
    for i in range(8):
        x.append(x2[i])
    for i in range(8):
        x.append(x3[i])


    with Compute(eng):
        CNOT2_mc(eng, t[1], x[7], x[15])
        CNOT2_mc(eng, t[2], x[23], x[31])
        CNOT2_mc(eng, t[3], x[7], x[31])
        CNOT2_mc(eng, t[4], x[15], x[23])
        CNOT2_mc(eng, t[5], x[0], x[8])
        CNOT2_mc(eng, t[6], x[6], x[14])
        CNOT2_mc(eng, t[7], x[5], x[29])
        CNOT2_mc(eng, t[8], x[16], x[24])
        CNOT2_mc(eng, t[9], x[22], x[30])
        CNOT2_mc(eng, t[10], x[13], x[21])
        CNOT2_mc(eng, t[11], x[1], x[9])
        CNOT2_mc(eng, t[12], x[10], x[18])
        CNOT2_mc(eng, t[13], x[2], x[26])
        CNOT2_mc(eng, t[14], x[17], x[25])
        CNOT2_mc(eng, t[15], x[4], x[12])
        CNOT2_mc(eng, t[16], x[3], x[27])
        CNOT2_mc(eng, t[17], x[20], x[28])
        CNOT2_mc(eng, t[18], x[11], x[19])
        CNOT2_mc(eng, t[19], x[0], t[4])
    CNOT2_mc(eng, y1[8-8], t[8], t[19])  # y8  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[21], x[6], t[9])
    CNOT2_mc(eng, y1[14-8], t[10], t[21])  # y14  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[23], x[7], x[22])
        CNOT2_mc(eng, t[24], x[8], t[1])
    CNOT2_mc(eng, y0[0], t[8], t[24])  # y0  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[26], x[10], t[13])
    CNOT2_mc(eng, y2[18-16], t[14], t[26])  # y18  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[28], x[13], t[7])
    CNOT2_mc(eng, y2[21-16], t[17], t[28])  # y21  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[30], x[14], t[2])
    CNOT2_mc(eng, y1[15-8], t[23], t[30])  # y15  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[32], x[6], x[15])
    CNOT2_mc(eng, y0[7], t[30], t[32])  # y7  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[34], x[15], t[3])
    CNOT2_mc(eng, y2[23-16], t[9], t[34]) #y23
    with Compute(eng):
        CNOT2_mc(eng, t[36], x[16], t[3])
    CNOT2_mc(eng, y3[24-24], t[5], t[36])  # y24
    with Compute(eng):
        CNOT2_mc(eng, t[38], x[22], t[6])
    CNOT2_mc(eng, y3[30-24], t[7], t[38]) #y30
    with Compute(eng):
        CNOT2_mc(eng, t[40], x[24], t[2])
    CNOT2_mc(eng, y2[16-16], t[5], t[40])  # y16  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[42], x[26], t[11])
    CNOT2_mc(eng, y0[2], t[12], t[42])  # y2  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[44], x[29], t[10])
    CNOT2_mc(eng, y0[5], t[15], t[44])  # y5  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[46], t[4], t[23])
    CNOT2_mc(eng, y3[31-24], t[21], t[46])  # y31  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[48], x[0], x[9])
        CNOT2_mc(eng, t[49], t[14], t[48])
    CNOT2_mc(eng, y0[1], t[24], t[49])  # y1  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[51], x[1], x[2])
        CNOT2_mc(eng, t[52], x[25], t[12])
    CNOT2_mc(eng, y3[26-24], t[51], t[52])  # y26  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[54], x[3], t[3])
        CNOT2_mc(eng, t[55], t[13], t[18])
    CNOT2_mc(eng, y3[27-24], t[54], t[55])  # y27  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[57], x[4], x[5])
        CNOT2_mc(eng, t[58], x[28], t[10])
    CNOT2_mc(eng, y3[29-24], t[57], t[58])  # y29  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[60], x[4], t[4])
        CNOT2_mc(eng, t[61], t[17], t[18])
    CNOT2_mc(eng, y1[12-8], t[60], t[61])  # y12  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[63], x[5], x[13])
        CNOT2_mc(eng, t[64], x[14], t[9])
    CNOT2_mc(eng, y0[6], t[63], t[64])  # y6  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[66], x[9], x[17])
        CNOT2_mc(eng, t[67], x[18], t[13])
    CNOT2_mc(eng, y1[10-8], t[66], t[67])  # y10  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[69], x[12], x[20])
        CNOT2_mc(eng, t[70], x[21], t[7])
    CNOT2_mc(eng, y1[13-8], t[69], t[70])  # y13  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[72], x[4], x[27])
        CNOT2_mc(eng, t[73], t[69], t[72])
    CNOT2_mc(eng, y3[28-24], t[54], t[73])  # y28  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[75], x[5], x[30])
        CNOT2_mc(eng, t[76], t[6], t[75])
    CNOT2_mc(eng, y2[22-16], t[70], t[76])  # y22  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[78], x[16], x[25])
        CNOT2_mc(eng, t[79], x[1], x[17])
        CNOT2_mc(eng, t[80], t[11], t[78])
    CNOT2_mc(eng, y2[17-16], t[40], t[80])  # y17  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[82], x[8], t[4])
        CNOT2_mc(eng, t[83], t[78], t[79])
    CNOT2_mc(eng, y1[9-8], t[82], t[83])  # y9  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[85], x[19], t[4])
        CNOT2_mc(eng, t[86], t[12], t[16])
    CNOT2_mc(eng, y1[11-8], t[85], t[86])  # y11  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[88], x[24], t[3])
        CNOT2_mc(eng, t[89], t[48], t[79])
    CNOT2_mc(eng, y3[25-24], t[88], t[89])  # y25  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[91], x[2], x[10])
        CNOT2_mc(eng, t[92], x[27], t[1])
        CNOT2_mc(eng, t[93], t[18], t[91])
    CNOT2_mc(eng, y0[3], t[92], t[93])  # y3  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[95], x[3], x[11])
        CNOT2_mc(eng, t[96], x[27], t[2])
        CNOT2_mc(eng, t[97], x[12], t[1])
        CNOT2_mc(eng, t[98], t[17], t[95])
    CNOT2_mc(eng, y0[4], t[97], t[98])  # y4  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[100], x[18], x[26])
        CNOT2_mc(eng, t[101], t[95], t[100])
    CNOT2_mc(eng, y2[19-16], t[96], t[101])  # y19  (3)
    with Compute(eng):
        CNOT2_mc(eng, t[103], x[19], x[28])
        CNOT2_mc(eng, t[104], t[15], t[103])
    CNOT2_mc(eng, y2[20-16], t[96], t[104])  # y20  (3)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)
    Uncompute(eng)

    Uncompute(eng)
    Uncompute(eng)

def CNOT2(eng, a, b, c):
    CNOT | (a, c); CNOT | (b, c)

# AND gate
def Toffoli_gate(eng, a, b, c, resource_check):

    thisqubit = eng.allocate_qureg(1)
    ancilla = thisqubit[0]

    H | c
    CNOT | (b, ancilla)
    CNOT | (c, a)
    CNOT | (c, b)
    CNOT | (a, ancilla)

    Tdag | a
    Tdag | b
    T | c
    T | ancilla

    CNOT | (a, ancilla)
    CNOT | (c, b)
    CNOT | (c, a)
    CNOT | (b, ancilla)

    H | c
    S | c

# ANDdag
def Toffoli_gate1(eng, a, b, c, resource_check):
    H | c
    with Dagger(eng):
        Measure | c

    #if(eng, c): # consider upper bound
    X | c
    Sdag | a # consider dag + dag -> S
    Sdag | b # consider dag + dag -> S
    CNOT | (a, b)
    S | b #consider dag -> Sdag
    CNOT | (a, b)

def Sbox(eng, u,t,m,l,s, resource_check):

    with Compute(eng):
        CNOT2(eng, u[7], u[4], t[0])
        CNOT2(eng, u[7], u[2], t[1])
        CNOT2(eng, u[7], u[1], t[2])
        CNOT2(eng, u[4], u[2], t[3])
        CNOT2(eng, u[3], u[1], t[4])
        CNOT2(eng, t[0], t[4], t[5])
        CNOT2(eng, u[6], u[5], t[6])
        CNOT2(eng, u[0], t[5], t[7])
        CNOT2(eng, u[0], t[6], t[8])
        CNOT2(eng, t[5], t[6], t[9])
        CNOT2(eng, u[6], u[2], t[10])
        CNOT2(eng, u[5], u[2], t[11])
        CNOT2(eng, t[2], t[3], t[12])
        CNOT2(eng, t[5], t[10], t[13])
        CNOT2(eng, t[4], t[10], t[14])
        CNOT2(eng, t[4], t[11], t[15])
        CNOT2(eng, t[8], t[15], t[16])
        CNOT2(eng, u[4], u[0], t[17])
        CNOT2(eng, t[6], t[17], t[18])
        CNOT2(eng, t[0], t[18], t[19])
        CNOT2(eng, u[1], u[0], t[20])
        CNOT2(eng, t[6], t[20], t[21])
        CNOT2(eng, t[1], t[21], t[22])
        CNOT2(eng, t[1], t[9], t[23])
        CNOT2(eng, t[19], t[16], t[24])
        CNOT2(eng, t[2], t[15], t[25])
        CNOT2(eng, t[0], t[11], t[26])
        Toffoli_gate(eng, t[12], t[5], m[0], resource_check)
        Toffoli_gate(eng, t[22], t[7], m[1], resource_check)
        CNOT2(eng, t[13], m[0], m[2])
        Toffoli_gate(eng, t[18], u[0], m[3], resource_check)
        CNOT2(eng, m[3], m[0], m[4])
        Toffoli_gate(eng, t[2], t[15], m[5], resource_check)
        Toffoli_gate(eng, t[21], t[8], m[6], resource_check)
        CNOT2(eng, t[25], m[5], m[7])
        Toffoli_gate(eng, t[19], t[16], m[8], resource_check)
        CNOT2(eng, m[8], m[5], m[9])
        Toffoli_gate(eng, t[0], t[14], m[10], resource_check)
        Toffoli_gate(eng, t[3], t[26], m[11], resource_check)
        CNOT2(eng, m[11], m[10], m[12])
        Toffoli_gate(eng, t[1], t[9], m[13], resource_check)
        CNOT2(eng, m[13], m[10], m[14])
        CNOT2(eng, m[2], m[1], m[15])
        CNOT2(eng, m[4], t[23], m[16])
        CNOT2(eng, m[7], m[6], m[17])
        CNOT2(eng, m[9], m[14], m[18])
        CNOT2(eng, m[15], m[12], m[19])
        CNOT2(eng, m[16], m[14], m[20])
        CNOT2(eng, m[17], m[12], m[21])
        CNOT2(eng, m[18], t[24], m[22])
        CNOT2(eng, m[21], m[22], m[23])
        CNOT | (m[21], l[0])
        CNOT | (m[19], l[1])
        Toffoli_gate(eng, m[21], m[19], m[24], resource_check)
        Toffoli_gate(eng, l[1], m[22], m[30], resource_check)
        Toffoli_gate(eng, m[20], l[0], m[33], resource_check)
        CNOT | (m[23], l[3])
        CNOT2(eng, m[20], m[24], m[25])
        CNOT2(eng, m[19], m[20], m[26])
        CNOT | (m[26], l[2])
        CNOT2(eng, m[22], m[24], m[27])
        CNOT2(eng, m[26], m[24], m[32])
        Toffoli_gate(eng, m[27], m[26], m[28], resource_check)
        Toffoli_gate(eng, m[25], m[23], m[29], resource_check)
        Toffoli_gate(eng, l[2], m[30], m[31], resource_check)
        Toffoli_gate(eng, l[3], m[33], m[34], resource_check)
        CNOT2(eng, m[23], m[24], m[35])
        CNOT2(eng, m[20], m[28], m[36])
        CNOT2(eng, m[31], m[32], m[37])
        CNOT2(eng, m[22], m[29], m[38])
        CNOT2(eng, m[34], m[35], m[39])
        CNOT2(eng, m[37], m[39], m[40])
        CNOT2(eng, m[36], m[38], m[41])
        CNOT2(eng, m[36], m[37], m[42])
        CNOT2(eng, m[38], m[39], m[43])
        CNOT2(eng, m[41], m[40], m[44])
        CNOT | (m[43], l[4])
        CNOT | (m[39], l[5])
        CNOT | (m[38], l[6])
        CNOT | (m[42], l[7])
        CNOT | (m[37], l[8])
        CNOT | (m[36], l[9])
        CNOT | (m[41], l[10])
        CNOT | (m[44], l[11])
        CNOT | (m[40], l[12])
        Toffoli_gate(eng, m[43], t[5], m[45], resource_check)
        Toffoli_gate(eng, m[39], t[7], m[46], resource_check)
        Toffoli_gate(eng, m[38], u[0], m[47], resource_check)
        Toffoli_gate(eng, m[42], t[15], m[48], resource_check)
        Toffoli_gate(eng, m[37], t[8], m[49], resource_check)
        Toffoli_gate(eng, m[36], t[16], m[50], resource_check)
        Toffoli_gate(eng, m[41], t[14], m[51], resource_check)
        Toffoli_gate(eng, m[44], t[26], m[52], resource_check)
        Toffoli_gate(eng, m[40], t[9], m[53], resource_check)
        Toffoli_gate(eng, l[4], t[12], m[54], resource_check)
        Toffoli_gate(eng, l[5], t[22], m[55], resource_check)
        Toffoli_gate(eng, l[6], t[18], m[56], resource_check)
        Toffoli_gate(eng, l[7], t[2], m[57], resource_check)
        Toffoli_gate(eng, l[8], t[21], m[58], resource_check)
        Toffoli_gate(eng, l[9], t[19], m[59], resource_check)
        Toffoli_gate(eng, l[10], t[0], m[60], resource_check)
        Toffoli_gate(eng, l[11], t[3], m[61], resource_check)
        Toffoli_gate(eng, l[12], t[1], m[62], resource_check)
        CNOT | (m[21], l[0])
        CNOT | (m[19], l[1])
        CNOT | (m[26], l[2])
        CNOT | (m[23], l[3])
        CNOT | (m[43], l[4])
        CNOT | (m[39], l[5])
        CNOT | (m[38], l[6])
        CNOT | (m[42], l[7])
        CNOT | (m[37], l[8])
        CNOT | (m[36], l[9])
        CNOT | (m[41], l[10])
        CNOT | (m[44], l[11])
        CNOT | (m[40], l[12])
        CNOT2(eng, m[60], m[61], l[0])
        CNOT2(eng, m[49], m[55], l[1])
        CNOT2(eng, m[45], m[47], l[2])
        CNOT2(eng, m[46], m[54], l[3])
        CNOT2(eng, m[53], m[57], l[4])
        CNOT2(eng, m[48], m[60], l[5])
        CNOT2(eng, m[61], l[5], l[6])
        CNOT2(eng, m[45], l[3], l[7])
        CNOT2(eng, m[50], m[58], l[8])
        CNOT2(eng, m[51], m[52], l[9])
        CNOT2(eng, m[52], l[4], l[10])
        CNOT2(eng, m[59], l[2], l[11])
        CNOT2(eng, m[47], m[50], l[12])
        CNOT2(eng, m[49], l[0], l[13])
        CNOT2(eng, m[51], m[60], l[14])
        CNOT2(eng, m[54], l[1], l[15])
        CNOT2(eng, m[55], l[0], l[16])
        CNOT2(eng, m[56], l[1], l[17])
        CNOT2(eng, m[57], l[8], l[18])
        CNOT2(eng, m[62], l[4], l[19])
        CNOT2(eng, l[0], l[1], l[20])
        CNOT2(eng, l[1], l[7], l[21])
        CNOT2(eng, l[3], l[12], l[22])
        CNOT2(eng, l[18], l[2], l[23])
        CNOT2(eng, l[15], l[9], l[24])
        CNOT2(eng, l[6], l[10], l[25])
        CNOT2(eng, l[7], l[9], l[26])
        CNOT2(eng, l[8], l[10], l[27])
        CNOT2(eng, l[11], l[14], l[28])
        CNOT2(eng, l[11], l[17], l[29])

    CNOT2(eng, l[6], l[24], s[7])
    CNOT2(eng, l[16], l[26], s[6])
    CNOT2(eng, l[19], l[28], s[5])
    X | s[6]
    X | s[5]
    CNOT2(eng, l[6], l[21], s[4])
    CNOT2(eng, l[20], l[22], s[3])
    CNOT2(eng, l[25], l[29], s[2])
    CNOT2(eng, l[13], l[27], s[1])
    CNOT2(eng, l[6], l[23], s[0])
    X | s[1]
    X | s[0]

    CNOT2(eng, l[11], l[17], l[29])
    CNOT2(eng, l[11], l[14], l[28])
    CNOT2(eng, l[8], l[10], l[27])
    CNOT2(eng, l[7], l[9], l[26])
    CNOT2(eng, l[6], l[10], l[25])
    CNOT2(eng, l[15], l[9], l[24])
    CNOT2(eng, l[18], l[2], l[23])



def Sbox_opt(eng, u,q,s, resource_check):

    CNOT2(eng, u[7], u[4], q[0])
    CNOT2(eng, u[7], u[2], q[1])
    CNOT | (u[1], u[7])
    CNOT2(eng, u[4], u[2], q[2])
    CNOT | (u[1], u[3])
    CNOT2(eng, q[0], u[3], q[3])
    CNOT2(eng, u[6], u[5], q[4])
    CNOT2(eng, u[0], q[3], q[5])
    CNOT2(eng, u[0], q[4], q[6])
    CNOT2(eng, q[3], q[4], q[7])
    CNOT | (u[2], u[6])
    CNOT | (u[2], u[5])
    CNOT2(eng, u[7], q[2], q[8])
    CNOT2(eng, q[3], u[6], q[9])
    CNOT | (u[3], u[6])
    CNOT | (u[5], u[3])
    CNOT2(eng, q[6], u[3], q[10])
    CNOT | (u[0], u[4])
    CNOT | (q[4], u[4])
    CNOT2(eng, q[0], u[4], q[11])
    CNOT | (u[0], u[1])
    CNOT | (u[1], q[4])
    CNOT2(eng, q[1], q[4], q[12])
    CNOT2(eng, q[1], q[7], q[13])
    CNOT2(eng, q[11], q[10], q[14])
    CNOT2(eng, u[7], u[3], q[15])
    CNOT | (q[0], u[5])
    Toffoli_gate(eng, q[8], q[3], q[16], resource_check)
    Toffoli_gate(eng, q[12], q[5], q[17], resource_check)
    CNOT | (q[16], q[9])
    Toffoli_gate(eng, u[4], u[0], q[18], resource_check)
    CNOT | (q[18], q[16])
    Toffoli_gate(eng, u[7], u[3], q[19], resource_check)
    Toffoli_gate(eng, q[4], q[6], q[20], resource_check)
    CNOT | (q[19], q[15])
    Toffoli_gate(eng, q[11], q[10], q[21], resource_check)
    CNOT | (q[19], q[21])
    Toffoli_gate(eng, q[0], u[6], q[22], resource_check)
    Toffoli_gate(eng, q[2], u[5], q[23], resource_check)
    CNOT | (q[22], q[23])
    Toffoli_gate(eng, q[1], q[7], q[24], resource_check)
    CNOT | (q[22], q[24])
    CNOT | (q[17], q[9])
    CNOT | (q[13], q[16])
    CNOT | (q[20], q[15])
    CNOT | (q[24], q[21])
    CNOT | (q[23], q[9])
    CNOT | (q[24], q[16])
    CNOT | (q[23], q[15])
    CNOT | (q[14], q[21])
    CNOT2(eng, q[15], q[21], q[25])
    CNOT | (q[15], q[60])
    CNOT | (q[9], q[61])
    Toffoli_gate(eng, q[15], q[9], q[26], resource_check)
    Toffoli_gate(eng, q[61], q[21], q[32], resource_check)
    Toffoli_gate(eng, q[16], q[60], q[35], resource_check)
    CNOT | (q[25], q[63])
    CNOT2(eng, q[16], q[26], q[27])
    CNOT2(eng, q[9], q[16], q[28])
    CNOT | (q[28], q[62])
    CNOT2(eng, q[21], q[26], q[29])
    CNOT2(eng, q[28], q[26], q[34])
    Toffoli_gate(eng, q[29], q[28], q[30], resource_check)
    Toffoli_gate(eng, q[27], q[25], q[31], resource_check)
    Toffoli_gate(eng, q[62], q[32], q[33], resource_check)
    Toffoli_gate(eng, q[63], q[35], q[36], resource_check)
    CNOT | (q[25], q[26])
    CNOT | (q[30], q[16])
    CNOT | (q[34], q[33])
    CNOT | (q[31], q[21])
    CNOT | (q[26], q[36])
    CNOT2(eng, q[33], q[36], q[37])
    CNOT2(eng, q[16], q[21], q[38])
    CNOT2(eng, q[16], q[33], q[39])
    CNOT2(eng, q[21], q[36], q[40])
    CNOT2(eng, q[38], q[37], q[41])
    CNOT | (q[40], q[64])
    CNOT | (q[36], q[65])
    CNOT | (q[21], q[66])
    CNOT | (q[39], q[67])
    CNOT | (q[33], q[68])
    CNOT | (q[16], q[69])
    CNOT | (q[38], q[70])
    CNOT | (q[41], q[71])
    CNOT | (q[37], q[72])
    Toffoli_gate(eng, q[40], q[3], q[42], resource_check)
    Toffoli_gate(eng, q[36], q[5], q[43], resource_check)
    Toffoli_gate(eng, q[21], u[0], q[44], resource_check)
    Toffoli_gate(eng, q[39], u[3], q[45], resource_check)
    Toffoli_gate(eng, q[33], q[6], q[46], resource_check)
    Toffoli_gate(eng, q[16], q[10], q[47], resource_check)
    Toffoli_gate(eng, q[38], u[6], q[48], resource_check)
    Toffoli_gate(eng, q[41], u[5], q[49], resource_check)
    Toffoli_gate(eng, q[37], q[7], q[50], resource_check)
    Toffoli_gate(eng, q[64], q[8], q[51], resource_check)
    Toffoli_gate(eng, q[65], q[12], q[52], resource_check)
    Toffoli_gate(eng, q[66], u[4], q[53], resource_check)
    Toffoli_gate(eng, q[67], u[7], q[54], resource_check)
    Toffoli_gate(eng, q[68], q[4], q[55], resource_check)
    Toffoli_gate(eng, q[69], q[11], q[56], resource_check)
    Toffoli_gate(eng, q[70], q[0], q[57], resource_check)
    Toffoli_gate(eng, q[71], q[2], q[58], resource_check)
    Toffoli_gate(eng, q[72], q[1], q[59], resource_check)
    CNOT | (q[15], q[60])
    CNOT | (q[9], q[61])
    CNOT | (q[28], q[62])
    CNOT | (q[25], q[63])
    CNOT | (q[40], q[64])
    CNOT | (q[36], q[65])
    CNOT | (q[21], q[66])
    CNOT | (q[39], q[67])
    CNOT | (q[33], q[68])
    CNOT | (q[16], q[69])
    CNOT | (q[38], q[70])
    CNOT | (q[41], q[71])
    CNOT | (q[37], q[72])
    CNOT2(eng, q[57], q[58], q[60])
    CNOT2(eng, q[46], q[52], q[61])
    CNOT2(eng, q[42], q[44], q[62])
    CNOT2(eng, q[43], q[51], q[63])
    CNOT2(eng, q[50], q[54], q[64])
    CNOT2(eng, q[45], q[57], q[65])
    CNOT2(eng, q[58], q[65], q[66])
    CNOT2(eng, q[42], q[63], q[67])
    CNOT2(eng, q[47], q[55], q[68])
    CNOT2(eng, q[48], q[49], q[69])
    CNOT2(eng, q[49], q[64], q[70])
    CNOT2(eng, q[56], q[62], q[71])
    CNOT2(eng, q[44], q[47], q[72])
    CNOT2(eng, q[66], q[70], q[73])
    CNOT | (q[60], q[46])
    CNOT | (q[57], q[48])
    CNOT | (q[61], q[51])
    CNOT | (q[60], q[52])
    CNOT | (q[61], q[53])
    CNOT | (q[68], q[54])
    CNOT | (q[64], q[59])
    CNOT | (q[61], q[60])
    CNOT2(eng, q[61], q[67], s[4])
    CNOT2(eng, q[63], q[72], s[3])
    CNOT2(eng, q[54], q[62], s[0])
    CNOT2(eng, q[51], q[69], s[7])
    CNOT2(eng, q[67], q[69], s[6])
    CNOT2(eng, q[68], q[70], s[1])
    CNOT2(eng, q[71], q[48], s[5])
    CNOT2(eng, q[71], q[53], s[2])
    CNOT | (q[66], s[7])
    CNOT | (q[52], s[6])
    CNOT | (q[59], s[5])
    X | s[6]
    X | s[5]
    CNOT | (q[66], s[4])
    CNOT | (q[60], s[3])
    CNOT | (q[73], s[2])
    CNOT | (q[46], s[1])
    CNOT | (q[66], s[0])
    X | s[1]
    X | s[0]

def Sbox_inv(eng, u, q, s, resource_check):
    CNOT | (q[70], q[69])
    CNOT | (q[73], q[68])
    CNOT | (q[77], q[63])
    CNOT | (q[70], q[62])
    CNOT | (q[69], q[61])
    CNOT | (q[70], q[60])
    CNOT | (q[66], q[57])
    CNOT | (q[69], q[55])
    CNOT2(eng, q[75], q[79], q[82])
    CNOT2(eng, q[53], q[56], q[81])
    CNOT2(eng, q[65], q[71], q[80])
    CNOT2(eng, q[58], q[73], q[79])
    CNOT2(eng, q[57], q[58], q[78])
    CNOT2(eng, q[56], q[64], q[77])
    CNOT2(eng, q[51], q[72], q[76])
    CNOT2(eng, q[67], q[74], q[75])
    CNOT2(eng, q[54], q[66], q[74])
    CNOT2(eng, q[59], q[63], q[73])
    CNOT2(eng, q[52], q[60], q[72])
    CNOT2(eng, q[51], q[53], q[71])
    CNOT2(eng, q[55], q[61], q[70])
    CNOT2(eng, q[66], q[67], q[69])
    CNOT | (q[46], q[81])
    CNOT | (q[50], q[80])
    CNOT | (q[47], q[79])
    CNOT | (q[42], q[78])
    CNOT | (q[43], q[77])
    CNOT | (q[48], q[76])
    CNOT | (q[44], q[75])
    CNOT | (q[45], q[74])
    CNOT | (q[49], q[73])
    CNOT | (q[29], q[72])
    CNOT | (q[32], q[71])
    CNOT | (q[9], q[70])
    CNOT | (q[15], q[69])
    Toffoli_gate(eng, q[81], q[1], q[68], resource_check)
    Toffoli_gate(eng, q[80], q[2], q[67], resource_check)
    Toffoli_gate(eng, q[79], q[0], q[66], resource_check)
    Toffoli_gate(eng, q[78], q[11], q[65], resource_check)
    Toffoli_gate(eng, q[77], q[4], q[64], resource_check)
    Toffoli_gate(eng, q[76], u[7], q[63], resource_check)
    Toffoli_gate(eng, q[75], u[4], q[62], resource_check)
    Toffoli_gate(eng, q[74], q[12], q[61], resource_check)
    Toffoli_gate(eng, q[73], q[8], q[60], resource_check)
    Toffoli_gate(eng, q[46], q[7], q[59], resource_check)
    Toffoli_gate(eng, q[50], u[5], q[58], resource_check)
    Toffoli_gate(eng, q[47], u[6], q[57], resource_check)
    Toffoli_gate(eng, q[42], q[10], q[56], resource_check)
    Toffoli_gate(eng, q[43], q[6], q[55], resource_check)
    Toffoli_gate(eng, q[48], u[3], q[54], resource_check)
    Toffoli_gate(eng, q[44], u[0], q[53], resource_check)
    Toffoli_gate(eng, q[45], q[5], q[52], resource_check)
    Toffoli_gate(eng, q[49], q[3], q[51], resource_check)
    CNOT | (q[46], q[81])
    CNOT | (q[50], q[80])
    CNOT | (q[47], q[79])
    CNOT | (q[42], q[78])
    CNOT | (q[43], q[77])
    CNOT | (q[48], q[76])
    CNOT | (q[44], q[75])
    CNOT | (q[45], q[74])
    CNOT | (q[49], q[73])
    CNOT2(eng, q[47], q[46], q[50])
    CNOT2(eng, q[44], q[45], q[49])
    CNOT2(eng, q[42], q[43], q[48])
    CNOT2(eng, q[42], q[44], q[47])
    CNOT2(eng, q[43], q[45], q[46])
    CNOT2(eng, q[40], q[41], q[45])
    CNOT2(eng, q[23], q[35], q[44])
    CNOT2(eng, q[37], q[38], q[43])
    CNOT2(eng, q[19], q[34], q[42])
    CNOT2(eng, q[29], q[30], q[41])
    Toffoli_gate(eng, q[72], q[39], q[40], resource_check)
    Toffoli_gate(eng, q[71], q[36], q[37], resource_check)
    Toffoli_gate(eng, q[31], q[29], q[35], resource_check)
    Toffoli_gate(eng, q[33], q[32], q[34], resource_check)
    CNOT2(eng, q[32], q[30], q[38])
    CNOT2(eng, q[23], q[30], q[33])
    CNOT | (q[32], q[71])
    CNOT2(eng, q[9], q[19], q[32])
    CNOT2(eng, q[19], q[30], q[31])
    CNOT | (q[29], q[72])
    Toffoli_gate(eng, q[19], q[69], q[39], resource_check)
    Toffoli_gate(eng, q[70], q[23], q[36], resource_check)
    Toffoli_gate(eng, q[15], q[9], q[30], resource_check)
    CNOT | (q[9], q[70])
    CNOT | (q[15], q[69])
    CNOT2(eng, q[15], q[23], q[29])
    CNOT | (q[14], q[23])
    CNOT | (q[26], q[15])
    CNOT | (q[28], q[19])
    CNOT | (q[26], q[9])
    CNOT | (q[28], q[23])
    CNOT | (q[21], q[15])
    CNOT | (q[13], q[19])
    CNOT | (q[17], q[9])
    CNOT2(eng, q[27], q[24], q[28])
    CNOT2(eng, q[25], q[24], q[26])
    CNOT2(eng, q[22], q[20], q[23])
    CNOT | (q[20], q[15])
    CNOT2(eng, q[18], q[16], q[19])
    CNOT | (q[16], q[9])
    Toffoli_gate(eng, q[1], q[7], q[27], resource_check)
    Toffoli_gate(eng, q[2], u[5], q[25], resource_check)
    Toffoli_gate(eng, q[0], u[6], q[24], resource_check)
    Toffoli_gate(eng, q[11], q[10], q[22], resource_check)
    Toffoli_gate(eng, q[4], q[6], q[21], resource_check)
    Toffoli_gate(eng, u[7], u[3], q[20], resource_check)
    Toffoli_gate(eng, u[4], u[0], q[18], resource_check)
    Toffoli_gate(eng, q[12], q[5], q[17], resource_check)
    Toffoli_gate(eng, q[8], q[3], q[16], resource_check)
    CNOT | (q[0], u[5])
    CNOT2(eng, u[7], u[3], q[15])
    CNOT2(eng, q[11], q[10], q[14])
    CNOT2(eng, q[1], q[7], q[13])
    CNOT2(eng, q[1], q[4], q[12])
    CNOT | (u[1], q[4])
    CNOT | (u[0], u[1])
    CNOT2(eng, q[0], u[4], q[11])
    CNOT | (q[4], u[4])
    CNOT | (u[0], u[4])
    CNOT2(eng, q[6], u[3], q[10])
    CNOT | (u[5], u[3])
    CNOT | (u[3], u[6])
    CNOT2(eng, q[3], u[6], q[9])
    CNOT2(eng, u[7], q[2], q[8])
    CNOT | (u[2], u[5])
    CNOT | (u[2], u[6])
    CNOT2(eng, q[3], q[4], q[7])
    CNOT2(eng, u[0], q[4], q[6])
    CNOT2(eng, u[0], q[3], q[5])
    CNOT2(eng, u[6], u[5], q[4])
    CNOT2(eng, q[0], u[3], q[3])
    CNOT | (u[1], u[3])
    CNOT2(eng, u[4], u[2], q[2])
    CNOT | (u[1], u[7])
    CNOT2(eng, u[7], u[2], q[1])
    CNOT2(eng, u[7], u[4], q[0])

def Sbox_combine(eng, u1, u2, s2, q_used, q_zero, q, resource_check):

    assert len(q_used) == 74
    assert len(q_zero) == 24

    new_q_used = []
    new_q_zero = []

    for i in range(74):
        new_q_used.append(-1)
    new_q_used[0] = q_zero[0]
    new_q_used[1] = q_zero[1]
    new_q_used[2] = q_zero[2]
    new_q_used[3] = q_zero[3]
    new_q_used[4] = q_zero[4]
    new_q_used[5] = q_zero[5]
    new_q_used[6] = q_zero[6]
    new_q_used[7] = q_zero[7]
    new_q_used[8] = q_zero[8]
    new_q_used[9] = q_zero[9]
    new_q_used[10] = q_zero[10]
    new_q_used[11] = q_zero[11]
    new_q_used[12] = q_zero[12]
    new_q_used[13] = q_zero[13]
    new_q_used[14] = q_zero[14]
    new_q_used[15] = q_zero[15]

    new_q_used[16] = q_used[73]

    new_q_used[17] = q_zero[16]
    new_q_used[18] = q_zero[17]
    new_q_used[19] = q_zero[18]
    new_q_used[20] = q_zero[19]
    new_q_used[21] = q_zero[20]
    new_q_used[22] = q_zero[21]
    new_q_used[23] = q_zero[22]
    new_q_used[24] = q_zero[23]

    new_q_used[25] = q_used[42]
    new_q_used[26] = q_used[45]
    new_q_used[32] = q_used[46]
    new_q_used[35] = q_used[47]
    new_q_used[27] = q_used[49]
    new_q_used[28] = q_used[50]
    new_q_used[29] = q_used[52]
    new_q_used[34] = q_used[53]
    new_q_used[30] = q_used[54]
    new_q_used[31] = q_used[55]
    new_q_used[33] = q_used[56]
    new_q_used[36] = q_used[57]
    new_q_used[37] = q_used[58]
    new_q_used[38] = q_used[59]
    new_q_used[39] = q_used[37]
    new_q_used[40] = q_used[38]
    new_q_used[41] = q_used[39]
    new_q_used[64] = q_used[40]
    new_q_used[65] = q_used[41]
    new_q_used[66] = q_used[64]
    new_q_used[67] = q_used[65]
    new_q_used[68] = q_used[66]
    new_q_used[69] = q_used[67]
    new_q_used[70] = q_used[68]
    new_q_used[71] = q_used[69]
    new_q_used[72] = q_used[70]
    new_q_used[42] = q_used[71]
    new_q_used[43] = q_used[72]
    new_q_used[44] = q_used[30]
    new_q_used[45] = q_used[31]
    new_q_used[46] = q_used[33]
    new_q_used[47] = q_used[36]
    new_q_used[48] = q_used[27]
    new_q_used[49] = q_used[28]
    new_q_used[50] = q_used[29]
    new_q_used[51] = q_used[34]
    new_q_used[52] = q_used[62]
    new_q_used[53] = q_used[63]
    new_q_used[54] = q_used[26]
    new_q_used[55] = q_used[32]
    new_q_used[56] = q_used[35]
    new_q_used[57] = q_used[25]
    new_q_used[58] = q_used[60]
    new_q_used[59] = q_used[61]
    new_q_used[60] = q_used[43]
    new_q_used[61] = q_used[44]
    new_q_used[62] = q_used[51]
    new_q_used[63] = q_used[48]
    new_q_used[73] = q_used[20]


    for bit in q:
        if bit not in new_q_used:
            new_q_zero.append(bit)


    CNOT | (q_used[61], q_used[60])
    CNOT | (q_used[64], q_used[59])
    CNOT | (q_used[68], q_used[54])
    CNOT | (q_used[61], q_used[53])
    CNOT | (q_used[60], q_used[52])
    CNOT | (q_used[61], q_used[51])
    CNOT | (q_used[57], q_used[48])
    CNOT | (q_used[60], q_used[46])
    CNOT2(eng, q_used[66], q_used[70], q_used[73])
    CNOT2(eng, q_used[44], q_used[47], q_used[72])
    CNOT2(eng, q_used[56], q_used[62], q_used[71])
    CNOT2(eng, q_used[49], q_used[64], q_used[70])
    CNOT2(eng, q_used[48], q_used[49], q_used[69])
    CNOT2(eng, q_used[47], q_used[55], q_used[68])
    CNOT2(eng, q_used[42], q_used[63], q_used[67])
    CNOT2(eng, q_used[58], q_used[65], q_used[66])
    CNOT2(eng, q_used[45], q_used[57], q_used[65])
    CNOT2(eng, q_used[50], q_used[54], q_used[64])
    CNOT2(eng, q_used[43], q_used[51], q_used[63])
    CNOT2(eng, q_used[42], q_used[44], q_used[62])
    CNOT2(eng, q_used[46], q_used[52], q_used[61])
    CNOT2(eng, q_used[57], q_used[58], q_used[60])
    CNOT | (q_used[37], q_used[72])
    CNOT | (q_used[41], q_used[71])
    CNOT | (q_used[38], q_used[70])
    CNOT | (q_used[16], q_used[69])
    CNOT | (q_used[33], q_used[68])
    CNOT | (q_used[39], q_used[67])
    CNOT | (q_used[21], q_used[66])
    CNOT | (q_used[36], q_used[65])
    CNOT | (q_used[40], q_used[64])
    CNOT | (q_used[25], q_used[63])
    CNOT | (q_used[28], q_used[62])
    CNOT | (q_used[9], q_used[61])
    CNOT | (q_used[15], q_used[60])
    Toffoli_gate1(eng, q_used[72], q_used[1], q_used[59], resource_check)
    Toffoli_gate1(eng, q_used[71], q_used[2], q_used[58], resource_check)
    Toffoli_gate1(eng, q_used[70], q_used[0], q_used[57], resource_check)
    Toffoli_gate1(eng, q_used[69], q_used[11], q_used[56], resource_check)
    Toffoli_gate1(eng, q_used[68], q_used[4], q_used[55], resource_check)
    Toffoli_gate1(eng, q_used[67], u1[7], q_used[54], resource_check)
    Toffoli_gate1(eng, q_used[66], u1[4], q_used[53], resource_check)
    Toffoli_gate1(eng, q_used[65], q_used[12], q_used[52], resource_check)
    Toffoli_gate1(eng, q_used[64], q_used[8], q_used[51], resource_check)
    Toffoli_gate1(eng, q_used[37], q_used[7], q_used[50], resource_check)
    Toffoli_gate1(eng, q_used[41], u1[5], q_used[49], resource_check)
    Toffoli_gate1(eng, q_used[38], u1[6], q_used[48], resource_check)
    Toffoli_gate1(eng, q_used[16], q_used[10], q_used[47], resource_check)
    Toffoli_gate1(eng, q_used[33], q_used[6], q_used[46], resource_check)
    Toffoli_gate1(eng, q_used[39], u1[3], q_used[45], resource_check)
    Toffoli_gate1(eng, q_used[21], u1[0], q_used[44], resource_check)
    Toffoli_gate1(eng, q_used[36], q_used[5], q_used[43], resource_check)
    Toffoli_gate1(eng, q_used[40], q_used[3], q_used[42], resource_check)
    CNOT | (q_used[37], q_used[72])
    CNOT | (q_used[41], q_used[71])
    CNOT | (q_used[38], q_used[70])
    CNOT | (q_used[16], q_used[69])
    CNOT | (q_used[33], q_used[68])
    CNOT | (q_used[39], q_used[67])
    CNOT | (q_used[21], q_used[66])
    CNOT | (q_used[36], q_used[65])
    CNOT | (q_used[40], q_used[64])
    CNOT2(eng, q_used[38], q_used[37], q_used[41])
    CNOT2(eng, q_used[21], q_used[36], q_used[40])
    CNOT2(eng, q_used[16], q_used[33], q_used[39])
    CNOT2(eng, q_used[16], q_used[21], q_used[38])
    CNOT2(eng, q_used[33], q_used[36], q_used[37])
    CNOT | (q_used[26], q_used[36])
    CNOT | (q_used[31], q_used[21])
    CNOT | (q_used[34], q_used[33])
    CNOT | (q_used[30], q_used[16])
    CNOT | (q_used[25], q_used[26])
    Toffoli_gate1(eng, q_used[63], q_used[35], q_used[36], resource_check)
    Toffoli_gate1(eng, q_used[62], q_used[32], q_used[33], resource_check)
    Toffoli_gate1(eng, q_used[27], q_used[25], q_used[31], resource_check)
    Toffoli_gate1(eng, q_used[29], q_used[28], q_used[30], resource_check)
    CNOT2(eng, q_used[28], q_used[26], q_used[34])
    CNOT2(eng, q_used[21], q_used[26], q_used[29])
    CNOT | (q_used[28], q_used[62])
    CNOT2(eng, q_used[9], q_used[16], q_used[28])
    CNOT2(eng, q_used[16], q_used[26], q_used[27])
    CNOT | (q_used[25], q_used[63])
    Toffoli_gate1(eng, q_used[16], q_used[60], q_used[35], resource_check)
    Toffoli_gate1(eng, q_used[61], q_used[21], q_used[32], resource_check)
    Toffoli_gate1(eng, q_used[15], q_used[9], q_used[26], resource_check)
    CNOT | (q_used[9], q_used[61])
    CNOT | (q_used[15], q_used[60])
    CNOT2(eng, q_used[15], q_used[21], q_used[25])
    CNOT | (q_used[14], q_used[21])
    CNOT | (q_used[23], q_used[15])
    CNOT | (q_used[24], q_used[16])
    CNOT | (q_used[23], q_used[9])
    CNOT | (q_used[24], q_used[21])
    CNOT | (q_used[20], q_used[15])
    CNOT | (q_used[13], q_used[16])
    CNOT | (q_used[17], q_used[9])
    CNOT | (q_used[22], q_used[24])
    Toffoli_gate1(eng, q_used[1], q_used[7], q_used[24], resource_check)
    CNOT | (q_used[22], q_used[23])
    Toffoli_gate1(eng, q_used[2], u1[5], q_used[23], resource_check)
    Toffoli_gate1(eng, q_used[0], u1[6], q_used[22], resource_check)
    CNOT | (q_used[19], q_used[21])
    Toffoli_gate1(eng, q_used[11], q_used[10], q_used[21], resource_check)
    CNOT | (q_used[19], q_used[15])
    Toffoli_gate1(eng, q_used[4], q_used[6], q_used[20], resource_check)
    Toffoli_gate1(eng, u1[7], u1[3], q_used[19], resource_check)
    CNOT | (q_used[18], q_used[16])
    Toffoli_gate1(eng, u1[4], u1[0], q_used[18], resource_check)
    CNOT | (q_used[16], q_used[9])
    Toffoli_gate1(eng, q_used[12], q_used[5], q_used[17], resource_check)
    Toffoli_gate1(eng, q_used[8], q_used[3], q_used[16], resource_check)
    CNOT | (q_used[0], u1[5])
    CNOT2(eng, u1[7], u1[3], q_used[15])
    CNOT2(eng, q_used[11], q_used[10], q_used[14])
    CNOT2(eng, q_used[1], q_used[7], q_used[13])
    CNOT2(eng, q_used[1], q_used[4], q_used[12])
    CNOT | (u1[1], q_used[4])
    CNOT | (u1[0], u1[1])
    CNOT2(eng, q_used[0], u1[4], q_used[11])
    CNOT | (q_used[4], u1[4])
    CNOT | (u1[0], u1[4])
    CNOT2(eng, q_used[6], u1[3], q_used[10])
    CNOT | (u1[5], u1[3])
    CNOT | (u1[3], u1[6])
    CNOT2(eng, q_used[3], u1[6], q_used[9])
    CNOT2(eng, u1[7], q_used[2], q_used[8])
    CNOT | (u1[2], u1[5])
    CNOT | (u1[2], u1[6])
    CNOT2(eng, q_used[3], q_used[4], q_used[7])
    CNOT2(eng, u1[0], q_used[4], q_used[6])
    CNOT2(eng, u1[0], q_used[3], q_used[5])
    CNOT2(eng, u1[6], u1[5], q_used[4])
    CNOT2(eng, q_used[0], u1[3], q_used[3])
    CNOT | (u1[1], u1[3])
    CNOT2(eng, u1[4], u1[2], q_used[2])
    CNOT | (u1[1], u1[7])
    CNOT2(eng, u1[7], u1[2], q_used[1])
    CNOT2(eng, u1[7], u1[4], q_used[0])


    CNOT2(eng, u2[7], u2[4], new_q_used[0])
    CNOT2(eng, u2[7], u2[2], new_q_used[1])
    CNOT | (u2[1], u2[7])
    CNOT2(eng, u2[4], u2[2], new_q_used[2])
    CNOT | (u2[1], u2[3])
    CNOT2(eng, new_q_used[0], u2[3], new_q_used[3])
    CNOT2(eng, u2[6], u2[5], new_q_used[4])
    CNOT2(eng, u2[0], new_q_used[3], new_q_used[5])
    CNOT2(eng, u2[0], new_q_used[4], new_q_used[6])
    CNOT2(eng, new_q_used[3], new_q_used[4], new_q_used[7])
    CNOT | (u2[2], u2[6])
    CNOT | (u2[2], u2[5])
    CNOT2(eng, u2[7], new_q_used[2], new_q_used[8])
    CNOT2(eng, new_q_used[3], u2[6], new_q_used[9])
    CNOT | (u2[3], u2[6])
    CNOT | (u2[5], u2[3])
    CNOT2(eng, new_q_used[6], u2[3], new_q_used[10])
    CNOT | (u2[0], u2[4])
    CNOT | (new_q_used[4], u2[4])
    CNOT2(eng, new_q_used[0], u2[4], new_q_used[11])
    CNOT | (u2[0], u2[1])
    CNOT | (u2[1], new_q_used[4])
    CNOT2(eng, new_q_used[1], new_q_used[4], new_q_used[12])
    CNOT2(eng, new_q_used[1], new_q_used[7], new_q_used[13])
    CNOT2(eng, new_q_used[11], new_q_used[10], new_q_used[14])
    CNOT2(eng, u2[7], u2[3], new_q_used[15])
    CNOT | (new_q_used[0], u2[5])
    Toffoli_gate(eng, new_q_used[8], new_q_used[3], new_q_used[16], resource_check)
    Toffoli_gate(eng, new_q_used[12], new_q_used[5], new_q_used[17], resource_check)
    CNOT | (new_q_used[16], new_q_used[9])
    Toffoli_gate(eng, u2[4], u2[0], new_q_used[18], resource_check)
    CNOT | (new_q_used[18], new_q_used[16])
    Toffoli_gate(eng, u2[7], u2[3], new_q_used[19], resource_check)
    Toffoli_gate(eng, new_q_used[4], new_q_used[6], new_q_used[20], resource_check)
    CNOT | (new_q_used[19], new_q_used[15])
    Toffoli_gate(eng, new_q_used[11], new_q_used[10], new_q_used[21], resource_check)
    CNOT | (new_q_used[19], new_q_used[21])
    Toffoli_gate(eng, new_q_used[0], u2[6], new_q_used[22], resource_check)
    Toffoli_gate(eng, new_q_used[2], u2[5], new_q_used[23], resource_check)
    CNOT | (new_q_used[22], new_q_used[23])
    Toffoli_gate(eng, new_q_used[1], new_q_used[7], new_q_used[24], resource_check)
    CNOT | (new_q_used[22], new_q_used[24])
    CNOT | (new_q_used[17], new_q_used[9])
    CNOT | (new_q_used[13], new_q_used[16])
    CNOT | (new_q_used[20], new_q_used[15])
    CNOT | (new_q_used[24], new_q_used[21])
    CNOT | (new_q_used[23], new_q_used[9])
    CNOT | (new_q_used[24], new_q_used[16])
    CNOT | (new_q_used[23], new_q_used[15])
    CNOT | (new_q_used[14], new_q_used[21])
    CNOT2(eng, new_q_used[15], new_q_used[21], new_q_used[25])
    CNOT | (new_q_used[15], new_q_used[60])
    CNOT | (new_q_used[9], new_q_used[61])
    Toffoli_gate(eng, new_q_used[15], new_q_used[9], new_q_used[26], resource_check)
    Toffoli_gate(eng, new_q_used[61], new_q_used[21], new_q_used[32], resource_check)
    Toffoli_gate(eng, new_q_used[16], new_q_used[60], new_q_used[35], resource_check)
    CNOT | (new_q_used[25], new_q_used[63])
    CNOT2(eng, new_q_used[16], new_q_used[26], new_q_used[27])
    CNOT2(eng, new_q_used[9], new_q_used[16], new_q_used[28])
    CNOT | (new_q_used[28], new_q_used[62])
    CNOT2(eng, new_q_used[21], new_q_used[26], new_q_used[29])
    CNOT2(eng, new_q_used[28], new_q_used[26], new_q_used[34])
    Toffoli_gate(eng, new_q_used[29], new_q_used[28], new_q_used[30], resource_check)
    Toffoli_gate(eng, new_q_used[27], new_q_used[25], new_q_used[31], resource_check)
    Toffoli_gate(eng, new_q_used[62], new_q_used[32], new_q_used[33], resource_check)
    Toffoli_gate(eng, new_q_used[63], new_q_used[35], new_q_used[36], resource_check)
    CNOT | (new_q_used[25], new_q_used[26])
    CNOT | (new_q_used[30], new_q_used[16])
    CNOT | (new_q_used[34], new_q_used[33])
    CNOT | (new_q_used[31], new_q_used[21])
    CNOT | (new_q_used[26], new_q_used[36])
    CNOT2(eng, new_q_used[33], new_q_used[36], new_q_used[37])
    CNOT2(eng, new_q_used[16], new_q_used[21], new_q_used[38])
    CNOT2(eng, new_q_used[16], new_q_used[33], new_q_used[39])
    CNOT2(eng, new_q_used[21], new_q_used[36], new_q_used[40])
    CNOT2(eng, new_q_used[38], new_q_used[37], new_q_used[41])
    CNOT | (new_q_used[40], new_q_used[64])
    CNOT | (new_q_used[36], new_q_used[65])
    CNOT | (new_q_used[21], new_q_used[66])
    CNOT | (new_q_used[39], new_q_used[67])
    CNOT | (new_q_used[33], new_q_used[68])
    CNOT | (new_q_used[16], new_q_used[69])
    CNOT | (new_q_used[38], new_q_used[70])
    CNOT | (new_q_used[41], new_q_used[71])
    CNOT | (new_q_used[37], new_q_used[72])
    Toffoli_gate(eng, new_q_used[40], new_q_used[3], new_q_used[42], resource_check)
    Toffoli_gate(eng, new_q_used[36], new_q_used[5], new_q_used[43], resource_check)
    Toffoli_gate(eng, new_q_used[21], u2[0], new_q_used[44], resource_check)
    Toffoli_gate(eng, new_q_used[39], u2[3], new_q_used[45], resource_check)
    Toffoli_gate(eng, new_q_used[33], new_q_used[6], new_q_used[46], resource_check)
    Toffoli_gate(eng, new_q_used[16], new_q_used[10], new_q_used[47], resource_check)
    Toffoli_gate(eng, new_q_used[38], u2[6], new_q_used[48], resource_check)
    Toffoli_gate(eng, new_q_used[41], u2[5], new_q_used[49], resource_check)
    Toffoli_gate(eng, new_q_used[37], new_q_used[7], new_q_used[50], resource_check)
    Toffoli_gate(eng, new_q_used[64], new_q_used[8], new_q_used[51], resource_check)
    Toffoli_gate(eng, new_q_used[65], new_q_used[12], new_q_used[52], resource_check)
    Toffoli_gate(eng, new_q_used[66], u2[4], new_q_used[53], resource_check)
    Toffoli_gate(eng, new_q_used[67], u2[7], new_q_used[54], resource_check)
    Toffoli_gate(eng, new_q_used[68], new_q_used[4], new_q_used[55], resource_check)
    Toffoli_gate(eng, new_q_used[69], new_q_used[11], new_q_used[56], resource_check)
    Toffoli_gate(eng, new_q_used[70], new_q_used[0], new_q_used[57], resource_check)
    Toffoli_gate(eng, new_q_used[71], new_q_used[2], new_q_used[58], resource_check)
    Toffoli_gate(eng, new_q_used[72], new_q_used[1], new_q_used[59], resource_check)
    CNOT | (new_q_used[15], new_q_used[60])
    CNOT | (new_q_used[9], new_q_used[61])
    CNOT | (new_q_used[28], new_q_used[62])
    CNOT | (new_q_used[25], new_q_used[63])
    CNOT | (new_q_used[40], new_q_used[64])
    CNOT | (new_q_used[36], new_q_used[65])
    CNOT | (new_q_used[21], new_q_used[66])
    CNOT | (new_q_used[39], new_q_used[67])
    CNOT | (new_q_used[33], new_q_used[68])
    CNOT | (new_q_used[16], new_q_used[69])
    CNOT | (new_q_used[38], new_q_used[70])
    CNOT | (new_q_used[41], new_q_used[71])
    CNOT | (new_q_used[37], new_q_used[72])
    CNOT2(eng, new_q_used[57], new_q_used[58], new_q_used[60])
    CNOT2(eng, new_q_used[46], new_q_used[52], new_q_used[61])
    CNOT2(eng, new_q_used[42], new_q_used[44], new_q_used[62])
    CNOT2(eng, new_q_used[43], new_q_used[51], new_q_used[63])
    CNOT2(eng, new_q_used[50], new_q_used[54], new_q_used[64])
    CNOT2(eng, new_q_used[45], new_q_used[57], new_q_used[65])
    CNOT2(eng, new_q_used[58], new_q_used[65], new_q_used[66])
    CNOT2(eng, new_q_used[42], new_q_used[63], new_q_used[67])
    CNOT2(eng, new_q_used[47], new_q_used[55], new_q_used[68])
    CNOT2(eng, new_q_used[48], new_q_used[49], new_q_used[69])
    CNOT2(eng, new_q_used[49], new_q_used[64], new_q_used[70])
    CNOT2(eng, new_q_used[56], new_q_used[62], new_q_used[71])
    CNOT2(eng, new_q_used[44], new_q_used[47], new_q_used[72])
    CNOT2(eng, new_q_used[66], new_q_used[70], new_q_used[73])
    CNOT | (new_q_used[60], new_q_used[46])
    CNOT | (new_q_used[57], new_q_used[48])
    CNOT | (new_q_used[61], new_q_used[51])
    CNOT | (new_q_used[60], new_q_used[52])
    CNOT | (new_q_used[61], new_q_used[53])
    CNOT | (new_q_used[68], new_q_used[54])
    CNOT | (new_q_used[64], new_q_used[59])
    CNOT | (new_q_used[61], new_q_used[60])
    CNOT2(eng, new_q_used[61], new_q_used[67], s2[4])
    CNOT2(eng, new_q_used[63], new_q_used[72], s2[3])
    CNOT2(eng, new_q_used[54], new_q_used[62], s2[0])
    CNOT2(eng, new_q_used[51], new_q_used[69], s2[7])
    CNOT2(eng, new_q_used[67], new_q_used[69], s2[6])
    CNOT2(eng, new_q_used[68], new_q_used[70], s2[1])
    CNOT2(eng, new_q_used[71], new_q_used[48], s2[5])
    CNOT2(eng, new_q_used[71], new_q_used[53], s2[2])
    CNOT | (new_q_used[66], s2[7])
    CNOT | (new_q_used[52], s2[6])
    CNOT | (new_q_used[59], s2[5])
    X | s2[6]
    X | s2[5]
    CNOT | (new_q_used[66], s2[4])
    CNOT | (new_q_used[60], s2[3])
    CNOT | (new_q_used[73], s2[2])
    CNOT | (new_q_used[46], s2[1])
    CNOT | (new_q_used[66], s2[0])
    X | s2[1]
    X | s2[0]

    return (new_q_used, new_q_zero)


def allocation_input_qubits(INPUT, KEY, qinput, qkey):
    def hextobin(ahex):
        if ahex == '0':
            return '0000'
        elif ahex == '1':
            return '1000'
        elif ahex == '2':
            return '0100'
        elif ahex == '3':
            return '1100'
        elif ahex == '4':
            return '0010'
        elif ahex == '5':
            return '1010'
        elif ahex == '6':
            return '0110'
        elif ahex == '7':
            return '1110'
        elif ahex == '8':
            return '0001'
        elif ahex == '9':
            return '1001'
        elif ahex == 'A':
            return '0101'
        elif ahex == 'B':
            return '1101'
        elif ahex == 'C':
            return '0011'
        elif ahex == 'D':
            return '1011'
        elif ahex == 'E':
            return '0111'
        elif ahex == 'F':
            return '1111'
    for site in range(24):
        thisstr = KEY[site]
        binstr = hextobin(thisstr[1])
        binstr += hextobin(thisstr[0])
        for bit in range(8):
            if binstr[bit] == '1':
                X | qkey[8*site+bit]
    for site in range(16):
        thisstr = INPUT[site]
        binstr = hextobin(thisstr[1])
        binstr += hextobin(thisstr[0])
        for bit in range(8):
            if binstr[bit] == '1':
                X | qinput[8*site+bit]



def print_all_qubits(allqubits):
    def bintohex(abin4):
        if abin4 == '0000':
            return '0'
        elif abin4 == '1000':
            return '1'
        elif abin4 == '0100':
            return '2'
        elif abin4 == '1100':
            return '3'
        elif abin4 == '0010':
            return '4'
        elif abin4 == '1010':
            return '5'
        elif abin4 == '0110':
            return '6'
        elif abin4 == '1110':
            return '7'
        elif abin4 == '0001':
            return '8'
        elif abin4 == '1001':
            return '9'
        elif abin4 == '0101':
            return 'A'
        elif abin4 == '1101':
            return 'B'
        elif abin4 == '0011':
            return 'C'
        elif abin4 == '1011':
            return 'D'
        elif abin4 == '0111':
            return 'E'
        elif abin4 == '1111':
            return 'F'

    for each_qubits in allqubits:
        bit_str = ''
        hex_str = ''
        for i in range(len(each_qubits)):
            if i != 0 and i % 8 == 0:
                bit_str += ' '
            thisqubit = str(int(each_qubits[i]))
            bit_str += thisqubit
        print(bit_str)

        hexnum = len(bit_str) // 9
        for thishex in range(hexnum + 1):
            thisstr = bit_str[thishex*9:thishex*9+8]
            hex_str += bintohex(thisstr[4:8])
            hex_str += bintohex(thisstr[0:4])
            hex_str += ' '
        print(hex_str)
    # i = 0
    # for each_qubits in allqubits:
    #     if i in [1,3,5,7,9,11,13,15,17,19,21,23]:
    #         bit_str = ''
    #         for i in range(len(each_qubits)):
    #             if i != 0 and i % 8 == 0:
    #                 bit_str += ' '
    #             thisqubit = str(int(each_qubits[i]))
    #             bit_str += thisqubit
    #         print(bit_str)
    #     i += 1


def swap8(value1, value2, tem_qubit8):
    for i in range(8):
        CNOT | (value1[i], tem_qubit8[i])
    for i in range(8):
        CNOT | (tem_qubit8[i], value1[i])
    for i in range(8):
        CNOT | (value2[i], value1[i])
    for i in range(8):
        CNOT | (value1[i], value2[i])
    for i in range(8):
        CNOT | (tem_qubit8[i], value2[i])
    for i in range(8):
        CNOT | (value2[i], tem_qubit8[i])

def swap1(qubit1, qubit2, tem_qubit):
    CNOT | (qubit1, tem_qubit)
    CNOT | (tem_qubit, qubit1)
    CNOT | (qubit2, qubit1)
    CNOT | (qubit1, qubit2)
    CNOT | (tem_qubit, qubit2)
    CNOT | (qubit2, tem_qubit)

def Mixcolumn(x0, x1, x2, x3, onequbit):
    # Changing the index of qubits
    x = []
    for i in range(8):
        x.append(x0[i])
    for i in range(8):
        x.append(x1[i])
    for i in range(8):
        x.append(x2[i])
    for i in range(8):
        x.append(x3[i])

    CNOT | (x[23], x[31])
    CNOT | (x[8], x[24])
    CNOT | (x[29], x[21])
    CNOT | (x[18], x[26])
    CNOT | (x[17], x[1])
    CNOT | (x[3], x[11])
    CNOT | (x[2], x[10])
    CNOT | (x[20], x[28])
    CNOT | (x[22], x[14])
    CNOT | (x[19], x[27])
    CNOT | (x[5], x[13])
    CNOT | (x[7], x[23])
    CNOT | (x[1], x[25])
    CNOT | (x[6], x[22])
    CNOT | (x[4], x[20])
    CNOT | (x[9], x[17])
    CNOT | (x[13], x[29])
    CNOT | (x[28], x[12])
    CNOT | (x[15], x[7])
    CNOT | (x[23], x[8])
    CNOT | (x[25], x[9])
    CNOT | (x[12], x[4])
    CNOT | (x[13], x[6])
    CNOT | (x[17], x[2])
    CNOT | (x[28], x[5])
    CNOT | (x[8], x[25])
    CNOT | (x[7], x[16])
    CNOT | (x[11], x[12])
    CNOT | (x[13], x[30])
    CNOT | (x[14], x[15])
    CNOT | (x[28], x[29])
    CNOT | (x[23], x[17])
    CNOT | (x[0], x[8])
    CNOT | (x[27], x[11])
    CNOT | (x[21], x[13])
    CNOT | (x[14], x[30])
    CNOT | (x[17], x[18])
    CNOT | (x[23], x[28])
    CNOT | (x[31], x[0])
    CNOT | (x[5], x[14])
    CNOT | (x[2], x[27])
    CNOT | (x[20], x[21])
    CNOT | (x[19], x[28])
    CNOT | (x[24], x[17])
    CNOT | (x[24], x[0])
    CNOT | (x[29], x[14])
    CNOT | (x[18], x[27])
    CNOT | (x[12], x[20])
    CNOT | (x[26], x[2])
    CNOT | (x[3], x[28])
    CNOT | (x[4], x[5])
    CNOT | (x[23], x[18])
    CNOT | (x[11], x[20])
    CNOT | (x[26], x[19])
    CNOT | (x[10], x[3])
    CNOT | (x[7], x[12])
    CNOT | (x[16], x[24])
    CNOT | (x[30], x[23])
    CNOT | (x[1], x[26])
    CNOT | (x[10], x[18])
    CNOT | (x[7], x[3])
    CNOT | (x[31], x[20])
    CNOT | (x[12], x[4])
    CNOT | (x[15], x[23])
    CNOT | (x[9], x[18])
    CNOT | (x[1], x[10])
    CNOT | (x[31], x[7])
    CNOT | (x[28], x[4])
    CNOT | (x[6], x[23])
    CNOT | (x[25], x[1])
    CNOT | (x[31], x[19])
    CNOT | (x[7], x[17])
    CNOT | (x[2], x[10])
    CNOT | (x[20], x[28])
    CNOT | (x[18], x[26])
    CNOT | (x[22], x[31])
    CNOT | (x[16], x[25])
    CNOT | (x[14], x[6])
    CNOT | (x[11], x[19])
    CNOT | (x[0], x[1])
    CNOT | (x[13], x[22])
    CNOT | (x[7], x[16])
    CNOT | (x[3], x[11])
    CNOT | (x[1], x[9])
    CNOT | (x[30], x[22])
    CNOT | (x[5], x[13])
    CNOT | (x[15], x[7])
    CNOT | (x[8], x[16])
    CNOT | (x[27], x[3])
    CNOT | (x[17], x[1])
    CNOT | (x[22], x[14])
    CNOT | (x[21], x[5])
    CNOT | (x[31], x[15])
    CNOT | (x[19], x[27])
    CNOT | (x[24], x[8])
    CNOT | (x[25], x[17])
    CNOT | (x[23], x[31])
    CNOT | (x[29], x[21])

    xvalues = [16, 1, 10, 11, 12, 13, 30, 15,
               8, 25, 2, 3, 4, 5, 14, 7,
               24, 17, 26, 19, 20, 29, 22, 31,
               0, 9, 18, 27, 28, 21, 6, 23]
    standardvalues = []
    for i in range(32):
        standardvalues.append(i)
    if CHECK_CIRCUIT_RIGHT == 1:
        while xvalues != standardvalues:
            find = 0
            for line in range(32):
                if xvalues[line] != standardvalues[line]:
                    for newline in range(line, 32):
                        if xvalues[newline] == line:
                            xvalues[line], xvalues[newline] = xvalues[newline], xvalues[line]
                            swap1(x[line], x[newline], onequbit)
                            find = 1
                            break
                    if find == 1:
                        break

def Mixcolumn_xiang_30_92(x0, x1, x2, x3, onequbit):
    # Changing the index of qubits
    x = []
    for i in range(8):
        x.append(x0[i])
    for i in range(8):
        x.append(x1[i])
    for i in range(8):
        x.append(x2[i])
    for i in range(8):
        x.append(x3[i])

    CNOT | (x[31], x[23]);
    CNOT | (x[15], x[31])
    CNOT | (x[4], x[12]);
    CNOT | (x[21], x[13])
    CNOT | (x[9], x[17]);
    CNOT | (x[27], x[11])
    CNOT | (x[28], x[4]);
    CNOT | (x[5], x[21])
    CNOT | (x[24], x[0]);
    CNOT | (x[7], x[15])
    CNOT | (x[1], x[9]);
    CNOT | (x[6], x[14])
    CNOT | (x[16], x[24]);
    CNOT | (x[22], x[6])
    CNOT | (x[31], x[16]);
    CNOT | (x[8], x[24])
    CNOT | (x[26], x[18]);
    CNOT | (x[30], x[22])
    CNOT | (x[10], x[26]);
    CNOT | (x[23], x[8])
    CNOT | (x[13], x[30]);
    CNOT | (x[29], x[13])
    CNOT | (x[13], x[5]);
    CNOT | (x[4], x[29])
    CNOT | (x[11], x[4]);
    CNOT | (x[19], x[11])
    CNOT | (x[12], x[13]);
    CNOT | (x[23], x[19])
    CNOT | (x[31], x[4]);
    CNOT | (x[20], x[12])
    CNOT | (x[12], x[28]);
    CNOT | (x[27], x[20])
    CNOT | (x[19], x[20]);
    CNOT | (x[31], x[27])
    CNOT | (x[15], x[12]);
    CNOT | (x[3], x[27])
    CNOT | (x[11], x[3]);
    CNOT | (x[2], x[11])
    CNOT | (x[18], x[19]);
    CNOT | (x[10], x[11])
    CNOT | (x[18], x[10]);
    CNOT | (x[2], x[18])
    CNOT | (x[9], x[10]);
    CNOT | (x[9], x[2])
    CNOT | (x[17], x[18]);
    CNOT | (x[25], x[17])
    CNOT | (x[17], x[1]);
    CNOT | (x[24], x[25])
    CNOT | (x[8], x[9]);
    CNOT | (x[15], x[24])
    CNOT | (x[15], x[11]);
    CNOT | (x[0], x[8])
    CNOT | (x[23], x[15]);
    CNOT | (x[16], x[17])
    CNOT | (x[0], x[16]);
    CNOT | (x[31], x[0])
    CNOT | (x[23], x[16]);
    CNOT | (x[6], x[23])
    CNOT | (x[7], x[31]);
    CNOT | (x[22], x[31])
    CNOT | (x[6], x[30]);
    CNOT | (x[14], x[7])
    CNOT | (x[21], x[14]);
    CNOT | (x[5], x[6])
    CNOT | (x[21], x[22]);
    CNOT | (x[29], x[5])
    CNOT | (x[28], x[21]);
    CNOT | (x[21], x[29])
    CNOT | (x[13], x[21]);
    CNOT | (x[27], x[12])
    CNOT | (x[26], x[27]);
    CNOT | (x[20], x[28])
    CNOT | (x[4], x[20]);
    CNOT | (x[1], x[26])
    CNOT | (x[30], x[14]);
    CNOT | (x[12], x[4])
    CNOT | (x[19], x[3]);
    CNOT | (x[27], x[19])
    CNOT | (x[25], x[1]);
    CNOT | (x[24], x[0])
    CNOT | (x[0], x[1]);
    CNOT | (x[26], x[2])
    CNOT | (x[9], x[25]);
    CNOT | (x[7], x[15])
    CNOT | (x[23], x[7]);
    CNOT | (x[14], x[6])
    CNOT | (x[17], x[9]);
    CNOT | (x[31], x[23])
    CNOT | (x[18], x[26]);
    CNOT | (x[6], x[22])
    CNOT | (x[0], x[17]);
    CNOT | (x[11], x[27])

    xvalues = [24, 25, 18, 19, 4, 29, 22, 15,
               16, 9, 2, 3, 28, 5, 6, 7,
               8, 1, 10, 11, 12, 21, 30, 31,
               0, 17, 26, 27, 20, 13, 14, 23]
    standardvalues = []
    for i in range(32):
        standardvalues.append(i)
    if CHECK_CIRCUIT_RIGHT == 1:
        while xvalues != standardvalues:
            find = 0
            for line in range(32):
                if xvalues[line] != standardvalues[line]:
                    for newline in range(line, 32):
                        if xvalues[newline] == line:
                            xvalues[line], xvalues[newline] = xvalues[newline], xvalues[line]
                            swap1(x[line], x[newline], onequbit)
                            find = 1
                            break
                    if find == 1:
                        break


def ShiftRow(values, tem_qubit8):
    assert len(values) == 16

    # 1 5 9 13 -> 5 9 13 1
    swap8(values[1], values[5], tem_qubit8)  # 5 1 9 13
    swap8(values[5], values[9], tem_qubit8)  # 5 9 1 13
    swap8(values[9], values[13], tem_qubit8)  # 5 9 13 1

    # 2 6 10 14 -> 10 14 2 6
    swap8(values[2], values[10], tem_qubit8)
    swap8(values[6], values[14], tem_qubit8)

    # 3 7 11 15 -> 15 3 7 11
    swap8(values[11], values[15], tem_qubit8)  # 3 7 15 11
    swap8(values[7], values[11], tem_qubit8)  # 3 15 7 11
    swap8(values[3], values[7], tem_qubit8)  # 15 3 7 11

    return values

def split_num(values, num):
    outputvalues = []
    for i in range(num):
        outputvalues.append(values[i*8:i*8+8])
    return outputvalues

def combine16(values):
    onevalue = []
    for value in values:
        for bit in value:
            onevalue.append(bit)
    return onevalue

def round0_addkey(input, key):
    for i in range(128):
        CNOT | (key[i], input[i])

def round1_nocombine(middle_mc, input, key, output, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3):

    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site+20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        Sbox_opt(eng, Sbox_inputs[site], q_inputs[site], Sbox_outputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        Sbox_opt(eng, q_ancli_for_key_w3_values[site], q_keys[site], Key_outputs[site], RESOURCE_CHECK)
    all_q_inputs_used = []
    all_q_inputs_zero = []
    for site in range(16):
        q_inputs_used = []
        q_inputs_zero = []
        for i in range(74):
            q_inputs_used.append(q_inputs[site][i])
        for i in range(74, 98):
            q_inputs_zero.append(q_inputs[site][i])
        all_q_inputs_used.append(q_inputs_used)
        all_q_inputs_zero.append(q_inputs_zero)
    all_q_keys_used = []
    all_q_keys_zero = []
    for site in range(0, 4):
        q_keys_used = []
        q_keys_zero = []
        for i in range(74):
            q_keys_used.append(q_keys[site][i])
        for i in range(74, 98):
            q_keys_zero.append(q_keys[site][i])
        all_q_keys_used.append(q_keys_used)
        all_q_keys_zero.append(q_keys_zero)


    X | Key_inputs[0][0]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site+4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site+4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1], mc_outputs[2], mc_outputs[3])
    XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5], mc_outputs[6], mc_outputs[7])
    XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9], mc_outputs[10], mc_outputs[11])
    XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13], mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])


    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)


def round_combine2(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass

    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine3(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][1]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])
    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])


    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine4(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][2]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])
    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass

    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])


    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine5(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass

    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])
    #
    #
    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine6(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][3]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])
    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine7(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)


    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])


    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)


    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][4]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine8(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])
    #
    #
    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine9(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][5]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])
    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine10(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)

    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][6]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])
    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass

    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    # w9 + w4 -> w10
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine11(round, middle_mc, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    mc_outputs = split_num(output, 16)  # next round values
    Sbox_outputs = split_num(middle_mc, 16)
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(16, 24):  # 4 5
        Key_used_in_this_round.append(allkeyset[i])

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        XOR105(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], mc_outputs[0], mc_outputs[1],
               mc_outputs[2], mc_outputs[3])
        XOR105(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], mc_outputs[4], mc_outputs[5],
               mc_outputs[6], mc_outputs[7])
        XOR105(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], mc_outputs[8], mc_outputs[9],
               mc_outputs[10], mc_outputs[11])
        XOR105(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], mc_outputs[12], mc_outputs[13],
               mc_outputs[14], mc_outputs[15])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], mc_outputs[site][bit])

    output = combine16(mc_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)

def round_combine12(round, input, key, output, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero, q_inputs, q_keys, tem_shift_qubit, q_ancli_for_key_w3, prior_input, prior_ancli_for_w3):

    prior_inputs = split_num(prior_input, 16)
    Sbox_inputs = split_num(input, 16)  # 16 Sboxes
    Sbox_outputs = split_num(output, 16)  # next round values
    allkeyset = split_num(key, 24)
    Key_used_in_this_round = []
    for i in range(0, 8):  # 0 1
        Key_used_in_this_round.append(allkeyset[i])
    for i in range(8, 16):  # 2 3
        Key_used_in_this_round.append(allkeyset[i])
    Key_inputs = split_num(key, 24)
    Key_outputs = [Key_inputs[0], Key_inputs[1], Key_inputs[2], Key_inputs[3]]
    q_ancli_for_key_w3_values = split_num(q_ancli_for_key_w3, 4)
    prior_ancli_for_w3_values = split_num(prior_ancli_for_w3, 4)


    for site in range(4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 20][bit], q_ancli_for_key_w3_values[site][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        swap8(q_ancli_for_key_w3_values[0], q_ancli_for_key_w3_values[1], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[1], q_ancli_for_key_w3_values[2], tem_shift_qubit)
        swap8(q_ancli_for_key_w3_values[2], q_ancli_for_key_w3_values[3], tem_shift_qubit)

    for site in range(16):
        all_q_inputs_used[site], all_q_inputs_zero[site] = Sbox_combine(eng, prior_inputs[site], Sbox_inputs[site], Sbox_outputs[site], all_q_inputs_used[site], all_q_inputs_zero[site], q_inputs[site], RESOURCE_CHECK)
    for site in range(0, 4):
        all_q_keys_used[site], all_q_keys_zero[site] = Sbox_combine(eng, prior_ancli_for_w3_values[site], q_ancli_for_key_w3_values[site], Key_outputs[site], all_q_keys_used[site], all_q_keys_zero[site], q_keys[site], RESOURCE_CHECK)


    X | Key_inputs[0][7]
    # w6 + w1 -> w7
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site][bit], Key_inputs[site + 4][bit])
    # w7 + w2 -> w8
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 4][bit], Key_inputs[site + 8][bit])
    # w8 + w3 -> w9
    for site in range(0, 4):
        for bit in range(8):
            CNOT | (Key_inputs[site + 8][bit], Key_inputs[site + 12][bit])

    if CHECK_CIRCUIT_RIGHT == 1:
        Sbox_outputs = ShiftRow(Sbox_outputs, tem_shift_qubit)
    else:
        pass


    if round < 12:
        Mixcolumn(Sbox_outputs[0], Sbox_outputs[1], Sbox_outputs[2], Sbox_outputs[3], tem_shift_qubit[0])
        Mixcolumn(Sbox_outputs[4], Sbox_outputs[5], Sbox_outputs[6], Sbox_outputs[7], tem_shift_qubit[0])
        Mixcolumn(Sbox_outputs[8], Sbox_outputs[9], Sbox_outputs[10], Sbox_outputs[11], tem_shift_qubit[0])
        Mixcolumn(Sbox_outputs[12], Sbox_outputs[13], Sbox_outputs[14], Sbox_outputs[15], tem_shift_qubit[0])

    for site in range(0, 16):
        for bit in range(8):
            CNOT | (Key_used_in_this_round[site][bit], Sbox_outputs[site][bit])
    if round < 12:
    # w9 + w4 -> w10
        for site in range(0, 4):
            for bit in range(8):
                CNOT | (Key_inputs[site + 12][bit], Key_inputs[site + 16][bit])
        # w8 + w3 -> w9
        for site in range(0, 4):
            for bit in range(8):
                CNOT | (Key_inputs[site + 16][bit], Key_inputs[site + 20][bit])

    output = combine16(Sbox_outputs)

    return (all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero)


#*******************************************************
CHECK_CIRCUIT_RIGHT = 0
# 1: test
# 0: resource estimation

RESOURCE_CHECK = 1

if CHECK_CIRCUIT_RIGHT == 1 and RESOURCE_CHECK == 1:
    RESOURCE_CHECK = 0


#******************** test vector ******************************
"""
0 4 8  12
1 5 9  13
2 6 10 14
3 7 11 15
"""

KEY = [
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
]
INPUT = [
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
    '12', '34', '56', '78',
]
#OUTPUT: 09c86188 05643634 059fbe2d 6fbadff4


if CHECK_CIRCUIT_RIGHT == 1:
    eng = MainEngine(backend=ClassicalSimulator())
else:
    circuit_backend = _resource.ResourceCounter()
    eng = MainEngine(backend=circuit_backend)

if __name__ == "__main__":


    key_qubits = eng.allocate_qureg(192)
    input_qibuts = eng.allocate_qureg(128)
    middle_mc_set = [0 for i in range(12)]
    for i in range(12):
        middle_mc_set[i] = eng.allocate_qureg(128)

    q_block0 = eng.allocate_qureg(98)
    q_block1 = eng.allocate_qureg(98)
    q_block2 = eng.allocate_qureg(98)
    q_block3 = eng.allocate_qureg(98)
    q_block4 = eng.allocate_qureg(98)
    q_block5 = eng.allocate_qureg(98)
    q_block6 = eng.allocate_qureg(98)
    q_block7 = eng.allocate_qureg(98)
    q_block8 = eng.allocate_qureg(98)
    q_block9 = eng.allocate_qureg(98)
    q_block10 = eng.allocate_qureg(98)
    q_block11 = eng.allocate_qureg(98)
    q_block12 = eng.allocate_qureg(98)
    q_block13 = eng.allocate_qureg(98)
    q_block14 = eng.allocate_qureg(98)
    q_block15 = eng.allocate_qureg(98)

    q_key0 = eng.allocate_qureg(98)
    q_key1 = eng.allocate_qureg(98)
    q_key2 = eng.allocate_qureg(98)
    q_key3 = eng.allocate_qureg(98)

    all_q_ancli_for_key_w3 = eng.allocate_qureg(32*8)


    allqbits_block = [q_block0, q_block1, q_block2, q_block3, q_block4, q_block5, q_block6, q_block7,
                      q_block8, q_block9, q_block10, q_block11, q_block12, q_block13, q_block14, q_block15]
    allqbits_key = [q_key0, q_key1, q_key2, q_key3]

    round1_qubits = eng.allocate_qureg(128)
    round2_qubits = eng.allocate_qureg(128)
    round3_qubits = eng.allocate_qureg(128)
    round4_qubits = eng.allocate_qureg(128)
    round5_qubits = eng.allocate_qureg(128)
    round6_qubits = eng.allocate_qureg(128)
    round7_qubits = eng.allocate_qureg(128)
    round8_qubits = eng.allocate_qureg(128)
    round9_qubits = eng.allocate_qureg(128)
    round10_qubits = eng.allocate_qureg(128)
    round11_qubits = eng.allocate_qureg(128)
    round12_qubits = eng.allocate_qureg(128)



    # allqubits = [key_qubits, input_qibuts, round1_qubits, round2_qubits, round3_qubits, round4_qubits, round5_qubits, round6_qubits, round7_qubits, round8_qubits, round9_qubits, round10_qubits, round11_qubits, round12_qubits]
    allqubits = [round12_qubits]


    if CHECK_CIRCUIT_RIGHT == 1:
        tem_shift_qubit = eng.allocate_qureg(8)
    else:
        tem_shift_qubit = [-1, -1, -1, -1, -1, -1, -1, -1]


    if CHECK_CIRCUIT_RIGHT == 1:
        allocation_input_qubits(INPUT, KEY, input_qibuts, key_qubits)



    print("round 0")
    round0_addkey(input_qibuts, key_qubits[0:128])
    print("round 1")
    all_q_inputs_used, all_q_inputs_zero, all_q_keys_used, all_q_keys_zero = round1_nocombine(middle_mc_set[0], input_qibuts, key_qubits,
                                                                                              round1_qubits, allqbits_block,
                                                                                              allqbits_key, tem_shift_qubit,
                                                                                              all_q_ancli_for_key_w3[0:32])
    print("round 2")
    round_combine2(2, middle_mc_set[1], round1_qubits, key_qubits, round2_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  -1, input_qibuts, -1)
    print("round 3")
    round_combine3(3, middle_mc_set[2], round2_qubits, key_qubits, round3_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 1:32 * 1 + 32], round1_qubits, all_q_ancli_for_key_w3[32 * 0:32 * 0 + 32])
    print("round 4")
    round_combine4(4, middle_mc_set[3], round3_qubits, key_qubits, round4_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 2:32 * 2 + 32], round2_qubits, all_q_ancli_for_key_w3[32 * 1:32 * 1 + 32])
    print("round 5")
    round_combine5(5, middle_mc_set[4], round4_qubits, key_qubits, round5_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  -1, round3_qubits, -1)
    print("round 6")
    round_combine6(6, middle_mc_set[5], round5_qubits, key_qubits, round6_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 3:32 * 3 + 32], round4_qubits, all_q_ancli_for_key_w3[32 * 2:32 * 2 + 32])
    print("round 7")
    round_combine7(7, middle_mc_set[6], round6_qubits, key_qubits, round7_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 4:32 * 4 + 32], round5_qubits, all_q_ancli_for_key_w3[32 * 3:32 * 3 + 32])
    print("round 8")
    round_combine8(8, middle_mc_set[7], round7_qubits, key_qubits, round8_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  -1, round6_qubits, -1)
    print("round 9")
    round_combine9(9, middle_mc_set[8], round8_qubits, key_qubits, round9_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 5:32 * 8 + 32], round7_qubits, all_q_ancli_for_key_w3[32 * 4:32 * 4 + 32])
    print("round 10")
    round_combine10(10, middle_mc_set[9], round9_qubits, key_qubits, round10_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 6:32 * 6 + 32], round8_qubits, all_q_ancli_for_key_w3[32 * 5:32 * 5 + 32])
    print("round 11")
    round_combine11(11, middle_mc_set[10], round10_qubits, key_qubits, round11_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  -1, round9_qubits, -1)
    print("round 12")
    round_combine12(12, round11_qubits, key_qubits, round12_qubits, all_q_inputs_used, all_q_inputs_zero, all_q_keys_used,
                  all_q_keys_zero, allqbits_block, allqbits_key, tem_shift_qubit,
                  all_q_ancli_for_key_w3[32 * 7:32 * 7 + 32], round10_qubits, all_q_ancli_for_key_w3[32 * 6:32 * 6 + 32])


    if CHECK_CIRCUIT_RIGHT == 1:
        for thisvar in allqubits:
            All(Measure) | thisvar


    if CHECK_CIRCUIT_RIGHT == 1:
        eng.flush()
    else:
        # eng.flush()
        eng.flush(deallocate_qubits=True)


    if CHECK_CIRCUIT_RIGHT == 1:
        print_all_qubits(allqubits)
    else:
        print(circuit_backend)
        print("depth_of_dag: {}".format(circuit_backend.depth_of_dag))




