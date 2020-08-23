from BankSpyder import BankSpyder
from CustomExceptions import *


class YapiKrediSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _get_currency_table(self):
        tbody_ = self.page_soup.find('tbody', attrs={'id': 'currencyResultContent'})
        return tbody_

    def _get_rates_list(self):
        table_ = self._get_currency_table()
        return table_.findChildren('tr', recursive=False)

    @staticmethod
    def _get_currency_name(row):
        raw_name_ = row[0].getText()

        name_ = raw_name_.strip()

        return name_

    @staticmethod
    def _get_bank_rates(row):

        bank_buys = row[2].text.replace(',', '.')
        bank_sells = row[3].text.replace(',', '.')
        
        return float(bank_buys), float(bank_sells)

    def _extract_values(self, rates_list):
        
        extracted_values = []

        for row in rates_list:
            row_children = row.findChildren(recursive=False)

            currency_name_ = self._get_currency_name(row_children)
            bank_buys, bank_sells = self._get_bank_rates(row_children)

            values_tuple = (currency_name_, bank_buys, bank_sells)

            extracted_values.append(values_tuple)

        return extracted_values

    @staticmethod
    def _get_usd_value(values):
        for value in values:
            if value[0] == 'USD':
                return value

        raise CurrencyNotFoundException("Could not find USD in the scraped results")

    def get_single_reading(self):
        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)
        
        usd_value = self._get_usd_value(extracted_values)

        return usd_value
