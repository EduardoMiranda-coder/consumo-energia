# PROJETO CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE


# ENTRADA 
aparelho = input("Digite o nome do aparelho:")
potencia = float(input("Digite a potência em watts(W)? "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
      
# PROCESSAMENTO 
# Cálculo do consumo mensal em kWh/mês.

consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo para extimativa de custo mensal do aparelho.
custo_estimado = consumo_mensal * 0.65

# SAÌDA 

print(f"O aparelho: {aparelho} tem um consumo mensal estimado de: {consumo_mensal:.2f}Kwh/mês")
print(f"O custo estimado será de R$: {custo_estimado:.2f}/mês")