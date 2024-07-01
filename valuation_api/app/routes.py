from flask import Blueprint, request, jsonify
from .database import db , add_company, add_data, get_existing_dates, add_financial_ratios, add_company_profile
from .api import FinancialAPI
from .models import IncomeStatement, BalanceSheet, FinancialRatios, CashFlowStatement, CompanyProfile, Company
from .utils import map_income_statement_data, map_balance_sheet_data, map_cash_flow_statement_data, calculate_ratios, map_company_profile_data
import logging
from sqlalchemy.exc import SQLAlchemyError


bp = Blueprint('routes', __name__)
api = FinancialAPI()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@bp.route('/api/add_company', methods=['POST'])
def add_company_route():
    data = request.get_json()
    symbol = data.get('symbol')
    cik = data.get('cik')
    company_id = add_company(symbol, cik)
    if company_id:
        profile_data = api.fetch_company_profile(symbol)
        if profile_data:
            mapped_profile_data = map_company_profile_data(profile_data)
            profile_id = add_company_profile(company_id, mapped_profile_data)
            if profile_id:
                return jsonify({'message': 'Company and profile added successfully', 'company_id': company_id, 'profile_id': profile_id}), 201
            else:
                return jsonify({'message': 'Company added but failed to add profile', 'company_id': company_id}), 201
        else:
            return jsonify({'message': 'Company added but failed to fetch profile', 'company_id': company_id}), 201
    else:
        return jsonify({'message': 'Failed to add company'}), 400
    
@bp.route('/api/fetch_and_store', methods=['POST'])
def fetch_and_store():
    data = request.get_json()
    symbol = data.get('symbol')
    
    company = Company.query.filter_by(symbol=symbol).first()
    if not company:
        return jsonify({'message': 'Company not found'}), 404
    
    company_id = company.id

    income_data = api.fetch_data('income-statement', symbol)
    balance_data = api.fetch_data('balance-sheet-statement', symbol)
    cashflow_data = api.fetch_data('cash-flow-statement', symbol)

    if not income_data or not balance_data or not cashflow_data:
        return jsonify({'message': 'Failed to fetch all required data'}), 400

    mapped_income_data = map_income_statement_data(income_data, company_id)
    mapped_balance_data = map_balance_sheet_data(balance_data, company_id)
    mapped_cashflow_data = map_cash_flow_statement_data(cashflow_data, company_id)

    existing_income_dates = get_existing_dates(IncomeStatement, company_id)
    existing_balance_dates = get_existing_dates(BalanceSheet, company_id)
    existing_cashflow_dates = get_existing_dates(CashFlowStatement, company_id)

    new_income_data = [record for record in mapped_income_data if record['date'] not in existing_income_dates]
    new_balance_data = [record for record in mapped_balance_data if record['date'] not in existing_balance_dates]
    new_cashflow_data = [record for record in mapped_cashflow_data if record['date'] not in existing_cashflow_dates]

    if new_income_data:
        add_data(new_income_data, IncomeStatement)
    if new_balance_data:
        add_data(new_balance_data, BalanceSheet)
    if new_cashflow_data:
        add_data(new_cashflow_data, CashFlowStatement)

    return jsonify({'message': 'Data fetched and stored successfully'}), 200

@bp.route('/api/calculate_ratios', methods=['POST'])
def calculate_ratios_route():
    data = request.get_json()
    company_id = data.get('company_id')

    logger.debug(f"Calculating ratios for company_id: {company_id}")

    latest_income_statement = IncomeStatement.query.filter_by(company_id=company_id).order_by(IncomeStatement.date.desc()).first()
    latest_balance_sheet = BalanceSheet.query.filter_by(company_id=company_id).order_by(BalanceSheet.date.desc()).first()
    company_profile_data = CompanyProfile.query.filter_by(company_id=company_id).first()
    latest_cashflow_statement = CashFlowStatement.query.filter_by(company_id=company_id).order_by(CashFlowStatement.date.desc()).first()

    logger.debug(f"Latest income statement: {latest_income_statement}")
    logger.debug(f"Latest balance sheet: {latest_balance_sheet}")
    logger.debug(f"Company profile data: {company_profile_data}")

    if not latest_income_statement or not latest_balance_sheet or not company_profile_data:
        return jsonify({'message': 'Required financial statements not found'}), 400

    ratios = calculate_ratios(company_profile=company_profile_data, income_statement=latest_income_statement, balance_sheet=latest_balance_sheet, cash_flow=latest_cashflow_statement)

    logger.debug(f"Calculated ratios: {ratios}")

    add_financial_ratios(company_id, latest_income_statement.date, ratios)

    return jsonify(ratios), 200

@bp.route('/api/get_all_tickers', methods=['GET'])
def get_all_tickers_route():
    try:
        tickers = db.session.query(Company.symbol).all()
        return jsonify({'tickers': [ticker[0] for ticker in tickers]}), 200
    except SQLAlchemyError as e:
        print(f"Error retrieving tickers: {e}")
        return jsonify({'message': 'Failed to retrieve tickers'}), 500

@bp.route('/api/get_ratios', methods=['GET'])
def get_ratios_route():
    company_id = request.args.get('company_id')
    ratios = FinancialRatios.query.filter_by(company_id=company_id).all
    return jsonify(ratios), 200



