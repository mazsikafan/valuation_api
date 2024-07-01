
import yfinance as yf
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from .database import db
from .models import Company, CompanyProfile, IncomeStatement, BalanceSheet, CashFlowStatement
def map_income_statement_data(api_data, company_id):
    mapped_data = []
    for record in api_data:
        mapped_record = {
            'company_id': company_id,
            'symbol': record.get('symbol'),
            'date': record.get('date'),
            'cik': record.get('cik'),
            'filling_date': record.get('fillingDate'),
            'accepted_date': record.get('acceptedDate'),
            'calendar_year': record.get('calendarYear'),
            'period': record.get('period'),
            'revenue': record.get('revenue'),
            'cost_of_revenue': record.get('costOfRevenue'),
            'gross_profit': record.get('grossProfit'),
            'gross_profit_ratio': record.get('grossProfitRatio'),
            'research_and_development_expenses': record.get('researchAndDevelopmentExpenses'),
            'general_and_administrative_expenses': record.get('generalAndAdministrativeExpenses'),
            'selling_and_marketing_expenses': record.get('sellingAndMarketingExpenses'),
            'selling_general_and_administrative_expenses': record.get('sellingGeneralAndAdministrativeExpenses'),
            'other_expenses': record.get('otherExpenses'),
            'operating_expenses': record.get('operatingExpenses'),
            'cost_and_expenses': record.get('costAndExpenses'),
            'interest_income': record.get('interestIncome'),
            'interest_expense': record.get('interestExpense'),
            'depreciation_and_amortization': record.get('depreciationAndAmortization'),
            'ebitda': record.get('ebitda'),
            'ebitda_ratio': record.get('ebitdaRatio'),
            'operating_income': record.get('operatingIncome'),
            'operating_income_ratio': record.get('operatingIncomeRatio'),
            'total_other_income_expenses_net': record.get('totalOtherIncomeExpensesNet'),
            'income_before_tax': record.get('incomeBeforeTax'),
            'income_before_tax_ratio': record.get('incomeBeforeTaxRatio'),
            'income_tax_expense': record.get('incomeTaxExpense'),
            'net_income': record.get('netIncome'),
            'net_income_ratio': record.get('netIncomeRatio'),
            'eps': record.get('eps'),
            'eps_diluted': record.get('epsDiluted'),
            'weighted_average_shs_out': record.get('weightedAverageShsOut'),
            'weighted_average_shs_out_dil': record.get('weightedAverageShsOutDil'),
            'link': record.get('link'),
            'final_link': record.get('finalLink')
        }
        mapped_data.append(mapped_record)
    return mapped_data

def map_balance_sheet_data(api_data, company_id):
    mapped_data = []
    for record in api_data:
        mapped_record = {
            'company_id': company_id,
            'symbol': record.get('symbol'),
            'date': record.get('date'),
            'reported_currency': record.get('reportedCurrency'),
            'cik': record.get('cik'),
            'filling_date': record.get('fillingDate'),
            'accepted_date': record.get('acceptedDate'),
            'calendar_year': record.get('calendarYear'),
            'period': record.get('period'),
            'cash_and_cash_equivalents': record.get('cashAndCashEquivalents'),
            'short_term_investments': record.get('shortTermInvestments'),
            'cash_and_short_term_investments': record.get('cashAndShortTermInvestments'),
            'net_receivables': record.get('netReceivables'),
            'inventory': record.get('inventory'),
            'other_current_assets': record.get('otherCurrentAssets'),
            'total_current_assets': record.get('totalCurrentAssets'),
            'property_plant_equipment_net': record.get('propertyPlantEquipmentNet'),
            'goodwill': record.get('goodwill'),
            'intangible_assets': record.get('intangibleAssets'),
            'goodwill_and_intangible_assets': record.get('goodwillAndIntangibleAssets'),
            'long_term_investments': record.get('longTermInvestments'),
            'tax_assets': record.get('taxAssets'),
            'other_non_current_assets': record.get('otherNonCurrentAssets'),
            'total_non_current_assets': record.get('totalNonCurrentAssets'),
            'other_assets': record.get('otherAssets'),
            'total_assets': record.get('totalAssets'),
            'account_payables': record.get('accountPayables'),
            'short_term_debt': record.get('shortTermDebt'),
            'tax_payables': record.get('taxPayables'),
            'deferred_revenue': record.get('deferredRevenue'),
            'other_current_liabilities': record.get('otherCurrentLiabilities'),
            'total_current_liabilities': record.get('totalCurrentLiabilities'),
            'long_term_debt': record.get('longTermDebt'),
            'deferred_revenue_non_current': record.get('deferredRevenueNonCurrent'),
            'deferred_tax_liabilities_non_current': record.get('deferredTaxLiabilitiesNonCurrent'),
            'other_non_current_liabilities': record.get('otherNonCurrentLiabilities'),
            'total_non_current_liabilities': record.get('totalNonCurrentLiabilities'),
            'other_liabilities': record.get('otherLiabilities'),
            'capital_lease_obligations': record.get('capitalLeaseObligations'),
            'total_liabilities': record.get('totalLiabilities'),
            'preferred_stock': record.get('preferredStock'),
            'common_stock': record.get('commonStock'),
            'retained_earnings': record.get('retainedEarnings'),
            'accumulated_other_comprehensive_income_loss': record.get('accumulatedOtherComprehensiveIncomeLoss'),
            'othertotal_stockholders_equity': record.get('othertotalStockholdersEquity'),
            'total_stockholders_equity': record.get('totalStockholdersEquity'),
            'total_equity': record.get('totalEquity'),
            'total_liabilities_and_stockholders_equity': record.get('totalLiabilitiesAndStockholdersEquity'),
            'minority_interest': record.get('minorityInterest'),
            'total_liabilities_and_total_equity': record.get('totalLiabilitiesAndTotalEquity'),
            'total_investments': record.get('totalInvestments'),
            'total_debt': record.get('totalDebt'),
            'net_debt': record.get('netDebt'),
            'link': record.get('link'),
            'final_link': record.get('finalLink')
        }
        mapped_data.append(mapped_record)
    return mapped_data

def map_cash_flow_statement_data(api_data, company_id):
    mapped_data = []
    for record in api_data:
        mapped_record = {
            'company_id': company_id,
            'symbol': record.get('symbol'),
            'date': record.get('date'),
            'reported_currency': record.get('reportedCurrency'),
            'cik': record.get('cik'),
            'filling_date': record.get('fillingDate'),
            'accepted_date': record.get('acceptedDate'),
            'calendar_year': record.get('calendarYear'),
            'period': record.get('period'),
            'net_income': record.get('netIncome'),
            'depreciation_and_amortization': record.get('depreciationAndAmortization'),
            'deferred_income_tax': record.get('deferredIncomeTax'),
            'stock_based_compensation': record.get('stockBasedCompensation'),
            'change_in_working_capital': record.get('changeInWorkingCapital'),
            'accounts_receivables': record.get('accountsReceivables'),
            'inventory': record.get('inventory'),
            'accounts_payables': record.get('accountsPayables'),
            'other_working_capital': record.get('otherWorkingCapital'),
            'other_non_cash_items': record.get('otherNonCashItems'),
            'net_cash_provided_by_operating_activities': record.get('netCashProvidedByOperatingActivities'),
            'investments_in_property_plant_and_equipment': record.get('investmentsInPropertyPlantAndEquipment'),
            'acquisitions_net': record.get('acquisitionsNet'),
            'purchases_of_investments': record.get('purchasesOfInvestments'),
            'sales_maturities_of_investments': record.get('salesMaturitiesOfInvestments'),
            'other_investing_activites': record.get('otherInvestingActivites'),
            'net_cash_used_for_investing_activites': record.get('netCashUsedForInvestingActivites'),
            'debt_repayment': record.get('debtRepayment'),
            'common_stock_issued': record.get('commonStockIssued'),
            'common_stock_repurchased': record.get('commonStockRepurchased'),
            'dividends_paid': record.get('dividendsPaid'),
            'other_financing_activites': record.get('otherFinancingActivites'),
            'net_cash_used_provided_by_financing_activities': record.get('netCashUsedProvidedByFinancingActivities'),
            'effect_of_forex_changes_on_cash': record.get('effectOfForexChangesOnCash'),
            'net_change_in_cash': record.get('netChangeInCash'),
            'cash_at_end_of_period': record.get('cashAtEndOfPeriod'),
            'cash_at_beginning_of_period': record.get('cashAtBeginningOfPeriod'),
            'operating_cash_flow': record.get('operatingCashFlow'),
            'capital_expenditure': record.get('capitalExpenditure'),
            'free_cash_flow': record.get('freeCashFlow'),
            'link': record.get('link'),
            'final_link': record.get('finalLink')
        }
        mapped_data.append(mapped_record)
    return mapped_data

def calculate_ratios(company_profile, income_statement, balance_sheet, cash_flow):
    ratios = {}
    try:
        # Calculating static ratios
        ratios['gross_margin'] = income_statement.gross_profit / income_statement.revenue if income_statement.revenue else None
        ratios['operating_margin'] = income_statement.operating_income / income_statement.revenue if income_statement.revenue else None
        ratios['net_margin'] = income_statement.net_income / income_statement.revenue if income_statement.revenue else None
        ratios['return_on_assets'] = income_statement.net_income / balance_sheet.total_assets if balance_sheet.total_assets else None
        ratios['return_on_equity'] = income_statement.net_income / balance_sheet.total_stockholders_equity if balance_sheet.total_stockholders_equity else None
        ratios['return_on_invested_capital'] = income_statement.operating_income / (balance_sheet.total_debt + balance_sheet.total_stockholders_equity) if (balance_sheet.total_debt + balance_sheet.total_stockholders_equity) else None
        ratios['current_ratio'] = balance_sheet.total_current_assets / balance_sheet.total_current_liabilities if balance_sheet.total_current_liabilities else None
        ratios['quick_ratio'] = (balance_sheet.total_current_assets - balance_sheet.inventory) / balance_sheet.total_current_liabilities if balance_sheet.total_current_liabilities else None
        ratios['cash_ratio'] = balance_sheet.cash_and_cash_equivalents / balance_sheet.total_current_liabilities if balance_sheet.total_current_liabilities else None
        ratios['debt_to_equity'] = balance_sheet.total_debt / balance_sheet.total_stockholders_equity if balance_sheet.total_stockholders_equity else None
        ratios['debt_to_assets'] = balance_sheet.total_debt / balance_sheet.total_assets if balance_sheet.total_assets else None
        ratios['interest_coverage'] = income_statement.operating_income / income_statement.interest_expense if income_statement.interest_expense else None
        ratios['asset_turnover'] = income_statement.revenue / balance_sheet.total_assets if balance_sheet.total_assets else None
        ratios['inventory_turnover'] = income_statement.cost_of_revenue / balance_sheet.inventory if balance_sheet.inventory else None
        ratios['days_sales_in_inventory'] = 365 / ratios['inventory_turnover'] if ratios['inventory_turnover'] else None
        ratios['days_sales_outstanding'] = (balance_sheet.net_receivables / income_statement.revenue) * 365 if income_statement.revenue else None
        ratios['days_payable_outstanding'] = (balance_sheet.account_payables / income_statement.cost_of_revenue) * 365 if income_statement.cost_of_revenue else None

        # Fetching previous period's income statement and balance sheet
        previous_income_statement = IncomeStatement.query.filter_by(company_id=income_statement.company_id).filter(IncomeStatement.date < income_statement.date).order_by(IncomeStatement.date.desc()).first()
        previous_balance_sheet = BalanceSheet.query.filter_by(company_id=balance_sheet.company_id).filter(BalanceSheet.date < balance_sheet.date).order_by(BalanceSheet.date.desc()).first()

        # Calculating growth ratios if previous data is available
        if previous_income_statement:
            ratios['revenue_growth'] = (income_statement.revenue - previous_income_statement.revenue) / previous_income_statement.revenue if previous_income_statement.revenue else None
            ratios['net_income_growth'] = (income_statement.net_income - previous_income_statement.net_income) / previous_income_statement.net_income if previous_income_statement.net_income else None

        if previous_balance_sheet:
            ratios['total_assets_growth'] = (balance_sheet.total_assets - previous_balance_sheet.total_assets) / previous_balance_sheet.total_assets if previous_balance_sheet.total_assets else None
            ratios['total_equity_growth'] = (balance_sheet.total_stockholders_equity - previous_balance_sheet.total_stockholders_equity) / previous_balance_sheet.total_stockholders_equity if previous_balance_sheet.total_stockholders_equity else None
            ratios['total_liabilities_growth'] = (balance_sheet.total_liabilities - previous_balance_sheet.total_liabilities) / previous_balance_sheet.total_liabilities if previous_balance_sheet.total_liabilities else None

        # Calculating other ratios
        ratios['dividend_payout_ratio'] = cash_flow.dividends_paid / income_statement.net_income if income_statement.net_income else None
        ratios['dividend_yield'] = cash_flow.dividends_paid / company_profile.price if company_profile.price else None
        ratios['price_to_earnings'] = company_profile.price / income_statement.eps if income_statement.eps else None
        ratios['price_to_sales'] = company_profile.price / income_statement.revenue if income_statement.revenue else None
        ratios['price_to_book'] = company_profile.price / balance_sheet.total_stockholders_equity if balance_sheet.total_stockholders_equity else None
        ratios['enterprise_value'] = company_profile.mkt_cap + balance_sheet.total_debt - balance_sheet.cash_and_cash_equivalents
        ratios['enterprise_value_to_revenue'] = ratios['enterprise_value'] / income_statement.revenue if income_statement.revenue else None
        ratios['enterprise_value_to_ebitda'] = ratios['enterprise_value'] / income_statement.ebitda if income_statement.ebitda else None



    except Exception as e:
        print(f"Error calculating ratios: {e}")
        return None
    return ratios



def map_company_profile_data(api_data):
    return {
        'symbol': api_data.get('symbol'),
        'price': api_data.get('price'),
        'beta': api_data.get('beta'),
        'vol_avg': api_data.get('volAvg'),
        'mkt_cap': api_data.get('mktCap'),
        'last_div': api_data.get('lastDiv'),
        'range': api_data.get('range'),
        'changes': api_data.get('changes'),
        'company_name': api_data.get('companyName'),
        'currency': api_data.get('currency'),
        'cik': api_data.get('cik'),
        'isin': api_data.get('isin'),
        'cusip': api_data.get('cusip'),
        'exchange': api_data.get('exchange'),
        'exchange_short_name': api_data.get('exchangeShortName'),
        'industry': api_data.get('industry'),
        'website': api_data.get('website'),
        'description': api_data.get('description'),
        'ceo': api_data.get('ceo'),
        'sector': api_data.get('sector'),
        'country': api_data.get('country'),
        'full_time_employees': api_data.get('fullTimeEmployees'),
        'phone': api_data.get('phone'),
        'address': api_data.get('address'),
        'city': api_data.get('city'),
        'state': api_data.get('state'),
        'zip': api_data.get('zip'),
        'dcf_diff': api_data.get('dcfDiff'),
        'dcf': api_data.get('dcf'),
        'image': api_data.get('image'),
        'ipo_date': api_data.get('ipoDate'),
        'is_etf': api_data.get('isEtf'),
        'is_actively_trading': api_data.get('isActivelyTrading'),
        'is_adr': api_data.get('isAdr'),
        'is_fund': api_data.get('isFund')
    }