# Automatic Email Organizer

An automation system built with **Python, JavaScript, and n8n** that classifies emails based on their subject line and message content.

The project demonstrates **workflow automation, JSON processing, rule-based classification, and integration between Python and n8n**, without relying on external APIs or paid services.

---

## Problem it solves

A crowded inbox makes it hard to quickly tell which messages matter. This project automates part of that process by analyzing each message and classifying it into one of the following categories:

- Finance
- Support
- Sales
- Other

Classification is performed using predefined keywords.

---

## How it works

```text
Manual Trigger
      │
      ▼
Simulated Emails
      │
      ▼
Email Classification
      │
      ▼
Final Result
```

### Workflow steps

1. **Manual Trigger** — starts the workflow directly from the n8n interface.
2. **Simulated Emails** — generates sample messages so the classifier can be tested without a real Gmail account.
3. **Email Classification** — analyzes the subject line and message body, searching for keywords that match the configured categories.
4. **Final Result** — returns the classified emails in a simple, readable format.

---

## Project architecture

The project includes two implementations of the same business logic.

### Python

The file `python/classifier.py` works as a standalone email classifier. It:

1. Receives JSON input through `STDIN`.
2. Reads the email subject and body.
3. Applies the classification rules.
4. Returns the result as JSON through `STDOUT`.

### n8n

The file `workflows/email-organizer.json` contains the exported n8n workflow. The classification logic is implemented in JavaScript inside n8n `Code` nodes, so the entire workflow runs directly within n8n.

### Conceptual workflow

```text
Email
  ↓
Data Extraction
  ↓
Subject and Body Analysis
  ↓
Keyword Matching
  ↓
Classification
  ↓
Result
```

---

## Technologies used

| Technology | Purpose |
|---|---|
| Python | Standalone email classifier |
| JavaScript | Classification logic executed within n8n |
| n8n | Workflow orchestration |
| JSON | Input and output data format |
| Git | Version control |
| GitHub | Project hosting and documentation |

---

## Project structure

```text
n8n-email-organizer/
│
├── python/
│   └── classifier.py            # Standalone Python classifier
│
├── workflows/
│   └── email-organizer.json     # Exported n8n workflow
│
├── examples/
│   ├── input_financeiro.json
│   ├── input_outros.json
│   ├── input_suporte.json
│   └── input_vendas.json
│
├── deploy.py                    # Optional: creates the workflow on an n8n instance via the n8n API
├── workflow.json                # n8n workflow export
├── requirements.txt             # Dependencies used by deploy.py
├── .gitignore
└── README.md
```

---

## Classification categories

| Category | Example keywords |
|---|---|
| **Finance** | boleto, invoice, payment, pix, nfe, debit, due date |
| **Support** | error, bug, failure, ticket, issue, not working |
| **Sales** | promotion, discount, offer, buy now, free, plan |
| **Other** | No matching keywords |

The original Portuguese keywords are kept in the classification rules to support emails written in Portuguese.

---

## Running the Python classifier

### Prerequisites

Python 3.8 or higher. The classifier itself uses only Python's standard library; the dependencies in `requirements.txt` are used by `deploy.py`.

### Windows PowerShell

```powershell
'{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

### Linux / macOS

```bash
echo '{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

### Testing with the sample files

```powershell
Get-Content examples/input_financeiro.json | python python/classifier.py
Get-Content examples/input_suporte.json     | python python/classifier.py
Get-Content examples/input_vendas.json       | python python/classifier.py
Get-Content examples/input_outros.json        | python python/classifier.py
```

---

## Importing the workflow into n8n

1. Open your **n8n** instance.
2. Go to the **Workflows** section.
3. Select **Import from File**.
4. Choose `workflows/email-organizer.json`.
5. Open the imported workflow and click **Execute Workflow**.
6. The simulated emails will be processed and classified automatically.

Alternatively, `deploy.py` can create the workflow on an n8n instance through the n8n API. It reads the `N8N_URL` and `N8N_API_KEY` environment variables (for example, from a `.env` file).

---

## Example

### Input

```json
{
  "subject": "Fatura vencida - R$ 350,00",
  "body": "Seu boleto está com vencimento urgente. Pague para evitar juros."
}
```

### Output

```json
{
  "categoria": "Financeiro"
}
```

The JSON field names and category values are kept in Portuguese to match the original classifier implementation.

---

## Technical decisions

The classification system was initially developed using a **keyword-based approach**. This approach was chosen because it provides:

- Fast execution.
- Offline functionality.
- No external API costs.
- Easy maintenance.
- Simple integration of new categories.
- Clear and understandable classification logic.

The architecture also makes it possible to replace the keyword-based system with an AI model or another classification mechanism in the future.

---

## Concepts applied

- Workflow automation
- Python programming
- JavaScript
- JSON processing
- STDIN and STDOUT
- Conditional statements
- Rule-based classification
- Integration between different technologies
- Project organization
- Git / GitHub / n8n

---

## Roadmap

- [x] Develop a keyword-based classifier.
- [x] Implement the classifier in Python.
- [x] Create an n8n workflow.
- [x] Implement the classification logic in JavaScript.
- [x] Create JSON files for testing.
- [x] Export the workflow to GitHub.
- [ ] Connect the workflow to Gmail.
- [ ] Automatically create Gmail labels.
- [ ] Organize emails into specific categories.
- [ ] Add classification history.
- [ ] Build an email classification dashboard.
- [ ] Implement automated tests.
- [ ] Dockerize the project.
- [ ] Integrate AI-powered email classification.

---

## Security

Files containing sensitive information, credentials, or environment variables should never be committed to the repository (for example, `.env` and `.env.*`). These files should be excluded using `.gitignore`.

---

## Author

**Emanuel Vitor Fernandes Nascimento**

Back-End Developer | Automation

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) · [GitHub](https://github.com/evfernandes-dev)

---

## About the project

This project was built as part of my hands-on learning in **Back-End Development and Workflow Automation**.

By combining Python, JavaScript, and n8n, I built a practical email classification system focused on simplicity, maintainability, and future scalability, strengthening my understanding of **business logic, data processing, workflow orchestration, and integration between different technologies**.
