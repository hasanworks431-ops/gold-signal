from providers.base_provider import BaseProvider


FIPIRAN_URL = "https://fund.fipiran.ir"


class FipiranProvider(BaseProvider):

    def __init__(self):
        super().__init__()


    def get_fund_data(self, symbol):

        try:

            response = self.get(
                FIPIRAN_URL
            )

            html = response.text


            # TODO:
            # استخراج واقعی NAV / AUM / Bubble
            # پس از مشخص شدن API یا ساختار صفحه FIPIRAN


            return {

                "symbol": symbol,

                "nav": None,

                "bubble": None,

                "aum": None,

                "source": "fipiran",

                "status": "partial",

                "raw": html[:200]

            }


        except Exception as e:

            print(
                f"FIPIRAN error for {symbol}: {e}",
                flush=True
            )


            return {

                "symbol": symbol,

                "nav": None,

                "bubble": None,

                "aum": None,

                "source": "fipiran",

                "status": "error"

            }



def get_fipiran(symbol):

    provider = FipiranProvider()

    return provider.get_fund_data(symbol)
