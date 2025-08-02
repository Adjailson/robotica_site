# Robótica Suassuna - Site Oficial

Este é o repositório do site oficial do **Clube de Robótica Suassuna**, desenvolvido com [Flask](https://flask.palletsprojects.com/) e [Jinja2](https://jinja.palletsprojects.com/) para divulgação de projetos, eventos e atividades realizadas na **ETE Ariano Vilar Suassuna**, localizada em **Garanhuns - PE**.

---

## 🌐 Acesse nosso Instagram
Siga o clube para acompanhar novidades e fotos dos projetos:  
👉 [@robotica_suassuna](https://www.instagram.com/robotica_suassuna/)

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório ou extraia o `.zip`**
2. Navegue até a pasta do projeto:
   ```bash
   cd robotica_suassuna
   ```
3. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute o servidor Flask:**
   ```bash
   python run.py ou flask run
   ```

6. Acesse no navegador:  
   👉 `http://localhost:5000`

---

## 📁 Estrutura de Pastas

```
robotica_suassuna/
├── routes.py
├── static/         # (CSS/JS/imagens)
└── templates/
   ├── base.html
   ├── index.html
   ├── sobre.html
   ├── galeria.html
   ├── espaco_maker.html
   ├── eventos.html
   └── contato.html

├── app.py
└── requirements.txt
```

---

## ✨ Funcionalidades

- Página inicial com imagem do Instagram
- Seção "Sobre o Clube"
- Galeria de fotos com link para o Instagram
- Espaço Maker e eventos
- Página de contato

---

## 📌 Licença

Este projeto é de uso educacional e sem fins lucrativos. Compartilhe e contribua com conhecimento!

---

Desenvolvido com 💻 por alunos e professores do **Clube de Robótica Suassuna** – Garanhuns, PE.
