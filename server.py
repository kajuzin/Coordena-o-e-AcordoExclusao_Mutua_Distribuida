import Pyro4
import time

@Pyro4.expose
class Barbeiro:
    def __init__(self):
        self.available = True

    def cortarCabelo(self):
        print("Recebendo uma solicitação de corte de cabelo.")
        time.sleep(3)
        return "Cabelo cortado"

    def cortarBarba(self):
        print("Recebendo uma solicitação de corte de barba.")
        time.sleep(4)
        return "Barba cortada"

    def cortarBigode(self):
        print("Recebendo uma solicitação de corte de bigode.")
        time.sleep(5)
        return "Bigode cortado"

if __name__ == "__main__":
    barbeiro = Barbeiro()
    daemon = Pyro4.Daemon(host="192.168.31.100", port=10000)
    uri = daemon.register(barbeiro)

    print("Registrando o servidor no Name Server...")

    with Pyro4.locateNS() as ns:
        ns.register("barbeiro", uri)

    print("Servidor registrado com sucesso. URI:", uri)

    print("Servidor aguardando conexões...")

    daemon.requestLoop()
