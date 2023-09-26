class Cliente:
    def __init__(self, nome, email, plano):
        global lista_planos
        self.nome = nome
        self.email = email
        lista_planos = ["Basic", "Premium", "Deluxe"]
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido.")
    
    def mudar_plano(self, novo_plano):
        if novo_plano in lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido.")

    
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "Basic" and plano_filme == "Premium":
            print("Faça o upgrade para Premium ou Deluxe para assistir esse filme. ")
        elif self.plano == "Premium" and plano_filme == "Deluxe":
            print("Faça upgrade para o Deluxe para assistir esse filme.")
        else:
            print("Plano Inválido.")
        
            

        


cliente1 = Cliente("Maykon", "maykonoliveiradev@gmail.com", "Premium")
print(cliente1.plano)
cliente1.ver_filme("Suits", "Deluxe")
cliente1.mudar_plano("Basicc")
print(cliente1.plano)
cliente1.ver_filme("Suits", "Deluxe")



        