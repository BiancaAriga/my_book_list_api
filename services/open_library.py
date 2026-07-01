import requests


def buscar_capa_livro(nome: str, autor: str) -> str | None:
    try:
        response = requests.get(
            "https://openlibrary.org/search.json",
            params={"q": f"{nome} {autor}", "limit": 1},
            timeout=5,
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    docs = response.json().get("docs", [])
    if not docs:
        return None

    doc = docs[0]
    cover_id = doc.get("cover_i")
    if cover_id:
        return f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

    isbns = doc.get("isbn") or []
    if isbns:
        return f"https://covers.openlibrary.org/b/isbn/{isbns[0]}-L.jpg"

    return None
