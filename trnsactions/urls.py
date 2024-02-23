

from django.urls import path
from .views import DepositMoneyView,WithdrawMoneyView,TransactionReportView,LoanListView,PayLoanView, LoanRequestView

# from .import views
urlpatterns = [
    path('diposit', DepositMoneyView.as_view(), name='diposit'),
    path('withdraw', WithdrawMoneyView.as_view(), name='Withdraw'),
    path('transaction_report', TransactionReportView.as_view(), name='transaction_report'),
    path('loan_list', LoanListView.as_view(), name='loan_list'),
    path('pay_loan/<int:loan_id>/', PayLoanView.as_view(), name='pay_loan'),
    path('loan_request', LoanRequestView.as_view(), name='loan_request'),
    
]
