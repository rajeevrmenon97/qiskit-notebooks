import argparse
from qiskit_ibm_runtime import QiskitRuntimeService

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help=f"API Token for Qiskit", required=True)
    args = parser.parse_args()

    QiskitRuntimeService.save_account(channel="ibm_quantum", token=args.token, overwrite=True)