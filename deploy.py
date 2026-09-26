import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

N8N_URL = os.getenv("N8N_URL")
N8N_API_KEY = os.getenv("N8N_API_KEY")


def novo_id():
    return str(uuid.uuid4())


workflow = {
    "name": "Organizador Automático de Emails",

    "nodes": [

        # 1 - NOVO EMAIL
        {
            "parameters": {
                "pollTimes": {
                    "item": [
                        {
                            "mode": "everyMinute"
                        }
                    ]
                },
                "simple": True,
                "filters": {
                    "readStatus": "unread"
                }
            },
            "id": novo_id(),
            "name": "Novo Email",
            "type": "n8n-nodes-base.gmailTrigger",
            "typeVersion": 1.4,
            "position": [0, 300]
        },

        # 2 - CLASSIFICAR EMAIL
        {
            "parameters": {
                "jsCode": """
const assunto =
    ($json.Subject || $json.subject || '').toLowerCase();

let categoria = 'Outros';

const financeiro = [
    'boleto',
    'pagamento',
    'fatura',
    'cobrança',
    'nota fiscal',
    'pix'
];

const suporte = [
    'erro',
    'problema',
    'ajuda',
    'suporte',
    'falha'
];

const vendas = [
    'pedido',
    'comprar',
    'compra',
    'orçamento',
    'produto',
    'preço'
];

if (financeiro.some(p => assunto.includes(p))) {

    categoria = 'Financeiro';

} else if (suporte.some(p => assunto.includes(p))) {

    categoria = 'Suporte';

} else if (vendas.some(p => assunto.includes(p))) {

    categoria = 'Vendas';

}

return [
    {
        json: {
            ...$json,
            categoria: categoria
        }
    }
];
"""
            },
            "id": novo_id(),
            "name": "Classificar Email",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [300, 300]
        },

        # 3 - SEPARAR CATEGORIA
        {
            "parameters": {
                "rules": {
                    "values": [

                        {
                            "conditions": {
                                "options": {
                                    "caseSensitive": False
                                },
                                "conditions": [
                                    {
                                        "leftValue": "={{ $json.categoria }}",
                                        "rightValue": "Financeiro",
                                        "operator": {
                                            "type": "string",
                                            "operation": "equals"
                                        }
                                    }
                                ]
                            },
                            "renameOutput": True,
                            "outputKey": "Financeiro"
                        },

                        {
                            "conditions": {
                                "options": {
                                    "caseSensitive": False
                                },
                                "conditions": [
                                    {
                                        "leftValue": "={{ $json.categoria }}",
                                        "rightValue": "Suporte",
                                        "operator": {
                                            "type": "string",
                                            "operation": "equals"
                                        }
                                    }
                                ]
                            },
                            "renameOutput": True,
                            "outputKey": "Suporte"
                        },

                        {
                            "conditions": {
                                "options": {
                                    "caseSensitive": False
                                },
                                "conditions": [
                                    {
                                        "leftValue": "={{ $json.categoria }}",
                                        "rightValue": "Vendas",
                                        "operator": {
                                            "type": "string",
                                            "operation": "equals"
                                        }
                                    }
                                ]
                            },
                            "renameOutput": True,
                            "outputKey": "Vendas"
                        }

                    ]
                },

                "options": {
                    "fallbackOutput": "extra"
                }
            },

            "id": novo_id(),
            "name": "Separar Categoria",
            "type": "n8n-nodes-base.switch",
            "typeVersion": 3.3,
            "position": [600, 300]
        },

        # 4 - FINANCEIRO
        {
            "parameters": {},
            "id": novo_id(),
            "name": "Financeiro",
            "type": "n8n-nodes-base.noOp",
            "typeVersion": 1,
            "position": [900, 0]
        },

        # 5 - SUPORTE
        {
            "parameters": {},
            "id": novo_id(),
            "name": "Suporte",
            "type": "n8n-nodes-base.noOp",
            "typeVersion": 1,
            "position": [900, 200]
        },

        # 6 - VENDAS
        {
            "parameters": {},
            "id": novo_id(),
            "name": "Vendas",
            "type": "n8n-nodes-base.noOp",
            "typeVersion": 1,
            "position": [900, 400]
        },

        # 7 - OUTROS
        {
            "parameters": {},
            "id": novo_id(),
            "name": "Outros",
            "type": "n8n-nodes-base.noOp",
            "typeVersion": 1,
            "position": [900, 600]
        }
    ],

    "connections": {

        "Novo Email": {
            "main": [
                [
                    {
                        "node": "Classificar Email",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },

        "Classificar Email": {
            "main": [
                [
                    {
                        "node": "Separar Categoria",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },

        "Separar Categoria": {
            "main": [

                [
                    {
                        "node": "Financeiro",
                        "type": "main",
                        "index": 0
                    }
                ],

                [
                    {
                        "node": "Suporte",
                        "type": "main",
                        "index": 0
                    }
                ],

                [
                    {
                        "node": "Vendas",
                        "type": "main",
                        "index": 0
                    }
                ],

                [
                    {
                        "node": "Outros",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        }
    },

    "settings": {
        "executionOrder": "v1"
    }
}


headers = {
    "X-N8N-API-KEY": N8N_API_KEY,
    "Content-Type": "application/json"
}


print("Criando organizador de emails no n8n...")


resposta = requests.post(
    f"{N8N_URL}/api/v1/workflows",
    headers=headers,
    json=workflow
)


if resposta.status_code in [200, 201]:

    dados = resposta.json()

    print()
    print("======================================")
    print("✅ ORGANIZADOR CRIADO COM SUCESSO")
    print("======================================")
    print("Nome:", dados.get("name"))
    print("ID:", dados.get("id"))
    print()
    print("Abra:", N8N_URL)

else:

    print()
    print("❌ ERRO")
    print("Status:", resposta.status_code)
    print(resposta.text)