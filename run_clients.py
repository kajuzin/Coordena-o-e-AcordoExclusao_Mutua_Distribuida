import subprocess

if __name__ == "__main__":
    clients = ["client1.py", "client2.py", "client3.py", "client4.py", "client5.py"]

    # Executa cada cliente em um processo separado
    processes = []
    for client in clients:
        process = subprocess.Popen(["python", client], shell=True)
        processes.append(process)

    # Aguarda a finalização de todos os processos
    for process in processes:
        process.wait()

    print("Todos os clientes finalizaram.")
