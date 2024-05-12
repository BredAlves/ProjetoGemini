# Projeto Gemini
O projeto em questão foi desenvolvido para o desafio proposto durante a Imersão IA da Alura e Google.


## Proposta
O projeto foi desenvolvido em Python, com a integração da GenAI. A proposta é utilizar a IA, para fazer levantamento de informações de uma forma mais eficaz que um questionário simples. E instruir o usuário ao final.

## Recomendações
Caso não tenha o pacote da GenAI, é necessário antes de executar o código fazer a instalação do mesmo.
```
pip install -q -U google-generativeai
```


como foi desenvolvido no Vscode, a APIKEY foi remvoida do codigo ao upa-lo para o repositório. gere a sua no

- [AI Studio](https://aistudio.google.com/)

```
GOOGLE_API_KEY="SUA_KEY_AQUI"
genai.configure(api_key=GOOGLE_API_KEY)
```
E a insira no local sinalizado nesse trecho do código.

## Observações
algumas instruções foram passadas para a IA dentro do contexto para tentar minimizar algumas interações incompativeis e minimizar algumas alucinações que surgiram nos primeiros testes.


- Versão 1 - 11/05
