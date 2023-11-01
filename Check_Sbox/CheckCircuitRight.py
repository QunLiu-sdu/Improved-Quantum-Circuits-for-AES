


class SboxOpt:
    def __init__(self):
        self.QuantumCircuit = []

    def Initial(self, file="QuantumCircuit.txt"):
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                if line == '':
                    continue

                if line[0] == 'X':
                    name = 'X'
                    shugang = -1
                    for bit in range(len(line)):
                        if line[bit] == '|':
                            shugang = bit
                            break
                    node1 = line[shugang+2:]
                    self.QuantumCircuit.append([name, node1])
                    continue
                if line[0:5] == "CNOT2":
                    name = "CNOT2"
                    alldouhao = []
                    for bit in range(len(line)):
                        if line[bit] == ',':
                            alldouhao.append(bit)

                    node1 = line[alldouhao[0] + 2:alldouhao[1]]
                    node2 = line[alldouhao[1] + 2:alldouhao[2]]
                    node3 = line[alldouhao[2] + 2:-1]
                    self.QuantumCircuit.append([name, node1, node2, node3])
                    continue
                if line[0] == "T":
                    name = line[0:12]
                    alldouhao = []
                    for bit in range(len(line)):
                        if line[bit] == ',':
                            alldouhao.append(bit)
                    node1 = line[alldouhao[0] + 2:alldouhao[1]]
                    node2 = line[alldouhao[1] + 2:alldouhao[2]]
                    node3 = line[alldouhao[2] + 2:alldouhao[3]]
                    self.QuantumCircuit.append([name, node1, node2, node3])
                    continue
                if line[0] == "C":
                    name = "CNOT"
                    zuokuo = -1
                    douhao = -1
                    for bit in range(len(line)):
                        if line[bit] == '(':
                            zuokuo = bit
                        if line[bit] == ',':
                            douhao = bit
                    node1 = line[zuokuo+1:douhao]
                    node2 = line[douhao+2:-1]
                    self.QuantumCircuit.append([name, node1, node2])
                    continue

    def CheckSboxRight(self):
        from SBoxCircuit import testSBox
        # from StantardSBoxCircuit import StantardSBox
        from StantardSBoxCircuit_depth6 import StantardSBox

        RC = [1, 2, 4, 8, 16, 32, 64, 128]

        SuccessNum = 0

        allResult = list()

        for X in range(0, 256):
            u = list()
            for ii in range(8):
                u.append((X >> ii) & 1)
            s = testSBox(u)
            u = list()
            for ii in range(8):
                u.append((X >> ii) & 1)
            Stantard_s = StantardSBox(u)
            str_s = ''
            str_stan = ''
            num = s[7] * 8 + s[6] * 4 + s[5] * 2 + s[4] * 1
            str_num = hex(num)[2:]
            str_s += str_num
            num = s[3]*8 + s[2]*4 + s[1]*2 + s[0]*1
            str_num = hex(num)[2:]
            str_s += str_num

            num = Stantard_s[7] * 8 + Stantard_s[6] * 4 + Stantard_s[5] * 2 + Stantard_s[4] * 1
            str_num = hex(num)[2:]
            str_stan += str_num
            num = Stantard_s[3] * 8 + Stantard_s[2] * 4 + Stantard_s[1] * 2 + Stantard_s[0] * 1
            str_num = hex(num)[2:]
            str_stan += str_num


            print("s: {}   STAN: {}  str_s:{} str_stan:{}".format(s, Stantard_s, str_s, str_stan))
            if s == Stantard_s:
                SuccessNum += 1
            SboxOutput = 0
            for i in range(8):
                if s[i] == 1:
                    SboxOutput += RC[i]
            SboxOutput = hex(SboxOutput)
            allResult.append(SboxOutput)

        if SuccessNum == 256:
            return 0
        else:
            return -1

    def PrintFromQuantumToCircuit(self, QuantumCircuit):
        with open('SBoxCircuit.py', 'w') as f:
            f.write("def testSBox(u):\n")
            f.write("\tt = list()\n")
            f.write("\tm = list()\n")
            f.write("\tl = list()\n")
            f.write("\ts = list()\n")
            f.write("\tn = list()\n")
            f.write("\tw = list()\n")
            f.write("\tq = list()\n")
            f.write("\tfor i in range(8):\n")
            f.write("\t\ts.append(0)\n")
            f.write("\tfor i in range(200):\n")
            f.write("\t\tt.append(0)\n")
            f.write("\t\tm.append(0)\n")
            f.write("\t\tl.append(0)\n")
            f.write("\t\tn.append(0)\n")
            f.write("\t\tw.append(0)\n")
            f.write("\t\tq.append(0)\n")

            for XOR in QuantumCircuit:
                if XOR[0] == "CNOT2":
                    f.write("\t{0} = {0} ^ {1} ^ {2}\n".format(XOR[3], XOR[1], XOR[2]))

                if XOR[0] == "Toffoli_gate":
                    f.write("\t{} = ({} & {}) ^ {}\n".format(XOR[3], XOR[1], XOR[2], XOR[3]))

                if XOR[0] == "X":
                    f.write("\t{0} = 1 ^ {0}\n".format(XOR[1]))

                if XOR[0] == "CNOT":
                    f.write("\t{} = {} ^ {}\n".format(XOR[2], XOR[1], XOR[2]))

            f.write("\n\treturn s\n")

    def PrintQuantum(self, QuantumCircuit, file='NewQuantumCircuit.txt'):
        with open(file, 'w') as f:
            for XOR in QuantumCircuit:
                if XOR[0] == "CNOT2":
                    f.write("{}(eng, {}, {}, {})\n".format(XOR[0], XOR[1], XOR[2], XOR[3]))

                if XOR[0] == "Toffoli_gate":
                    f.write("{}(eng, {}, {}, {}, resource_check)\n".format(XOR[0], XOR[1], XOR[2], XOR[3]))

                if XOR[0] == "X":
                    f.write("X | {}\n".format(XOR[1]))

                if XOR[0] == "CNOT":
                    f.write("CNOT | ({}, {})\n".format(XOR[1], XOR[2]))



if __name__ == "__main__":
    test = SboxOpt()
    test.Initial("QuantumCircuit.txt")
    test.PrintFromQuantumToCircuit(test.QuantumCircuit)

    isright = test.CheckSboxRight()
    if isright != 0:
        print("check right fail")
    else:
        print("check right!")

