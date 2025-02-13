# Blog Wag - Projeto Django

Este repositório contém um projeto Django para um blog com funcionalidades de autenticação, postagens e comentários.

## 📌 **Pré-requisitos**
Antes de rodar o projeto, certifique-se de ter instalado em seu sistema:
- Python 3.10+
- Git
- Virtualenv
- Banco de Dados SQLite (já incluído no Django por padrão)

## 🚀 **Passo a passo para rodar o projeto**


### **2️⃣ Criar e ativar o ambiente virtual** (recomendado)
```bash
python -m venv venv  # Criar o ambiente virtual
```
Ativar:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Instalar as dependências**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar o banco de dados**
Criar as migrações do banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Criar um superusuário (admin)**
```bash
python manage.py createsuperuser
```
Digite um nome de usuário, e-mail e senha quando solicitado.

### **6️⃣ Rodar o servidor local**
```bash
python manage.py runserver
```
Acesse o projeto no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### **7️⃣ Acessar o painel de administração**
Se desejar acessar a administração do Django, vá para:
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
E faça login com o superusuário criado.

## 📂 **Estrutura do projeto**
```
NOME_REPOSITORIO/
│-- blogWag/
│   ├── telaInicial/          # Aplicação principal
│   ├── static/               # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/            # Templates HTML
│   ├── db.sqlite3            # Banco de dados SQLite
│   ├── manage.py             # Arquivo principal do Django
│   ├── requirements.txt      # Dependências do projeto
│   ├── README.md             # Documentação do projeto
```

## 🛠 **Principais Funcionalidades**
✅ Cadastro e login de usuários
✅ Publicação de postagens com imagem
✅ Comentários nas postagens
✅ Sistema de autenticação
✅ Painel administrativo para gerenciamento

## 📜 **Licença**
Este projeto é de uso pessoal, para a matéria Web BackEnd (ifmt) Professor Alberto Sales. Caso queira utilizá-lo ou modificá-lo, sinta-se à vontade!

---
Desenvolvido por **Wagner Ferreira** 🚀

