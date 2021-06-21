# Design Patterns Python I

👋 Olá, Seja Bem-vindo(a) ao 'Design Patterns Python I: Boas práticas de programação'.

# Projeto 'Design Patterns Python I: Boas práticas de programação' do curso:

## [Design Patterns Python I: Boas práticas de programação](https://cursos.alura.com.br/course/design-patterns-python)

### Aulas

<details>
    <summary>Muitos Descontos e o Chain of Responsibility</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Muitos Descontos e o Chain of Responsibility</li>
        <li>Quando usar o Chain of Responsibility?</li>
        <li>Utilidade da classe Calculador_de_descontos</li>
        <li>Strategy e Chain of Responsibility</li>
        <li>Desvantagens de Patterns</li>
        <li>Colocando em prática</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Códigos parecidos e o Template Method</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Códigos parecidos e o Template Method</li>
        <li>Classes abstratas</li>
        <li>Quando usar o Template Method?</li>
        <li>O princípio de Hollywood</li>
        <li>Colocando em prática</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Comportamentos compostos por outros comportamentos e o Decorator</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Comportamentos compostos por outros comportamentos e o Decorator</li>
        <li>Quando usar o Decorator?</li>
        <li>Decorator ou Chain of Responsibility</li>
        <li>Decorator do Python</li>
        <li>Colocando em prática</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Estados que variam e o State</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Estados que variam e o State</li>
        <li>Refletindo sobre o código</li>
        <li>Quando usar o State?</li>
        <li>Colocando em prática</li>
        <li>Desconto Extra aplicado uma única vez</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Criação de Objetos e Builder</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Criação de Objetos e Builder</li>
        <li>Python e construtor</li>
        <li>Builder vs Recursos de linguagem</li>
        <li>Quando usar o Builder?</li>
        <li>Colocando em prática</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Executando diferentes ações e o Observer</summary>
    <ul>
        <li>Vídeo 1</li>
        <li>Executando diferentes ações e o Observer</li>
        <li>Quando usar o Observer?</li>
        <li>Colocando em prática</li>
        <li>Arquivos do projeto atual</li>
    </ul>
</details>

<details>
    <summary>Além dos padrões de projeto</summary>
    <ul>
        <li>Além dos padrões de projeto</li>
        <li>Qual é o padrão para o problema dos Vários Filtros?</li>
        <li>Qual é o padrão para o problema da Notificação de Sistemas Externos?</li>
        <li>Qual é o padrão para o problema dos Algoritmos Similares?</li>
        <li>Qual é o padrão para o problema do Contrato?</li>
        <li>O que voce pensa sobre Padrões de Projeto?</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python impostos_strategy/calculador_de_impostos.py
```

## Listar pacotes:
```sh
docker-compose run --rm app pipdeptree
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Chain of Responsibility](https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility)

[3° Template Method](https://refactoring.guru/pt-br/design-patterns/template-method)

[4° Decorator](https://refactoring.guru/pt-br/design-patterns/decorator)

[5° State](https://refactoring.guru/pt-br/design-patterns/state)

[6° Builder](https://refactoring.guru/pt-br/design-patterns/builder)

[7° Observer](https://refactoring.guru/pt-br/design-patterns/observer)