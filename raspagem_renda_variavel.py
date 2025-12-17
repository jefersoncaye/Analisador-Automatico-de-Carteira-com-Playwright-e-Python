from playwright.sync_api import sync_playwright
from datetime import datetime

CARTEIRA = [

    # CRIPTOS
    {"ativo": "BTC-BRL", "quantidade": 0.05, "preco_compra": 135000, "classe": "Cripto"},
    {"ativo": "ETH-BRL", "quantidade": 0.30, "preco_compra": 10500, "classe": "Cripto"},
    {"ativo": "XRP-BRL", "quantidade": 1200, "preco_compra": 2.90, "classe": "Cripto"},
    {"ativo": "SOL-BRL", "quantidade": 20, "preco_compra": 95.00, "classe": "Cripto"},

    # AÇÕES
    {"ativo": "ITSA3:BVMF", "quantidade": 200, "preco_compra": 8.40, "classe": "Ação"},
    {"ativo": "BBAS3:BVMF", "quantidade": 100, "preco_compra": 48.50, "classe": "Ação"},
    {"ativo": "PETR4:BVMF", "quantidade": 150, "preco_compra": 34.20, "classe": "Ação"},
    {"ativo": "VALE3:BVMF", "quantidade": 80, "preco_compra": 67.00, "classe": "Ação"},

    # FIIS
    {"ativo": "HGLG11:BVMF", "quantidade": 10, "preco_compra": 168.00, "classe": "FII"},
    {"ativo": "MXRF11:BVMF", "quantidade": 200, "preco_compra": 10.20, "classe": "FII"},
    {"ativo": "KNRI11:BVMF", "quantidade": 12, "preco_compra": 155.00, "classe": "FII"},
]



def buscar_preco_atual(page, ativo):
    url = f"https://www.google.com/finance/quote/{ativo}"
    page.goto(url, timeout=60000)

    preco_texto = page.locator("div[data-last-price] span").first.inner_text()

    preco = (
        preco_texto
        .replace("R$", "")
        .replace(".", "")
        .replace(",", ".")
        .strip()
    )

    return float(preco)


def processar_carteira(page):
    resultados = []

    for item in CARTEIRA:
        preco_atual = buscar_preco_atual(page, item["ativo"])

        valor_investido = item["quantidade"] * item["preco_compra"]
        valor_atual = item["quantidade"] * preco_atual
        resultado = valor_atual - valor_investido
        percentual = (resultado / valor_investido) * 100

        resultados.append({
            **item,
            "preco_atual": preco_atual,
            "valor_investido": valor_investido,
            "valor_atual": valor_atual,
            "resultado": resultado,
            "percentual": percentual
        })

    return resultados


def resumo_por_classe(resultados):
    resumo = {}

    for r in resultados:
        classe = r["classe"]
        resumo.setdefault(classe, {
            "investido": 0,
            "atual": 0,
            "resultado": 0
        })

        resumo[classe]["investido"] += r["valor_investido"]
        resumo[classe]["atual"] += r["valor_atual"]
        resumo[classe]["resultado"] += r["resultado"]

    return resumo


def main():
    print("\n========================================")
    print(" ANÁLISE AUTOMÁTICA DE CARTEIRA")
    print("========================================")

    print(f"Execução: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        resultados = processar_carteira(page)

        browser.close()

    # -------- DETALHE POR ATIVO --------
    print(">>> RESULTADO POR ATIVO\n")
    for r in resultados:
        print(
            f"{r['ativo']:12} | "
            f"Atual: R$ {r['preco_atual']:,.2f} | "
            f"Resultado: R$ {r['resultado']:,.2f} "
            f"({r['percentual']:.2f}%)"
        )

    # -------- RESUMO POR CLASSE --------
    print("\n>>> RESUMO POR CLASSE\n")
    resumo = resumo_por_classe(resultados)

    for classe, dados in resumo.items():
        perc = (dados["resultado"] / dados["investido"]) * 100
        print(
            f"{classe:7} | "
            f"Investido: R$ {dados['investido']:,.2f} | "
            f"Atual: R$ {dados['atual']:,.2f} | "
            f"Resultado: R$ {dados['resultado']:,.2f} "
            f"({perc:.2f}%)"
        )

        # -------- TOTAL GERAL DA CARTEIRA --------
    total_investido = sum(r["valor_investido"] for r in resultados)
    total_atual = sum(r["valor_atual"] for r in resultados)
    total_resultado = total_atual - total_investido
    total_percentual = (total_resultado / total_investido) * 100

    print("\n>>> TOTAL GERAL DA CARTEIRA\n")
    print(
        f"Investido: R$ {total_investido:,.2f}\n"
        f"Atual:     R$ {total_atual:,.2f}\n"
        f"Resultado: R$ {total_resultado:,.2f} "
        f"({total_percentual:.2f}%)"
    )

    # -------- RANKING --------
    melhor = max(resultados, key=lambda x: x["percentual"])
    pior = min(resultados, key=lambda x: x["percentual"])

    print("\n>>> RANKING\n")
    print(f"MELHOR ATIVO: {melhor['ativo']} ({melhor['percentual']:.2f}%)")
    print(f"PIOR ATIVO:   {pior['ativo']} ({pior['percentual']:.2f}%)")


if __name__ == "__main__":
    main()
