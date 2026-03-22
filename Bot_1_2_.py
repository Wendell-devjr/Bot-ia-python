print("Oi!, Eu sou a IA!")

#loop continuo de perguntas simples

while True:
    msg = input("Voce: ").lower()

    if "sair" in msg:
        print("IA: Até mais!")
        break

    elif "olá" in msg or "oi" in msg:
        print("IA: Oi, tudo bem?")

    elif "qual seu nome" in msg:
        print("IA: Ainda nao tenho nome! apenas IA")

    elif "tudo bem" in msg:
        print("IA: Sim! estou funcionando perfeitamente")

    elif "quem te criou" in msg:
        print("IA: Foi o Wendell!")
        
    elif "bom dia" in msg:
        print("IA: Bom dia!, como posso ajudar?")
    
    elif "boa tarde" in msg:
        print("IA: Boa Tarde!, como posso ajudar?")
    elif "boa noite" in msg:
        print("IA: Boa Noite!, como posso ajudar?")
        

#parte do sistema de matematica!
        
    elif "calculo" in msg or "calcular" in msg or "matematica" in msg:
            print("IA: voce quer ajuda com calculos ?, escolha qual opçao deseja")
            print("IA: 1 = Multiplicaçao!\nIA: 2 = Adiçao!\nIA: 3 = Subtraçao!\nIA: 4 = Divisao!")
            
            op = (input("IA: Escolha a opçao: "))
                          
            n1 = float(input("digite o primeiro numero: "))
            n2 = float(input("digite o segundo numero: "))
            
            if op == "1":
                print (f"IA: Resultado: {n1 * n2}")
            elif op == "2":
                    print(f"IA: Resultado: {n1 + n2}")
            elif op == "3":
                print(f"IA: Resultado: {n1 - n2}")
            elif op == "4":
                print(f"IA: Resultado: {n1 / n2}")
            else:
                print("IA: Opçao invalida!")

    else:
        print("IA: Não Entendi")