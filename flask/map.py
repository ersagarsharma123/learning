# Python Interview Question: Mapping Sales Invoice Payments to Invoices 
# You are provided with two lists of dictionaries representing sales invoice data and sales invoice payments. The sales_invoice_data list contains information about invoices, including fields such as invoice number, customer, total amount, currency, and posting date. The sales_invoice_payments list contains information about payments made towards these invoices, including fields such as payment ID, invoice number (parent), amount, mode of payment, type, and account.
# Your task is to write a Python function named map_payments_to_invoices(sales_invoice_data, sales_invoice_payments) to efficiently map each payment to its corresponding invoice using the invoice number. Then, create a consolidated view that includes invoice details along with associated payments.

# Input:
sales_invoice_data = [
    {'name': 'INV001', 'customer': 'John Doe', 'total_amount': 1500, 'currency': 'USD', 'posting_date': '2024-06-10'},
    {'name': 'INV002', 'customer': 'Jane Smith', 'total_amount': 2000, 'currency': 'EUR', 'posting_date': '2024-06-11'},
    {'name': 'INV003', 'customer': 'Alice Johnson', 'total_amount': 1200, 'currency': 'GBP', 'posting_date': '2024-06-12'}
]

sales_invoice_payments = [
    {'parent': 'INV001', 'name': 'PAY001', 'amount': 500, 'mode_of_payment': 'Credit Card', 'type': 'Income', 'account': 'Accounts Receivable'},
    {'parent': 'INV002', 'name': 'PAY002', 'amount': 1000, 'mode_of_payment': 'Cash', 'type': 'Income', 'account': 'Cash'},
    {'parent': 'INV001', 'name': 'PAY003', 'amount': 200, 'mode_of_payment': 'Cheque', 'type': 'Income', 'account': 'Accounts Receivable'}
]

for data in sales_invoice_data:
    name = data.get('name')
    for payment in sales_invoice_payments:
        invoice_number = payment.get('parent')
        if invoice_number == name:
            data.update({'payment': payment})

print('sales_invoice_data=', sales_invoice_data)

[{'name': 'PAY003', 'customer': 'John Doe', 'total_amount': 1500, 'currency': 'USD', 'posting_date': '2024-06-10', 'parent': 'INV001', 'amount': 200, 'mode_of_payment': 'Cheque', 'type': 'Income', 'account': 'Accounts Receivable'}, 
 {'name': 'PAY002', 'customer': 'Jane Smith', 'total_amount': 2000, 'currency': 'EUR', 'posting_date': '2024-06-11', 'parent': 'INV002', 'amount': 1000, 'mode_of_payment': 'Cash', 'type': 'Income', 'account': 'Cash'}, {'name': 'INV003', 'customer': 'Alice Johnson', 'total_amount': 1200, 'currency': 'GBP', 'posting_date': '2024-06-12'}]



[{'name': 'INV001', 'customer': 'John Doe', 'total_amount': 1500, 'currency': 'USD', 'posting_date': '2024-06-10', 'payment': {'parent': 'INV001', 'name': 'PAY003', 'amount': 200, 'mode_of_payment': 'Cheque', 'type': 'Income', 'account': 'Accounts Receivable'}}, 
 {'name': 'INV002', 'customer': 'Jane Smith', 'total_amount': 2000, 'currency': 'EUR', 'posting_date': '2024-06-11', 'payment': {'parent': 'INV002', 'name': 'PAY002', 'amount': 1000, 'mode_of_payment': 'Cash', 'type': 'Income', 'account': 'Cash'}}, {'name': 'INV003', 'customer': 'Alice Johnson', 'total_amount': 1200, 'currency': 'GBP', 'posting_date': '2024-06-12'}]


# result = 
# [
#     {'invoice_number': 'INV001', 'customer': 'John Doe', 'total_amount': 1500, 'currency': 'USD', 'posting_date': '2024-06-10', 'payments': [{'payment_id': 'PAY001', 'amount': 500, 'mode_of_payment': 'Credit Card', 'type': 'Income', 'account': 'Accounts Receivable'}, {'payment_id': 'PAY003', 'amount': 200, 'mode_of_payment': 'Cheque', 'type': 'Income', 'account': 'Accounts Receivable'}]},
#     {'invoice_number': 'INV002', 'customer': 'Jane Smith', 'total_amount': 2000, 'currency': 'EUR', 'posting_date': '2024-06-11', 'payments': [{'payment_id': 'PAY002', 'amount': 1000, 'mode_of_payment': 'Cash', 'type': 'Income', 'account': 'Cash'}]},
#     {'invoice_number': 'INV003', 'customer': 'Alice Johnson', 'total_amount': 1200, 'currency': 'GBP', 'posting_date': '2024-06-12', 'payments

