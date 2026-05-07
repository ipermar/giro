import time
import pandas as pd
import asyncio

#URL="https://api.allorigins.win/raw?url=https://www.procyclingstats.com/race/giro-d-italia/2026/startlist"
#URL = "https://firstcycling.com/race.php?r=13&y=2026&k=8"


anio=2026
URL = f"https://www.procyclingstats.com/race/giro-d-italia/{anio}}/startlist"


def _parse_startlist(soup) -> pd.DataFrame:
    """Extrae corredores y dorsales del HTML parseado."""
    from bs4 import BeautifulSoup

    riders = []

    # procyclingstats estructura el startlist en divs con clase 'ridersCont'
    # Cada equipo tiene un bloque ul con los corredores
    teams = soup.find_all("ul", class_=lambda c: c and "startlist" in c.lower())

    # Fallback: buscar todos los <li> que contengan número de dorsal
    if not teams:
        # Estructura alternativa: tabla o lista plana
        items = soup.select("li.rider, div.rider, .startlist li")
        for item in items:
            bib_tag = item.find(class_=lambda c: c and "bib" in c.lower()) or item.find("span")
            name_tag = item.find("a")
            if name_tag:
                bib = bib_tag.get_text(strip=True) if bib_tag else ""
                name = name_tag.get_text(strip=True)
                riders.append({"dorsal": bib, "corredor": name})
    else:
        for ul in teams:
            for li in ul.find_all("li"):
                a_tag = li.find("a")
                # El dorsal suele estar en el primer texto del <li>
                texts = list(li.stripped_strings)
                bib = texts[0] if texts and texts[0].isdigit() else ""
                name = a_tag.get_text(strip=True) if a_tag else ""
                if name:
                    riders.append({"dorsal": bib, "corredor": name})

    # Segunda estrategia de parseo: buscar tabla con números y nombres
    if not riders:
        for row in soup.select("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                bib_text = cells[0].get_text(strip=True)
                name_tag = cells[1].find("a") or cells[1]
                name_text = name_tag.get_text(strip=True)
                if bib_text.isdigit() and name_text:
                    riders.append({"dorsal": bib_text, "corredor": name_text})

    return pd.DataFrame(riders)


async def scrape_with_playwright() -> pd.DataFrame:
    """
    Usa Playwright para renderizar la página como un navegador real.
    Necesario si el contenido se carga via JavaScript.
    """
    #from playwright.sync_api import sync_playwright
    from playwright.async_api import async_playwright
    from bs4 import BeautifulSoup

    async with async_playwright() as p:
        browser =  await p.chromium.launch(headless=True)
        context =  await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="es-ES",
        )
        page =  await context.new_page()

        # Visita home primero para evitar detección
        #await page.goto("https://firstcycling.com/", wait_until="domcontentloaded")

        #await page.wait_for_timeout(2000)
        await page.goto(URL, wait_until="domcontentloaded", timeout=30000)
        #await page.wait_for_timeout(2000)
        #await page.wait_for_selector("ul.startlist_v4", timeout=60000)
        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    return _parse_startlist(soup)


corredores=asyncio.run(scrape_with_playwright())
corredores.to_excel("data/startlist_giro_2026.xlsx", index=False)
