from providers.base_provider import BaseProvider


RAHAVARD_URL = "https://rahavard365.com"


class RahavardProvider(BaseProvider):

    def __init__(self):
        super().__init__()


    def get_history(self, symbol):

        try:

            response = self.get(
                RAHAVARD_URL
            )

            html = response.text


            # TODO:
            # اتصال به API داخلی Rahavard
            # یا ساخت Scraper
            #
            # خروجی مورد انتظار:
            # prices
            # volume
            # dates


            return {

                "symbol": symbol,

                "prices": None,

                "volume": None,

                "dates": None,

                "ema20": None,
                "ema50": None,
                "ema200": None,

                "rsi": None,
                "macd": None,

                "source": "rahavard",

                "status": "partial",

                "raw": html[:200]

            }


        except Exception as e:

            print(
                f"Rahavard error for {symbol}: {e}",
                flush=True
            )


            return {

                "symbol": symbol,

                "prices": None,

                "volume": None,

                "dates": None,

                "ema20": None,
                "ema50": None,
                "ema200": None,

                "rsi": None,
                "macd": None,

                "source": "rahavard",

                "status": "error"

            }



def get_rahavard(symbol):

    provider = RahavardProvider()

    return provider.get_history(symbol)
