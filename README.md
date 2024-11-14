# Reconhecedor de Voz com Flask

Este projeto implementa uma aplicação web utilizando Flask, que permite ao usuário interagir com o reconhecimento de voz e conversão de texto em fala. O sistema é capaz de capturar áudio do microfone, converter em texto e também transformar texto em áudio.

## Funcionalidades

- **Reconhecimento de fala**: Captura o áudio do microfone e converte para texto.
- **Conversão de texto para fala**: Converte o texto inserido pelo usuário em áudio e o reproduz.
- **Limpar campos**: Limpa a área de texto e o campo de entrada de texto.
  
## Estrutura do Projeto

```plaintext
voz_em_texto/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
└── app.py

## Requisitos

Certifique-se de ter os seguintes pacotes Python instalados:

- Flask
- SpeechRecognition
- pyttsx3

Para instalar as dependências, use o seguinte comando:

```bash
pip install Flask SpeechRecognition pyttsx3
```
