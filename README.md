Opa, pessoal! DevWadson, aqui! E falando sobre este projeto.

# 🧭 Minecraft Coordinates

Um projeto simples e útil para jogadores de **Minecraft** que precisam acompanhar suas coordenadas no jogo sem depender apenas da tela de debug (`F3`).  
A ideia é facilitar a visualização e a visita de posições importantes, como casa, portais, biomas ou pontos de mineração...qualquer lugar que você
queira voltar ou ir e precisa de uma coordenada para isto.

---

🚀 Funcionalidades (por enquanto)

   - Salvar e nomear pontos de interesse (waypoints) no jogo.
   - Interface leve e minimalista usando CustomTkinter.
   - Armazenamento de coordenadas em banco de dados SQLite.
   - Manipulação de dados com DataFrames.
   - Suporte a múltiplos servidores e dimensões (IDs no banco de dados).

---

## 🛠️ Tecnologias usadas

- **Linguagem:** Python 3  
- **Bibliotecas:**  
  - `customtkinter` → interface gráfica moderna
  - `pyautogui` → captura de tela/inputs (se aplicável)
  - `pandas` → manipulação de dados em DataFrames
  - `sqlite3` → banco de dados leve integrado
- **Outras ferramentas:** Git, VS Code

---

## 🖥️ Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/minecraft-coordinates.git
   cd minecraft-coordinates

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate.ps1  # Windows Powershell
   .venv\Scripts\activate.bat  # Windows CMD

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Execute o projeto:
   se usa PPM (Python Package Manager)
   ```bash
   uv run python -m src.main

🤝 Contribuições

Contribuições são super bem-vindas!

Abra uma issue para sugestões ou relatos de bugs.

Crie um pull request se quiser adicionar funcionalidades ou melhorias.
