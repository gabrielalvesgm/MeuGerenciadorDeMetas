Documentação da aplicação

Oque é o MyWay?
O MyWay é um gerenciador de metas pessoais desenvolvido como uma API RESTful, permitindo que os usuários acompanhem seus objetivos de forma organizada e eficiente. A API foi construída utilizando Python com o microframework Flask, integrando PostgreSQL como banco de dados, utilizando psycopg2 para a comunicação entre o back-end e o banco de dados. Para segurança e autenticação, a API implementa um sistema baseado em JWT (JSON Web Tokens), utilizando a biblioteca Flask-JWT-Extended para gerenciamento de tokens.

Para que serve o MyWay?
O MyWay serve para ajudar os usuários a gerenciarem suas metas de forma personalizada. Cada usuário pode se registrar e fazer login, tendo acesso ao seu próprio perfil, onde pode criar, editar e excluir metas. Cada meta contém as seguintes informações:
Título: Nome da meta.
Descrição: Explicação detalhada do objetivo.
Prazo: Data limite para conclusão.
Prioridade: Nível de importância da meta.
Além disso, o sistema utiliza tokens JWT para garantir segurança nas requisições e controle de sessão dos usuários, garantindo que apenas usuários autenticados possam acessar e modificar seus dados.




Estrutura da aplicação:

MeuGerenciadorDeMetas/
├── aplicativo/
│   ├── __init__.py         # Torna a pasta um módulo Python
│   ├── main.py             # Arquivo main
│   ├── routes.py           # Arquivo contendo rotas
│   ├── config/
│   │   ├── database.py     # Configuração e conexão com o PostgreSQL
│   │   └── config.py       # Configurações gerais, incluindo JWT
│   ├── models/
│   │   ├──__psyache__
│   │   ├── __init__.py     # Torna a pasta um módulo Python
│   │   ├── usuario.py      # CRUD para a tabela Usuario
│   │   ├── metas.py        # CRUD para a tabela Metas
│   │   └── auth.py         # Novo arquivo para autenticação
│   ├── tests               # Página com todos os testes unitários
│   ├── main.py             # Ponto de entrada principal do app
│   └── routes.py           # Define as rotas da aplicação
├── requirements.txt        # Lista de dependências do projeto
├── README.md               # Documentação inicial

1. Pasta `aplicativo
   Contém todo o código da aplicação. Essa pasta é o núcleo do projeto.

   __init__.py
     Marca a pasta como um módulo Python, permitindo importar e organizar pacotes.

   Subpasta `config/`
    `database.py` 
       Configura e estabelece a conexão com o banco de dados PostgreSQL.  
       Exemplo: funções para conectar ao banco e retornar um objeto de conexão para uso em outros módulos.

   Subpasta `models/
     Organiza as operações relacionadas ao banco de dados.
    `usuario.py`
       Implementa os CRUDs para manipular os dados na tabela `usuario`.
    `meta.py`
       Implementa os CRUDs para manipular os dados na tabela `metas`.

    Subpasta `utils/ 
    helpers.py
       Contém funções auxiliares que podem ser reutilizadas em diferentes partes do código, como validações ou formatação de dados.

    main.py 
     O ponto de entrada da aplicação. Ele será responsável por iniciar o servidor Flask, configurar rotas e importar os módulos necessários.

2.  requirements.txt  
   Lista de dependências do projeto para que outras pessoas ou ambientes possam instalar os pacotes necessários.  
   Exemplo: `flask`, `psycopg2-binary`, etc.

3. README.md
   Contém a documentação inicial do projeto, com explicação sobre o objetivo, como configurar e usar a aplicação.

Fluxo Geral da Aplicação

1. Configuração do Banco de Dados
 database.py estabelece a conexão com o PostgreSQL e disponibiliza essa conexão para os outros módulos.

Operações CRUD (Models)
   - Os arquivos `usuario.py` e `meta.py` implementam as funcionalidades principais (criação, leitura, atualização e exclusão de dados) para as tabelas `usuario` e `metas`.

Utilização das Funcionalidades no Flask 
   - O arquivo `main.py`:
     - Importa os métodos dos arquivos `usuario.py` e `meta.py`.
     - Configura as rotas HTTP (como `/criar_usuario`, `/listar_metas`, etc.).
     - Inicia o servidor Flask para receber requisições.

Execução da Aplicação  
   - Ao executar `main.py`, o servidor é iniciado, permitindo chamadas para as rotas configuradas, que interagem com os métodos nos arquivos de model.



**Inicio do desenvolvimento do app e testes.**
 Comecei estabelecendo a conexão com o PostgreSQL utilizando a lib psycopg2, foi criada a função create_conection.
Após estabelecida a função, no PostgreSQL, criei duas tabelas (usuario, meta) onde foi definido id, user_id, nome_meta, descricao_meta, prazo_meta, status_meta, e para usuario: id, username, email e password.
Após criado as tabelas no SQL, implementei CRUDS em models/usuario.py e meta.py, inicialmente criei as funções GET E POST para usuario e metas.
Então criei uma pasta para testes dos CRUDS. Meu primeiro teste será com o test.create.py que servirá para função POST.
**primeiro teste**: Testei o POST usuario e meta, o retorno foi um sucesso, o log me respondeu: ''Usuário criado com ID: 1, Meta criada com ID: 1"
    No postgreSQL, testei no query SELECT * FROM usuario; SELECT * FROM metas;
    o postgreSQL me respondeu com os dados do teste, portando foi um sucesso.
    fiz este teste continuamente, criando diversos arquivos para testes singulares em aplicativo/tests/ realizei diversos testes CRUD, como GET, POST, DELETE.
    Houveram alguns erros, porém, todos foram tratados e corrigidos facilmente.
    nos testes de delete.user/meta, falta uma refinação do código.
Próximo passo será criar um tipo de ''validação'' para manter a segurança dos usuários e suas metas, também criar um sistema de lógica para evitar redundâncias e limitar os usuários e suas metas.
**Fazendo sistema de autenticação e segurança p login com o flask-jwt-extended
criando e configurando o arquivo ''config.py'' que será o arquivo responsável pelas configurações do sistema.

**Criar uma página web utilizando HTML, CSS, JavaScript, implementar um sistema de registro e login com input para usuários utilizarem, sistema de visualização e manutenção de metas de cada usuário.

    