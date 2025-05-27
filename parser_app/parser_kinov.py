import requests
from bs4 import BeautifulSoup as BS

# Ссылка сайта
URL = 'https://kinovibe.co/genreserial/melodrama/'

# Заголовки — чтобы не считали ботом
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}

# Получение HTML
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

# Получение данных из HTML
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_='custom1-item')  # Возможно, нужно изменить селектор
    kinov_list = []

    for item in items:
        title = item.get_text(strip=True)
        kinov_list.append({
            'title': title,
        })
    return kinov_list

# Парсинг
def parsing_kinov():
    response = get_html(URL)
    if response.status_code == 200:
        kinov_list_2 = []
        for page in range(1, 2):  # Можно увеличить диапазон
            response = get_html(URL, params={'page': page})
            kinov_list_2.extend(get_data(response.text))
        return kinov_list_2
    else:
        raise Exception('Ошибка при парсинге страницы')

# Точка входа
if __name__ == '__main__':
    data = parsing_kinov()
    for item in data:
        print(item)
