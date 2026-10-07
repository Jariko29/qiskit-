import os

from qiskit_ibm_runtime import QiskitRuntimeService

api_key = os.environ["IBM_QUANTUM_API_KEY"]
instance = os.environ["IBM_QUANTUM_INSTANCE"]

service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=api_key,
    instance=instance
)

backend = service.least_busy(
    operational=True,
    simulator=False,
    min_num_qubits=2
)

print("Using:", backend.name)