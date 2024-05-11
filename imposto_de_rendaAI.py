

import google.generativeai as genai

# Substitua 'SUA_CHAVE_API' pela sua chave de API
GOOGLE_API_KEY="SUA_KEY_AQUI"
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações de geração e segurança (opcional)
generation_config = genai.GenerationConfig(temperature=0.7)
safety_settings ={
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
    }

# Inicializa o modelo Gemini
model = genai.GenerativeModel(
    model_name="models/gemini-pro", 
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Inicializar contexto e lista de documentos
contexto = []
documentos = []

# Pergunta inicial
pergunta = """Olá, vou te ajudar com a sua declaração do imposto de renda.\n

Qual foi a sua renda total em 2023? Inclua salários, pró-labore, aluguéis, pensões, etc."""
print(pergunta)

# Loop principal do questionário
chat = model.start_chat()
while True:
  resposta = input("Sua resposta: ")
  contexto.append(f"{pergunta} {resposta}")

  # Lógica para coletar documentos (simplificada)
  if "sim" in resposta.lower():
    documento = input("Por favor, informe o nome do documento que comprova essa informação: ")
    documentos.append(documento)

  # Gerar próxima pergunta com base no contexto
  prompt = f"""
  Você é um especialista ajudando um cliente a declarar o Imposto de Renda.
  Baseado nas informações já fornecidas, gere a próxima pergunta 
  pertinente para o questionário. 
  voce nao envia emails, suas interações sao apenas pelo prompt
  Contexto: {contexto}
  """
  response = chat.send_message(prompt)
  pergunta = response.text
  print(pergunta, "\n")

  # Condição de saída (simplificada)
  if "Obrigado pelas informações!" in pergunta:
    break

# Resumo final
print("\nObrigado pelas informações!")
print("Documentos necessários:", documentos)