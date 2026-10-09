import math
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister,generate_preset_pass_manager
from qiskit.circuit.library import grover_operator, MCMTGate, ZGate
from qiskit.visualization import plot_distribution,plot_histogram
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def run_circuit_and_get_counts(circuit, backend, shots=int):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(circuit)
    result = backend.run(isa_circuit, shots=shots).result()
    return result.get_counts()

def grover_oracle(deimos_states):
    if not isinstance(deimos_states, list):
        deimos_states = [deimos_states]
    num_qbits = len(deimos_states[0])
    qc = QuantumCircuit(num_qbits)
    for target in deimos_states:
        rev_deimos = target[::-1]
        zero_ind = [ind for ind in range(num_qbits) if rev_deimos.startswith('0', ind)]
        print(f"Zero indices for target {target}: {zero_ind}")
        qc.x(zero_ind)
        qc.compose(MCMTGate(ZGate(), num_qbits - 1, 1), inplace = True)
        qc.x(zero_ind)
    return qc

deimos_state = '1110'
oracle = grover_oracle(deimos_state)
oracle.draw(output='mpl', style='iqp', filename='grover_oracle.png')

backend = AerSimulator()
counts = run_circuit_and_get_counts(oracle, backend, shots=3000)
fig = plot_histogram(counts)
plt.savefig("grover_oracle_histogram.png")