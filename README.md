# projeto-api-atividade# Microsserviço de Atividades

Este microsserviço é responsável pela gestão de atividades vinculadas aos professores, fornecidos pela API de Professores.

## 🏗️ Arquitetura

- Estrutura baseada em MVC (Model-View-Controller);
- Banco de dados SQLite;
- API RESTful com Flask e Flask-RESTx;
- Documentação Swagger embutida.

## 🔗 Integração

- O campo `professor_id` vincula uma atividade a um professor cadastrado no microsserviço de Professores.

## 🚀 Como Executar (Docker)

1. Construa a imagem:

```bash
docker build -t atividade-service .