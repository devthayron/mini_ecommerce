# E-commerce Django

## Descrição

Projeto de e-commerce simples desenvolvido com Django, onde os usuários podem visualizar, adicionar e editar produtos, além de realizar login e gerenciar suas informações. O sistema foi construído para ser escalável e fácil de adaptar a um e-commerce real.

## Tecnologias Utilizadas

### Frontend
- **Bootstrap 5**: Framework CSS utilizado para o design responsivo.
- **Crispy Forms**: Utilizado para melhorar a apresentação dos formulários, aplicando o estilo do Bootstrap automaticamente.

### Backend
- **Django**: Framework utilizado para desenvolvimento do backend, incluindo autenticação, CRUD de produtos e categorias, e rotas de login e logout.
- **SQLite**: Banco de dados utilizado para armazenamento de dados no desenvolvimento local.

## Funcionalidades Implementadas

### Produtos
- **Cadastro e Edição de Produtos**: Usuários administradores podem adicionar e editar produtos, incluindo nome, preço, imagem e quantidade.
- **Exibição de Produtos**: Produtos são exibidos em uma lista com imagem, nome, preço e quantidade. A descrição do produto foi temporariamente removida da visualização.
- **Categorias**: Produtos podem ser categorizados, com a possibilidade de escolher uma categoria ao adicionar ou editar um produto.

### Autenticação
- **Login e Logout**: Implementação de login e logout de usuários usando o sistema de autenticação do Django.
- **Proteção de Views**: As views, como a edição e a deleção de produtos, estão protegidas para que apenas usuários autenticados possam acessá-las.

### Admin
- **Admin do Django**: Interface administrativa do Django utilizada para gerenciar categorias e produtos. O admin também permite a atribuição de categorias aos produtos.

### Funcionalidades Futuras
- **Carrinho de Compras**: Adicionar funcionalidade de carrinho de compras onde os usuários podem adicionar produtos e revisar o carrinho.
- **Finalização de Pedido**: Implementação de checkout e pagamento.
- **Histórico de Pedidos**: Visualização do histórico de pedidos para o usuário.

## Instruções de Instalação

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```

2. **Instalar dependências**:
   - Se você ainda não tem o `pip` e o `virtualenv`, instale-os primeiro.
   - Crie e ative o ambiente virtual:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Para Linux/Mac
     venv\Scripts\activate  # Para Windows
     ```
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configurar o banco de dados**:
   - Aplique as migrações do banco de dados:
     ```bash
     python manage.py migrate
     ```

4. **Criar superusuário**:
   - Crie um superusuário para acessar o admin:
     ```bash
     python manage.py createsuperuser
     ```

5. **Iniciar o servidor**:
   - Execute o servidor local:
     ```bash
     python manage.py runserver
     ```

6. **Acessar a aplicação**:
   - Acesse o sistema no navegador em: `http://127.0.0.1:8000/`