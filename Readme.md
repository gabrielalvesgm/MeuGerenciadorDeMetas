Documentação da aplicação
Oque é? a aplicação se trata de um gerenciador de metas, nele irei utilizar python como linguagem principal e postgreSQL como banco de dados, na aplicação o usuário poderá criar uma conta com username, senha e email, poderá criar metas com prazo e descrições, também poderá customizarlas como bem entender.

Estrutura da aplicação:

MeuGerenciadorDeMetas/
├── aplicativo/
│   ├── __init__.py         # Torna a pasta um módulo Python
│   ├── config/
│   │   └── database.py     # Configuração e conexão com o PostgreSQL
│   ├── models/
│   │   ├── __init__.py     # Torna a pasta um módulo Python
│   │   ├── usuario.py      # CRUD para a tabela Usuario
│   │   └── meta.py         # CRUD para a tabela Metas
│   ├── utils/
│   │   └── helpers.py      # Funções auxiliares
│   └── main.py             # Ponto de entrada da aplicação
├── requirements.txt        # Lista de dependências do projeto
├── README.md               # Documentação inicial

Em aplicativo>config>database.py criamos os seguintes métodos CRUD:
create_user, read_user, delete_user, create_meta, update_meta_status