from bs4 import BeautifulSoup
import requests

def buscarNoticias () :
    input_data = [
        {
            'url': 'https://eldeber.com.bo/',
            'params': [
                {
                    'selector': 'div.area:nth-child(1)',
                    'tag': 'a',
                    'class': 'nota-link'
                }            
            ]
        },
        {    
            'url': 'https://www.la-razon.com',
            'params': [
                {
                    'selector': '.post-content > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)',
                    'tag': 'a',
                    'class': 'title'
                },
                {
                    'selector': '.post-content > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)',
                    'tag': 'a',
                    'class': 'title'
                },
            ]
        },
        {    
            'url': 'https://www.eldiario.net/portal/',
            'params': [
                {
                    'selector': '.jeg_pl_lg_5 > div:nth-child(2) > h3:nth-child(1)',
                    'tag': 'a',
                    'class': ''
                },
            ]
        }
    ]

    result_noticias = []
    for data in input_data:
        url = data['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for params in data['params']:
            
            selector = soup.select(params['selector'])
            titulo =  selector[0].find_all(params['tag'], params['class']) if len(selector) > 0 else []
            print (url, len(titulo))
            for txt in titulo:
                result_noticias.append(txt.string)

    result_noticias = list(set(result_noticias))
    print(result_noticias)
    return result_noticias
