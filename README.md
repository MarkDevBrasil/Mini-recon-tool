# Mini Recon Tool

Ferramenta simples em Python para fins educacionais. Ela permite verificar algumas portas TCP e conferir a presença de determinados headers de segurança HTTP.

## Funcionalidades

- Verifica as portas definidas na lista do código.
- Confere os headers `Strict-Transport-Security` e `X-Frame-Options`.
- Permite repetir a verificação sem reiniciar o programa.

> O programa verifica apenas as portas configuradas; ele não faz uma varredura de todas as portas.

## Requisitos

- Python 3
- Biblioteca `requests`

Instale a dependência com:

```bash
python -m pip install requests
