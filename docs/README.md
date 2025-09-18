# 📘 Guia de Exercícios e Desafios — Volume 1

Este guia reúne todos os exercícios e desafios do Volume 1 do eBook *Python por Jogos*, organizados por capítulo e com sugestões de extensão. Ideal para quem quer praticar, revisar ou expandir seus conhecimentos em programação de jogos com Python.

## 📁 Estrutura Recomendada do Repositório

```
python-por-jogos/
├── src/                # Código-fonte dos capítulos
│   ├── cap1/
│   ├── cap2/
│   ├── ...
│   └── cap7
├── desafios/           # Desafios práticos por capítulo
│   ├── cap1/
│   |   ├── desafio1_nickname.py
│   |   └── ...
|   ├── cap2/
│   └── ...
├── docs/               # Documentação e guias
│   └── README.md       # Este arquivo
└── savegame.json       # Arquivo de salvamento (opcional)
```

## 🧠 Capítulos e Desafios

### 1. 👋 Introdução e Primeiros Programas
- `desafio1_gerador_nickname.py`: Crie um nickname épico com cidade + animal.
- `desafio2_calculadora_pocoes.py`: Some poções atuais e compradas.
- `desafio3_status_personagem.py`: Exiba uma ficha de personagem formatada.

### 2. 🔢 Tipos de Dados e Variáveis
- `desafio1_conversor_moedas.py`: Converta dólares em ouro.
- `desafio2_nome_guilda.py`: Gere nome de guilda em MAIÚSCULAS.
- `desafio3_dano_critico.py`: Calcule dano crítico com multiplicador.

### 3. 🔁 Controle de Fluxo
- `desafio1_simulador_batalha.py`: Reduza HP do inimigo até derrotá-lo.
- `desafio2_contador_moedas.py`: Some moedas de 5 fases e desbloqueie baú.
- `desafio3_validador_senha.py`: Valide senha com while e dicas.

### 4. 🧩 Funções e Modularização
- `desafio1_misturar_pocoes.py`: Combine tipos de poções e retorne resultado.
- `desafio2_sistema_niveis.py`: Calcule XP e suba de nível.
- `desafio3_modulo_combate.py`: Crie funções de combate e teste em `main.py`.

### 5. 📦 Estruturas de Dados
- `desafio1_inimigos.py`: Gerencie inimigos com lista de dicionários.
- `desafio2_colecionaveis.py`: Use conjuntos para verificar coleção completa.
- `desafio3_inventario.py`: Inventário com quantidades e uso de itens.

### 6. 📚 Módulos e Pacotes
- `desafio1_inimigos_coletor.py`: Adicione inimigos ao jogo de moedas.
- `desafio2_niveis_coletor.py`: Aumente velocidade a cada 5 moedas.
- `desafio3_meus_utils/`: Crie pacote com funções e constantes reutilizáveis.

### 7. 🛡️ Tratamento de Erros
- `desafio1_sistema_comandos.py`: Aceite comandos e registre erros.
- `desafio2_validador_save.py`: Verifique chaves e corrija dados corrompidos.
- `desafio3_recuperacao_falhas.py`: Salve estado em caso de erro fatal.
- `desafio4_testes_salvamento.py`: Teste salvamento e carregamento com `pytest`.

### 8. 🧙‍♂️ Projeto Final — RPG em Terminal
- Sistema completo com:
  - Combate por turnos
  - Inventário e uso de itens
  - Pets e progressão
  - Eventos e narrativa
  - Salvamento e carregamento

## 🚀 Como Executar

```bash
# Executar um desafio específico
python desafios/cap1/desafio1_gerador_nickname.py

```

## 🛠️ Dicas para Contribuir

- 💡 Crie novos desafios com base nos capítulos.
- 🧪 Teste suas modificações com `print()` ou `assert`.
- 📋 Documente suas mudanças em um changelog.
- 🔄 Faça backup antes de grandes alterações.

## 📣 Créditos

Este repositório é baseado no eBook **Python por Jogos — Volume 1** de [MisterEu Code](https://github.com/MisterEu09).  
Para dúvidas, sugestões ou contribuições, abra uma issue ou envie um e-mail para mistereu09@gmail.com.

---