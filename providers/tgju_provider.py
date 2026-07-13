from providers.base_provider import BaseProvider


TGJU_URL = "https://www.tgju.org"


class TgjuProvider(BaseProvider):

    def __init__(self):
        super().__init__()


    def get_market_data(self):

        try:

            response = self.get(
                TGJU_URL
            )

            html = response.text


            # TODO:
            # استخراج واقعی:
            # Dollar
            # Gold
            # Ounce


            return {

                "gold": None,

                "dollar": None,

                "ounce": None,

                "source": "tgju",

                "status": "partial",

                "raw": html[:200]

            }


        except Exception as e:

            print(
                f"TGJU error: {e}",
                flush=True
            )


            return {

                "gold": None,

                "dollar": None,

                "ounce": None,

                "source": "tgju",

                "status": "error"

            }



def get_tgju():

    provider = TgjuProvider()

    return provider.get_market_data()
