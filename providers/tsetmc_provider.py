from providers.base_provider import BaseProvider


TSETMC_SEARCH_URL = "https://old.tsetmc.com/tsev2/data/search.aspx"


class TsetmcProvider(BaseProvider):

    def __init__(self):
        super().__init__()


    def search_symbol(self, symbol):

        try:

            response = self.get(
                TSETMC_SEARCH_URL,
                params={
                    "name": symbol
                }
            )

            return response.text

        except Exception as e:

            print(
                f"TSETMC search error for {symbol}: {e}",
                flush=True
            )

            return None


    def parse_search_result(self, raw, symbol):

        """
        فعلاً فقط اسکلت Parser.
        استخراج کامل در مرحله بعد با فرمت واقعی TSETMC انجام می‌شود.
        """

        return {

            "symbol": symbol,

            "status": "found",

            "price": 0,
            "close": 0,

            "volume": 0,
            "value": 0,

            "trade_count": 0,

            "buy_power": 0,
            "sell_power": 0,

            "prices": [],

            "raw": raw[:200]

        }


    def get_market_data(self, symbol):

        raw = self.search_symbol(symbol)


        if not raw:

            return {

                "symbol": symbol,

                "status": "unavailable",

                "price": 0,
                "close": 0,

                "volume": 0,
                "value": 0,

                "trade_count": 0,

                "buy_power": 0,
                "sell_power": 0,

                "prices": []

            }


        return self.parse_search_result(
            raw,
            symbol
        )



def get_tsetmc(symbol):

    provider = TsetmcProvider()

    return provider.get_market_data(symbol)
