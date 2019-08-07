from stockx import api

api = api.StockXScraper()
total_pages = 24


def run():
    for page in range(1, total_pages + 1):
        print(page)
        api.parse_products(
            api.get_listings(page=page)
        )
    return api.df


run()
api.df.to_csv('current_stockx_listings.csv')
