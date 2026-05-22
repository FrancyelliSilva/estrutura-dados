# Estrutura de Dados

Este repositório contém atividades realizadas na disciplina de Estruturas de Dados do curso de Bacharelado em Sistemas de Informação da Universidade Tecnológica Federal do Paraná (UTFPR).

## Sobre o projeto

O projeto apresenta uma implementação simples de filas em Python, com um exemplo de aplicação que simula o fluxo de pacientes em um atendimento médico/triagem.

## Conteúdo do repositório

- `aula-fila/fila.py`: classe `Fila` que implementa operações básicas de fila (entrar, chamar, size, isEmpty, proximo e verFila).
- `aula-fila/main.py`: script interativo que usa a fila para gerenciar pacientes em triagem e em filas de atendimento verde/vermelho.

## Como usar

1. Navegue até a pasta do projeto:
   ```bash
   cd aula-fila
   ```

2. Execute o script em Python:
   ```bash
   python main.py
   ```

3. Siga o menu para:
   - adicionar pacientes à fila de triagem
   - chamar pacientes para classificação
   - atender pacientes das filas verde e vermelha

## Descrição da lógica

- Cada paciente entra na fila de triagem.
- Ao realizar a triagem, o paciente é direcionado para a fila verde ou vermelha com base no comprimento do nome (exemplo de critério simplificado).
- O atendimento dá prioridade à fila vermelha.

## Observações

- Este é um exercício de aprendizagem de estruturas de dados e manipulação de filas em Python.
- A lógica de triagem é apenas ilustrativa e pode ser adaptada para critérios mais realistas.

## UTFPR

Atividades desenvolvidas como parte do curso de Bacharelado em Sistemas de Informação na UTFPR.