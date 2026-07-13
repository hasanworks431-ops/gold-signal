from providers.base_provider import BaseProvider


FIPIRAN_URL = "https://fund.fipiran.ir"


class FipiranProvider(BaseProvider):

    def __init__(self):
        super().__init__()

    def get_fund_data(self, symbol):

        try:

            response = self.get(FIPIRAN_URL)

            html = response.text

            # مرحله بعد اینجا NAV و Bubble استخراج می‌شود

            return {

                "symbol": symbol,

                "nav": 0,

                "bubble": 0,

                "aum": 0,

                "source": "fipiran",

                "status": "ok",

                "html": html[:200]

            }

        except Exception as e:

            print(
                f"FIPIRAN error for {symbol}: {e}",
                flush=True
            )

            return {

                "symbol": symbol,

                "nav": 0,

                "bubble": 0,

                "aum": 0,

                "source": "fipiran",

                "status": "error"

            }


def get_fipiran(symbol):

    provider = FipiranProvider()

    return provider.get_fund_data(symbol)
