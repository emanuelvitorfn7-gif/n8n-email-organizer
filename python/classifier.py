"""
Email Classifier
Recebe JSON pelo STDIN com "subject" e "body", devolve JSON pelo STDOUT.
"""

import io
import json
import sys
import unicodedata

sys.stdin  = io.TextIOWrapper(sys.stdin.buffer,  encoding="utf-8-sig")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


KEYWORDS = {
    "Financeiro": [
        "boleto", "pagamento", "fatura", "cobranca", "pix", "nfe",
        "nota fiscal", "debito", "credito", "vencimento", "invoice",
    ],
    "Suporte": [
        "erro", "problema", "suporte", "falha", "nao funciona", "bug",
        "ajuda", "help", "ticket", "incidente",
    ],
    "Vendas": [
        "promocao", "desconto", "compre agora", "oferta", "gratis",
        "clique aqui", "ganhe", "propaganda", "venda", "oportunidade",
        "produto", "plano", "assine",
    ],
}


def normalize(text: str) -> str:
    """Remove acentos e converte para minúsculas."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def find_category(text: str) -> str:
    """Retorna a categoria da primeira palavra-chave encontrada, ou 'Outros'."""
    for category, keywords in KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    return "Outros"


def classify(subject: str, body: str) -> dict:
    text = normalize(subject + " " + body)
    return {"categoria": find_category(text)}


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    subject = data.get("subject", "")
    body = data.get("body", "")
    result = classify(subject, body)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
