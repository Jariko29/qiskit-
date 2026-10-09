from qiskit import QuantumCircuit, generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_circuit_and_get_counts(circuit, backend, shots=int):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(circuit)
    result = backend.run(isa_circuit, shots=shots).result()
    return result.get_counts()

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.h(1)
qc.cx(1, 2)
qc.measure_all()
print(qc)
qc.draw(output="mpl", filename="bell_circuit_3q.png")
backend = AerSimulator()
counts = run_circuit_and_get_counts(qc, backend, shots=3000)

fig = plot_histogram(counts)
fig.savefig("bell_histogram_3q.png")
plt.show()

qc = QuantumCircuit(4,4)
qc.h(0)
qc.cx(0, 1)
qc.h(1)
qc.barrier()
qc.measure(2, 0)
qc.cx(1, 2)
qc.h(2)
qc.cx(2, 3)
qc.barrier()
qc.measure(0, 1)

print(qc)
qc.draw(output="mpl", filename="bell_circuit_4q.png")
backend = AerSimulator()
counts = run_circuit_and_get_counts(qc, backend, shots=3000)

fig = plot_histogram(counts)
fig.savefig("bell_histogram_4q.png")
plt.show()