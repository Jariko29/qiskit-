import os

from qiskit_ibm_runtime import QiskitRuntimeService

api_key = os.environ["IBM_QUANTUM_API_KEY"]
instance = os.environ["IBM_QUANTUM_INSTANCE"]

service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=api_key,
    instance=instance
)

print("Successfully connected to IBM Quantum!")