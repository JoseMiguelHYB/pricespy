import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def scrape_amazon(product_name: str):
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "es-ES,es;q=0.9"
    }

    query = product_name.replace(" ", "+")
    url = f"https://www.amazon.es/s?k={query}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "lxml")

        results = []

        for item in soup.select("div[data-component-type='s-search-result']")[:3]:  # Solo 3 productos
            title_elem = item.select_one("h2 a span")
            price_elem = item.select_one("span.a-price > span.a-offscreen")
            link_elem = item.select_one("h2 a")

            if title_elem and price_elem and link_elem:
                title = title_elem.text.strip()
                price = price_elem.text.strip().replace("€", "").replace(",", ".")
                link = f"https://www.amazon.es{link_elem.get('href')}"

                results.append({
                    "name": title,
                    "price": float(price),
                    "store": "Amazon",
                    "link": link
                })

        return results

    except Exception as e:
        print(f"[ERROR]: {e}")
        return []
