This is the code for the paper: Improved Quantum Circuits for AES: Reducing the Depth and the Number of Qubits accepted by ASIACRYPT 2023.

### Check S-box

We provide the S-box circuits.

"S-box with 60 ancilla qubits.txt" and "S-box with 74 ancilla qubits.txt" contain the circuits.

"CheckQuantumCost.py": runs the resource estimation.

"CheckCircuitRight.py": verifies the S-box circuits, where the circuit is put into "QuantumCircuit.txt".

### Check MixColumns

We provide the in-place circuit with depth 16.

"Check_MC_Depth_16.py": runs the resource estimation.

### Quantum Circuits (Thanks for the code snippets from Paper Quantum Analysis of AES eprint 2022/683.)

In "TestVector", we provide the test of the quantum circuit for AES-128, 192, and -256.

In "ResourceEstimitation", we provide the quantum circuits with different types.
