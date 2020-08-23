from BankSpyder import BankSpyder
from CustomExceptions import *


class YapiKrediSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _get_currency_table(self):
        top_container = self.page_soup.find('tbody', attrs={'id': 'currencyResultContent'})

    def _get_rates_list(self):
        table_ = self._get_currency_table()

    def _extract_values(self, rates_list):
        pass

    @staticmethod
    def _get_usd_value(values):
        pass

    def get_single_reading(self):
        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd_value(extracted_values)
