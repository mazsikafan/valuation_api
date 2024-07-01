from sqlalchemy.exc import SQLAlchemyError
from .models import db, Company, FinancialRatios, IncomeStatement, BalanceSheet, CashFlowStatement, CompanyProfile
from .api import FinancialAPI
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

def add_company(symbol, cik):
    existing_company = Company.query.filter_by(symbol=symbol).first()
    if existing_company:
        return existing_company.id
    
    company = Company(symbol=symbol, cik=cik)
    try:
        db.session.add(company)
        db.session.commit()
        return company.id
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding company: {e}")
        return None

def add_company_profile(company_id, profile_data):
    try:
        profile = CompanyProfile(company_id=company_id, **profile_data)
        db.session.add(profile)
        db.session.commit()
        return profile.id
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding company profile: {e}")
        return None
    
def add_data(data, model):
    try:
        for record in data:
            if 'date' in record and not record['date']:
                continue
            db.session.merge(model(**record))
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding data to {model.__tablename__}: {e}")

def get_existing_dates(model, company_id):
    try:
        results = db.session.query(model.date).filter_by(company_id=company_id).all()
        return set(result[0] for result in results)
    except SQLAlchemyError as e:
        print(f"Error retrieving existing dates from {model.__tablename__}: {e}")
        return set()
    

def add_financial_ratios(company_id, date, ratios):
    financial_ratios = FinancialRatios(
        company_id=company_id,
        date=date,
        gross_margin=ratios.get('gross_margin'),
        operating_margin=ratios.get('operating_margin'),
        net_margin=ratios.get('net_margin'),
        return_on_assets=ratios.get('return_on_assets'),
        return_on_equity=ratios.get('return_on_equity'),
        return_on_invested_capital=ratios.get('return_on_invested_capital'),
        current_ratio=ratios.get('current_ratio'),
        quick_ratio=ratios.get('quick_ratio'),
        cash_ratio=ratios.get('cash_ratio'),
        debt_to_equity=ratios.get('debt_to_equity'),
        debt_to_assets=ratios.get('debt_to_assets'),
        interest_coverage=ratios.get('interest_coverage'),
        asset_turnover=ratios.get('asset_turnover'),
        inventory_turnover=ratios.get('inventory_turnover'),
        days_sales_in_inventory=ratios.get('days_sales_in_inventory'),
        days_sales_outstanding=ratios.get('days_sales_outstanding'),
        days_payable_outstanding=ratios.get('days_payable_outstanding'),
        revenue_growth=ratios.get('revenue_growth'),
        net_income_growth=ratios.get('net_income_growth'),
        total_assets_growth=ratios.get('total_assets_growth'),
        total_equity_growth=ratios.get('total_equity_growth'),
        total_liabilities_growth=ratios.get('total_liabilities_growth'),
        dividend_payout_ratio=ratios.get('dividend_payout_ratio'),
        dividend_yield=ratios.get('dividend_yield'),
        price_to_earnings=ratios.get('price_to_earnings'),
        price_to_sales=ratios.get('price_to_sales'),
        price_to_book=ratios.get('price_to_book'),
        enterprise_value=ratios.get('enterprise_value'),
        enterprise_value_to_revenue=ratios.get('enterprise_value_to_revenue'),
        enterprise_value_to_ebitda=ratios.get('enterprise_value_to_ebitda')
    )

    try:
        db.session.add(financial_ratios)
        db.session.commit()
        logger.debug(f"Financial ratios added to database for company_id: {company_id}, date: {date}")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding financial ratios: {e}")
        logger.error(f"Error adding financial ratios: {e}")
        logger.debug(f"Financial ratios data: {financial_ratios}")
