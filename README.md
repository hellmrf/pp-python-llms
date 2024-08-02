# Utilizando Modelos de Linguagem de Grande Escala (LLM) em Python

✏️ Por [Heliton Martins](https://hellmrf.dev.br) | 01 de agosto de 2024 | [🌱 Programação Popular](https://youtube.com/@programacaopopular).

Usaremos neste tutorial os seguintes modelos (LLMs):
- **OpenAI GPT 4o** (pago)
    - 🗝️ [Chaves de API](https://platform.openai.com/api-keys) (pegue sua chave aqui)
    - 📄 [Documentação](https://platform.openai.com/docs/overview)
    - 💰 Necessário recarregar a conta em no mínimo US$ 5,00 (R$ 28,76 na data da escrita deste documento);
- **Google Gemini 1.5** (gratuito para testes)
    - 🗝️ [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat) (pegue sua chave aqui)
    - 📄 [Documentação](https://ai.google.dev/gemini-api/docs)
    - 💰 Gratuito, mas com limites no número de **R**equisições **P**or **M**inuto (2 RPM para o Gemini 1.5 Pro, 15 RPM para o Gemini 1.5 Flash)

## Configurando o ambiente

Após clonar o repositório, é fortemente recomendado configurar um novo ambiente do Python (usando, por exemplo, [venv](https://cloud.google.com/python/docs/setup?hl=pt-br#installing_and_using_virtualenv) ou [conda](https://docs.anaconda.com/miniconda/)) para isolar suas dependências.

Instale as dependências com o pip:
```shell
python3 -m pip install -r requirements.txt
```

Feito isso, copie o arquivo `.env.sample` para `.env` e insira suas chaves de API. Por exemplo:

```shell
cp .env.sample .env # copia o arquivo

code .env # abre para edição com vscode
nano .env # abre para edição com nano
vim .env # abre para edição com vim
```

O conteúdo do arquivo será algo assim (substitua `YOUR-API-KEY` pelas chaves verdadeiras):

```ini
OPENAI_API_KEY="YOUR-API-KEY"
GOOGLE_API_KEY="YOUR-API-KEY"
```