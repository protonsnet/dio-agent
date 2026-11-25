# 🤖 DIO Agent — Especialização em Cibersegurança

> Seu mentor de Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me), agora especializado em **análise defensiva de vulnerabilidades**.

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos e prática técnica. Além de apoiar com planos de estudo, desafios e conceitos, este fork evolui o agente para atuar como um **mentor de cibersegurança**, conduzindo análises de vulnerabilidades de forma estruturada—sem treinar modelo algum, apenas por meio de arquivos Markdown que orientam comportamento, conhecimento e fluxo de decisão.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um chatbot comum responde perguntas, como um buscador mais esperto. Um *agente* de IA vai além: ele lê, planeja e executa passos para te ajudar a alcançar um objetivo. É a diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é um agente desse tipo: um tutor particular que acompanha a sua evolução.

- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos no seu ritmo |
| Destravar um desafio | Te guia até a solução, sem entregar a resposta pronta |
| Entender um conceito | Explica de forma simples, com analogias e exemplos |
| Analisar vulnerabilidades | Coleta contexto, avalia impacto, probabilidade e severidade e orienta correção defensiva |

Ele conhece os formatos da DIO: Bootcamps, Formações, Acelerações, Cursos, English4Tech, Desafios de Código, Desafios de Projeto, Desafios Criativos, Lives e Mentorias. Assim, as recomendações sempre apontam para algo que você já tem na plataforma.

---

## 🛡️ Especialização em Cibersegurança (Desafio DIO)

### Por que especializar o agente?

Em vez de responder diretamente com comandos prontos, payloads ou correções genéricas sem contexto, o agente foi especializado para agir como um profissional de segurança:

1. **Entende o cenário antes de agir:** pergunta sobre ambiente (laboratório ou produção), exposição à internet, dados envolvidos e privilégios antes de sugerir comandos ou mudanças.
2. **Avalia risco com critério:** relaciona a falha à tríade **CID** (Confidencialidade, Integridade e Disponibilidade) e classifica **impacto**, **probabilidade** e **severidade** com justificativa.
3. **Orienta correção na causa raiz e validação:** guia a remediação segura (como consultas parametrizadas) e explica como confirmar que a falha foi mitigada.

### Arquivos criados e alterados

| Arquivo | Ação | Papel na especialização |
|---------|------|-------------------------|
| `skills/vulnerability-analysis/SKILL.md` | **Criado** | Roteiro operacional em 4 etapas (coleta de contexto, identificação da falha/mecanismo, avaliação de risco e orientação de correção/validação). |
| `skills/vulnerability-analysis/README.md` | **Criado** | Documentação humana explicando o objetivo, o funcionamento e os exemplos de uso da nova skill. |
| `agent/knowledge/security-basics.md` | **Criado** | Base conceitual sobre vulnerabilidade, ameaça, risco, tríade CID e boas práticas defensivas. |
| `agent/persona.md` | **Alterado** | Reforço da postura consultiva e cautelosa: perguntar contexto antes de agir, manter foco defensivo e diferenciar laboratório de produção. |
| `AGENTS.md` | **Alterado** | Inclusão da skill `vulnerability-analysis` na tabela principal de roteamento do agente. |
| `README.md` | **Alterado** | Documentação da especialização, estrutura atualizada, guia de execução no Hermes, melhoria escolhida e evidências. |

### Melhoria escolhida: Padronização de Relatório (Etapas 3 e 4)

Como evolução além do fluxo básico, foi adicionado um **formato padrão de resposta** nas Etapas 3 e 4 do `skills/vulnerability-analysis/SKILL.md`. Sempre que há contexto suficiente para avaliar um caso, o agente estrutura o parecer nos mesmos campos (`Alvo e cenário`, `Causa raiz e mecanismo`, `Referências`, `Impacto (CID)`, `Probabilidade`, `Severidade`, `Correção recomendada` e `Validação da mitigação`), tornando diferentes análises de código e infraestrutura diretamente comparáveis.

---

## 🚀 Como rodar no Hermes

1. **Clone este repositório e acesse a pasta raiz** (sempre execute o harness a partir da raiz de `dio-agent`):

```bash
git clone https://github.com/protonsnet/dio-agent.git
cd dio-agent
```

2. **Instale e configure o Hermes** conforme a documentação oficial (`https://hermes-agent.nousresearch.com/docs`):

```bash
hermes model
```

3. **Inicie o agente a partir da raiz do projeto:**

```bash
hermes
```

### Exemplos de prompts para testar

**🔍 Análise de código (AppSec)**
```
Como um especialista em segurança, analise o app.py e avalie se há vulnerabilidades.
```

**🖥️ Cenário de infraestrutura (coleta de contexto antes de agir)**
```
Tenho um servidor Ubuntu de laboratório exposto na internet. O que devo revisar primeiro?
```

**✅ Validação após correção**
```
Substituí a concatenação SQL por consulta parametrizada. Pode revisar novamente para confirmar se o risco foi mitigado?
```

---

## 📸 Evidências e Testes Realizados

> Antes de publicar no GitHub, garanta que a pasta `docs/images/` (ou o caminho escolhido) exista no repositório com os prints reais correspondentes.

1. **Análise inicial do `app.py` vulnerável (SQL Injection + MITRE ATT&CK):**
   - *Descrição:* Identificação da concatenação direta na consulta SQL, explicação conceitual da falha, referência técnica e sugestão de correção.
   - `![Análise do app.py vulnerável](docs/images/01-analise-app-vulneravel.png)`

2. **Reavaliação do `app.py` após consulta parametrizada:**
   - *Descrição:* Nova varredura confirmando a mitigação da falha de injeção SQL.
   - `![Validação do app.py corrigido](docs/images/02-validacao-app-corrigido.png)`

3. **Perguntas de contexto em cenário de infraestrutura (servidor Ubuntu exposto):**
   - *Descrição:* Demonstração do agente aplicando a Etapa 1 da skill `vulnerability-analysis` e solicitando detalhes de exposição, serviços e ambiente antes de sugerir comandos.
   - `![Coleta de contexto no cenário Ubuntu](docs/images/03-contexto-servidor-ubuntu.png)`

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. Além das skills originais do DIO Agent, este repositório conta com a skill de cibersegurança:

| Skill | Para que serve |
|-------|----------------|
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Conduz análise defensiva de falhas em código e infraestrutura com coleta de contexto e avaliação de risco |
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma didática, com analogias e exemplos |
| [Pesquisa na web](skills/web-search/SKILL.md) | Fundamenta respostas com busca atual e fontes citadas |

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                        Este guia
├── AGENTS.md                        Definição e roteamento do agente (lida por qualquer harness)
├── CLAUDE.md                        Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                   Personalidade, tom e conduta defensiva do agente
│   └── knowledge/
│       ├── dio-platform.md          O que é a DIO
│       ├── learning-experiences.md  Os formatos de aprendizado da DIO
│       └── security-basics.md       Conceitos de vulnerabilidade, ameaça, risco, tríade CID e boas práticas
│
├── skills/
│   ├── README.md                    O que são skills e como criar novas
│   ├── vulnerability-analysis/      Skill: análise de vulnerabilidades (SKILL.md + README.md)
│   ├── study-plan/                  Skill: plano de estudos
│   ├── unblock-challenge/           Skill: destravar desafio
│   ├── explain-concept/             Skill: explicar conceito
│   └── web-search/                  Skill: pesquisa na web
│
└── docs/
    └── glossary.md                  Glossário de termos
```

---

## 📖 Glossário e Referências

- **[Glossário completo](docs/glossary.md):** explicação de termos como *agente*, *harness*, *skill* e *prompt*.
- **Repositório base:** [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent)

---

## 💬 Sobre este projeto

Projeto desenvolvido como prática de especialização de agentes de IA para cibersegurança na [DIO](https://dio.me), demonstrando como estruturar comportamento profissional e defensivo apenas com arquivos versionados no repositório.