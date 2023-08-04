import Pyro4

if __name__ == "__main__":
    # Solicita ao usuário um nome fictício para o cliente
    nome_cliente = ("Cliente 4")

    # Inicializa o Name Server
    ns = Pyro4.locateNS()

    # Localiza o servidor remoto usando o Name Server
    uri = ns.lookup("barbeiro")
    barbeiro = Pyro4.Proxy(uri)

    print("Conexão bem-sucedida!")

    for _ in range(20):
        print(f"{nome_cliente} solicitou um corte de cabelo.")
        resultado = barbeiro.cortarCabelo()
        print(resultado)
        print(f"{nome_cliente} terminou o serviço.")
        print(f"{nome_cliente} solicitou um corte de Barba.")
        resultado = barbeiro.cortarBarba()
        print(resultado)
        print(f"{nome_cliente} terminou o serviço.")
        print(f"{nome_cliente} solicitou um corte de Bigode.")
        resultado = barbeiro.cortarBigode()
        print(resultado)
        print(f"{nome_cliente} terminou o serviço.")
        

