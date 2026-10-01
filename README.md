# 📧 Organizador Automático de E-mails

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![n8n](https://img.shields.io/badge/n8n-Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versionamento-F05032?style=for-the-badge&logo=git&logoColor=white)

Sistema de automação desenvolvido com **Python, JavaScript e n8n** para classificar e-mails automaticamente com base no assunto e no conteúdo da mensagem.

O projeto demonstra conceitos de **automação de workflows, manipulação de JSON, classificação baseada em regras e integração entre Python e n8n**, sem depender de APIs externas ou serviços pagos.

---

## 🎯 Problema que resolve

Caixas de entrada com muitos e-mails podem dificultar a identificação rápida de mensagens importantes.

Este projeto automatiza parte desse processo, analisando o conteúdo de cada mensagem e classificando o e-mail em uma das seguintes categorias:

- 💰 Financeiro
- 🛠️ Suporte
- 🛒 Vendas
- 📁 Outros

A classificação é realizada por meio de palavras-chave previamente definidas.

---

## ⚙️ Como funciona

```text
Trigger Manual
      │
      ▼
Emails Simulados
      │
      ▼
Classificar Email
      │
      ▼
Resultado Final
```

### Etapas do workflow

**1. Trigger Manual**

Inicia o workflow diretamente pelo painel do n8n.

**2. Emails Simulados**

Gera mensagens de exemplo para validar o comportamento do classificador sem depender de uma conta Gmail real.

**3. Classificar Email**

Analisa o assunto e o corpo da mensagem e procura palavras-chave correspondentes às categorias configuradas.

**4. Resultado Final**

Retorna os e-mails classificados em um formato simples e legível.

---

## 🧠 Arquitetura do projeto

O projeto possui duas implementações da mesma regra de negócio.

### Python

O arquivo:

```text
python/classifier.py
```

funciona como um classificador independente.

Ele:

1. recebe um JSON pelo `STDIN`;
2. lê o assunto e o corpo do e-mail;
3. aplica as regras de classificação;
4. retorna o resultado em JSON pelo `STDOUT`.

### n8n

O arquivo:

```text
workflows/email-organizer.json
```

contém o workflow exportado do n8n.

A lógica de classificação foi implementada em JavaScript dentro dos nós `Code`, permitindo que todo o fluxo seja executado diretamente no n8n.

### Fluxo conceitual

```text
E-mail
  ↓
Extração dos dados
  ↓
Análise do assunto e corpo
  ↓
Busca por palavras-chave
  ↓
Classificação
  ↓
Resultado
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python 3.8+ | Classificador independente |
| JavaScript | Lógica executada dentro do n8n |
| n8n | Orquestração do workflow |
| JSON | Entrada e saída dos dados |
| Git | Controle de versão |
| GitHub | Hospedagem e documentação do projeto |

---

## 📂 Estrutura do projeto

```text
n8n-email-organizer/
│
├── python/
│   └── classifier.py
│
├── workflows/
│   └── email-organizer.json
│
├── examples/
│   ├── input_financeiro.json
│   ├── input_suporte.json
│   ├── input_vendas.json
│   └── input_outros.json
│
├── screenshots/
│   └── workflow-n8n.png
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🏷️ Categorias de classificação

| Categoria | Exemplos de palavras-chave |
|---|---|
| **Financeiro** | boleto, fatura, pagamento, pix, nfe, débito, vencimento |
| **Suporte** | erro, bug, falha, ticket, problema, não funciona |
| **Vendas** | promoção, desconto, oferta, compre agora, grátis, plano |
| **Outros** | nenhuma palavra-chave correspondente |

---

## 💻 Como executar localmente

### Pré-requisitos

É necessário ter:

```text
Python 3.8 ou superior
```

O classificador utiliza apenas bibliotecas padrão do Python.

Não é necessário instalar dependências externas.

---

## 🐍 Executando o classificador Python

### Windows PowerShell

```powershell
'{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

### Linux / macOS

```bash
echo '{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

---

## 🧪 Testando com os exemplos

### Financeiro

```powershell
Get-Content examples/input_financeiro.json | python python/classifier.py
```

### Suporte

```powershell
Get-Content examples/input_suporte.json | python python/classifier.py
```

### Vendas

```powershell
Get-Content examples/input_vendas.json | python python/classifier.py
```

### Outros

```powershell
Get-Content examples/input_outros.json | python python/classifier.py
```

---

## 📥 Como importar o workflow no n8n

1. Abra sua instância do **n8n**.
2. Acesse a área de **Workflows**.
3. Escolha a opção **Import from File**.
4. Selecione:

```text
workflows/email-organizer.json
```

5. Abra o workflow.
6. Clique em **Execute Workflow**.
7. Os e-mails simulados serão processados automaticamente.

---

## 📊 Exemplo de funcionamento

### Entrada

```json
{
  "subject": "Fatura vencida - R$ 350,00",
  "body": "Seu boleto está com vencimento urgente. Pague para evitar juros."
}
```

### Saída

```json
{
  "categoria": "Financeiro"
}
```

---

## 📋 Exemplo de resultado no n8n

```text
#1 | Financeiro
#2 | Suporte
#3 | Vendas
#4 | Outros
```

---

## 🖼️ Workflow

Adicione uma captura do seu workflow dentro da pasta:

```text
screenshots/
```

Depois utilize:

```markdown
![Workflow n8n](screenshots/workflow-n8n.png)
```

O resultado aparecerá diretamente no README.

---

## 💡 Decisões técnicas

A classificação foi desenvolvida inicialmente utilizando **palavras-chave**.

Essa abordagem foi escolhida porque permite:

- execução rápida;
- funcionamento offline;
- ausência de custos com APIs;
- facilidade de manutenção;
- facilidade para adicionar novas categorias;
- entendimento simples da lógica utilizada.

A arquitetura também permite substituir futuramente o sistema baseado em palavras-chave por um modelo de inteligência artificial ou outro mecanismo de classificação.

---

## 📚 Conceitos aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos de:

- Automação de workflows
- Programação em Python
- JavaScript
- Manipulação de JSON
- STDIN e STDOUT
- Estruturas condicionais
- Classificação baseada em regras
- Integração entre tecnologias
- Organização de projetos
- Git
- GitHub
- n8n
- Versionamento de código

---

## 🚀 Roadmap

- [x] Criar classificador baseado em palavras-chave
- [x] Implementar classificador em Python
- [x] Criar workflow no n8n
- [x] Implementar lógica em JavaScript
- [x] Criar arquivos JSON para testes
- [x] Exportar workflow para o GitHub
- [ ] Conectar o workflow ao Gmail
- [ ] Criar labels automaticamente
- [ ] Mover e-mails para categorias específicas
- [ ] Adicionar histórico das classificações
- [ ] Criar dashboard de e-mails classificados
- [ ] Implementar testes automatizados
- [ ] Dockerizar o projeto
- [ ] Adicionar classificação utilizando IA

---

## 🔮 Próximas evoluções

Uma evolução natural do projeto será substituir os e-mails simulados por mensagens reais provenientes do Gmail.

O fluxo poderá seguir a arquitetura:

```text
Gmail Trigger
      ↓
Novo e-mail
      ↓
Extração do assunto e corpo
      ↓
Classificação
      ↓
Criação / aplicação de Label
      ↓
Organização automática da caixa de entrada
```

Também será possível integrar modelos de inteligência artificial para analisar o contexto completo das mensagens, tornando a classificação mais flexível do que uma abordagem baseada apenas em palavras-chave.

---

## 🔒 Segurança

Arquivos contendo informações sensíveis, credenciais ou variáveis de ambiente não devem ser enviados para o repositório.

Exemplo:

```text
.env
.env.*
```

Esses arquivos devem permanecer configurados no `.gitignore`.

---

## 👨‍💻 Autor

**Emanuel Vítor Fernandes Nascimento**

Desenvolvedor Back-End | Automação

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) • [GitHub](https://github.com/emanuelvitorfn7-gif)

---

## ⭐ Sobre o projeto

Este projeto foi desenvolvido como parte do meu aprendizado prático em **desenvolvimento Back-End e automação**, utilizando Python, JavaScript e n8n para construir uma solução simples, funcional e expansível.
