import csv
import pandas
accounts_relations = pandas.read_csv('account_relations.csv')
clients = pandas.read_csv('clients.csv')
transactions_history = pandas.read_csv('transactions_history.csv')
transactions_test = pandas.read_csv('transactions_test.csv')
print(clients['account_type'].tolist())
print(clients.iloc[10].tolist())