# Organizador Automático de E-mails

Classificador de e-mails por palavras-chave, com lógica implementada em Python e integrada ao n8n via workflow exportado.

---

## Problema que resolve

Caixas de entrada cheias tornam difícil identificar o que é urgente e o que pode aguardar. Este projeto automatiza a triagem de e-mails, classificando cada mensagem por categoria — sem depender de serviços externos ou APIs pagas.

---

## Como funciona o fluxo

```
Trigger Manual
     │
     ▼
Emails Simulados  ──►  Classificar Email  ──►  Resultado Final
(3 e-mails de teste)   (por palavras-chave)    (resumo formatado)
```

1. **Trigger manual** — inicia o workflow no n8n com um clique.
2. **Emails Simulados** — gera 3 e-mails de teste representando categorias diferentes (Financeiro, Suporte, Vendas).
3. **Classificar Email** — aplica regras de palavras-chave para determinar a categoria.
4. **Resultado Final** — formata a saída como um resumo legível por item.

A mesma lógica de classificação existe em dois formatos:
- `python/classifier.py` — script Python puro (sem dependências externas), que lê JSON pelo STDIN e retorna JSON pelo STDOUT.
- `workflows/email-organizer.json` — workflow n8n com a lógica reimplementada em JavaScript, pronto para importar e executar.

---

## Tecnologias utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.8+ | Classificador via linha de comando (stdlib apenas) |
| JavaScript | Lógica de classificação dentro dos nós Code do n8n |
| n8n | Orquestração do fluxo de automação |

---

## Estrutura do projeto

```
n8n-email-organizer/
├── python/
│   └── classifier.py          # Classificador via STDIN → STDOUT (Python puro)
├── workflows/
│   └── email-organizer.json   # Workflow n8n exportado, pronto para importar
├── examples/
│   ├── input_financeiro.json  # Exemplo de entrada: categoria Financeiro
│   ├── input_suporte.json     # Exemplo de entrada: categoria Suporte
│   ├── input_vendas.json      # Exemplo de entrada: categoria Vendas
│   └── input_outros.json      # Exemplo de entrada: categoria Outros
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Como executar localmente

**Pré-requisitos:** Python 3.8 ou superior. Nenhuma dependência externa — o classificador usa apenas a biblioteca padrão.

**Linux / macOS:**
```bash
echo '{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

**Windows (PowerShell):**
```powershell
'{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

**Usando os arquivos de exemplo:**
```bash
python python/classifier.py < examples/input_financeiro.json
python python/classifier.py < examples/input_suporte.json
python python/classifier.py < examples/input_vendas.json
```

---

## Como importar o workflow no n8n

1. Abra o n8n na sua instância local ou na nuvem.
2. Vá em **Workflows → Import from file**.
3. Selecione o arquivo `workflows/email-organizer.json`.
4. Clique em **Execute Workflow** para testar com os 3 e-mails simulados.

---

## Categorias de classificação

| Categoria  | Palavras-chave (exemplos)                                    |
|------------|--------------------------------------------------------------|
| Financeiro | boleto, fatura, pagamento, pix, nfe, débito, vencimento      |
| Suporte    | erro, bug, falha, ticket, problema, não funciona             |
| Vendas     | promoção, desconto, oferta, compre agora, grátis, plano      |
| Outros     | (nenhuma palavra-chave encontrada)                           |

---

## Exemplo de funcionamento

**Entrada:**
```json
{ "subject": "Fatura vencida - R$ 350,00", "body": "Seu boleto está com vencimento urgente. Pague para evitar juros." }
```

**Saída:**
```json
{ "categoria": "Financeiro" }
```

**Resumo gerado pelo n8n:**
```
#1 | Financeiro
#2 | Suporte
#3 | Vendas
```

---

## Melhorias futuras

- Conectar ao Gmail real via API para classificar e-mails da caixa de entrada ao vivo
- Aplicar labels automáticas no Gmail com base na categoria detectada
- Adicionar suporte a e-mails em inglês nas regras de palavras-chave
- Exportar relatório diário de e-mails classificados por categoria
- Substituir regras fixas por um modelo de linguagem para classificação mais precisa
