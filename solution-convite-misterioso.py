# Mensagem recebida
convite = """
##[convite001]##>>>👀Você foi escolhido para uma missão secreta!<<<##FIM##
"""

# Extrair a mensagem real (manual: contamos os índices a olho)
mensagem_limpa = convite[23:67]  # Começa após o 👀 e vai até antes das <<<

# Mostrar a mensagem ao usuário
print("📩 Mensagem secreta decodificada:")
print(mensagem_limpa)

# Entrada do usuário
resposta = input("\nDigite exatamente a mensagem secreta para confirmar seu acesso: ")

# Verificação
if resposta == mensagem_limpa:
    print("\n✅ Acesso concedido. Você está pronto para a missão!")
else:
    print("\n❌ Acesso negado. A mensagem está incorreta!")
