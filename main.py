import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, verify=False)  # <-- вимикає перевірку SSL
        if response.status_code == 200:
            data = response.json()
            print(f'"{data["content"]}"\n- {data["author"]}')
        else:
            print("Помилка сервера:", response.status_code)
    except requests.exceptions.SSLError as e:
        print("SSL помилка:", e)

get_random_quote()
