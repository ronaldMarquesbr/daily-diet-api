
# Daily-diet

Este projeto refere-se a criação de uma API para controle de dieta alimentar. Com essa API, um cliente pode cadastrar, visualizar, editar e excluir as refeições que ele fez em um dia. Esse projeto faz parte de um módulo do curso de Backend com Python da [Rocketseat](https://www.rocketseat.com.br/).

## Tecnologias usadas

- **Linguagem:** Python
- **Framework:** Flask
- **Banco de dados:** MySQL
- **ORM:** SQLAlchemy
- **Testes:** Pytest e Postman
- **Utils**: Requests (requisições nos testes), Datetime e PyTZ(para lidar com datas e timezones)

## Referência da API

### Criar refeição

```
  POST /meal
```

Corpo da requisição
```json
{
    "name": "<string>",
    "description": "<string, optional>",
    "date": "<string: datetime in ISO 8601 format, optional>",
    "off_diet": "<bool>"
}
```

**Notas:**


- Campo `description`: é definido como uma string vazia "", caso não seja passado nenhum valor
- Campo `date`: é definido com o datetime atual, caso não seja passado



Respostas
| Código    |  Descrição                       |
| :-------- |:-------------------------------- |
| 200    | Refeição criada com sucesso |
| 400    | Dados enviados incorretamente ou formato de data inválido (especificado no retorno)|


### Obter refeição

```
  GET /meal/<id>   
```

| Parâmetro | Tipo     | Descrição                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Inteiro` | **Obrigatório**. ID da refeição a ser obtida|

Respostas
| Código    |  Descrição                       | Retorno
| :-------- |:-------------------------------- |:---------|
| 200    | Refeição encontrada com sucesso| Meal object
| 404    | Refeição não encontrada| {"message": "<string>"}

### Obter todas as refeições

```
  GET /meals
```

Respostas
| Código    |  Descrição                       | Retorno
| :-------- |:-------------------------------- |:---------|
| 200    | Todas as refeições são retornadas| `Meal` objects

### Atualizar refeição

```
  PATCH /meal/<id>   
```
As informações da refeição podem ser atualizadas isoladamente ou em conjunto.

| Parâmetro | Tipo     | Descrição                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Inteiro` | **Obrigatório**. ID da refeição a ser atualizada|

Corpo da requisição
```json
{
    "name": "<string>",
    "description": "<string>",
    "date": "<string: datetime in ISO 8601 format>",
    "off_diet": "<bool>"
}

```

Respostas
| Código    |  Descrição                       | Retorno
| :-------- |:-------------------------------- |:---------|
| 200    | Refeição atualizada com sucesso|{"id": int, "message": "<string>"}
| 400    | Dados inválidos/faltantes ou formato de data inválido | {"message": "<string>"}
| 404    | Refeição não encontrada| {"message": "<string>"}

### Remover refeição

```
  DELETE /meal/<id>   
```

| Parâmetro | Tipo     | Descrição                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `Inteiro` | **Obrigatório**. ID da refeição a ser removida|

Respostas
| Código    |  Descrição                       | Retorno
| :-------- |:-------------------------------- |:---------|
| 200    | Refeição deletada com sucesso|{"message": "<string>"}
| 404    | Refeição não encontrada| {"message": "<string>"}