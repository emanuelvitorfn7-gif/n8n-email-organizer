# 📧 Automatic Email Organizer

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![n8n](https://img.shields.io/badge/n8n-Automation-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)

An automation system developed using **Python, JavaScript, and n8n** to automatically classify emails based on their subject lines and message content.

This project demonstrates concepts such as **workflow automation, JSON processing, rule-based classification, and integration between Python and n8n**, without relying on external APIs or paid services.

---

## 🎯 Problem It Solves

Managing an inbox with a large number of emails can make it difficult to quickly identify important messages.

This project automates part of that process by analyzing each message and classifying it into one of the following categories:

- 💰 Finance
- 🛠️ Support
- 🛒 Sales
- 📁 Other

Classification is performed using predefined keywords.

---

## ⚙️ How It Works

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

### Workflow Steps

**1. Manual Trigger**

Starts the workflow directly from the n8n interface.

**2. Simulated Emails**

Generates sample messages to validate the classifier without requiring a real Gmail account.

**3. Email Classification**

Analyzes the subject line and message body, searching for keywords that match the configured categories.

**4. Final Result**

Returns the classified emails in a simple, readable format.

---

## 🧠 Project Architecture

The project includes two implementations of the same business logic.

### Python

The file:

```text
python/classifier.py
```

works as a standalone email classifier.

It:

1. Receives JSON input through `STDIN`.
2. Reads the email subject and body.
3. Applies the classification rules.
4. Returns the result as JSON through `STDOUT`.

### n8n

The file:

```text
workflows/email-organizer.json
```

contains the exported n8n workflow.

The classification logic is implemented in JavaScript inside n8n `Code` nodes, allowing the entire workflow to run directly within n8n.

### Conceptual Workflow

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

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.8+ | Standalone email classifier |
| JavaScript | Classification logic executed within n8n |
| n8n | Workflow orchestration |
| JSON | Input and output data format |
| Git | Version control |
| GitHub | Project hosting and documentation |

---

## 📂 Project Structure

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

## 🏷️ Classification Categories

| Category | Example Keywords |
|---|---|
| **Finance** | boleto, invoice, payment, pix, nfe, debit, due date |
| **Support** | error, bug, failure, ticket, issue, not working |
| **Sales** | promotion, discount, offer, buy now, free, plan |
| **Other** | No matching keywords |

The original Portuguese keywords can be retained in the classification rules to support emails written in Portuguese.

---

## 💻 Running Locally

### Prerequisites

You need:

```text
Python 3.8 or higher
```

The classifier uses only Python's standard library.

No external dependencies are required.

---

## 🐍 Running the Python Classifier

### Windows PowerShell

```powershell
'{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

### Linux / macOS

```bash
echo '{"subject": "Boleto vencendo amanhã", "body": "Valor: R$ 350,00. Pagamento urgente."}' | python python/classifier.py
```

---

## 🧪 Testing with Sample Files

### Finance

```powershell
Get-Content examples/input_financeiro.json | python python/classifier.py
```

### Support

```powershell
Get-Content examples/input_suporte.json | python python/classifier.py
```

### Sales

```powershell
Get-Content examples/input_vendas.json | python python/classifier.py
```

### Other

```powershell
Get-Content examples/input_outros.json | python python/classifier.py
```

---

## 📥 Importing the Workflow into n8n

1. Open your **n8n** instance.
2. Navigate to the **Workflows** section.
3. Select **Import from File**.
4. Choose the following file:

```text
workflows/email-organizer.json
```

5. Open the imported workflow.
6. Click **Execute Workflow**.
7. The simulated emails will be processed and classified automatically.

---

## 📊 Example

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

## 📋 Example n8n Output

```text
#1 | Finance
#2 | Support
#3 | Sales
#4 | Other
```

---

## 🖼️ Workflow Screenshot

Add a screenshot of your workflow to the following directory:

```text
screenshots/
```

Then include this Markdown reference in your README:

```markdown
![n8n Workflow](screenshots/workflow-n8n.png)
```

The screenshot will be displayed directly in the GitHub README.

---

## 💡 Technical Decisions

The classification system was initially developed using a **keyword-based approach**.

This approach was chosen because it provides:

- Fast execution.
- Offline functionality.
- No external API costs.
- Easy maintenance.
- Simple integration of new categories.
- Clear and understandable classification logic.

The architecture also makes it possible to replace the keyword-based system with an artificial intelligence model or another classification mechanism in the future.

---

## 📚 Concepts Applied

The development of this project involved several programming and automation concepts:

- Workflow Automation
- Python Programming
- JavaScript
- JSON Processing
- STDIN and STDOUT
- Conditional Statements
- Rule-Based Classification
- Technology Integration
- Project Organization
- Git
- GitHub
- n8n
- Version Control

---

## 🚀 Roadmap

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

## 🔮 Future Improvements

A natural next step is to replace simulated emails with real messages retrieved from Gmail.

The future workflow could follow this architecture:

```text
Gmail Trigger
      ↓
New Email
      ↓
Subject and Body Extraction
      ↓
Email Classification
      ↓
Label Creation / Assignment
      ↓
Automatic Inbox Organization
```

It will also be possible to integrate artificial intelligence models to analyze the full context of incoming messages, making classification more flexible and accurate than a system based solely on predefined keywords.

---

## 🔒 Security

Files containing sensitive information, credentials, or environment variables should never be committed to the repository.

For example:

```text
.env
.env.*
```

These files should be excluded using `.gitignore`.

---

## 👨‍💻 Author

**Emanuel Vítor Fernandes Nascimento**

Back-End Developer | Automation

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) • [GitHub](https://github.com/emanuelvitorfn7-gif)

---

## ⭐ About the Project

This project was developed as part of my hands-on learning experience in **Back-End Development and Workflow Automation**.

By combining Python, JavaScript, and n8n, I built a practical email classification system focused on simplicity, maintainability, and future scalability.

The project allowed me to strengthen my understanding of **business logic, data processing, workflow orchestration, and integration between different technologies**, while exploring how automation can simplify repetitive tasks.
