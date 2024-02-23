from typing import Any
from django.contrib import admin
from .models import Transaction
from .views import user_transaction_email
# Register your models here.

@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display=['account','amount','balance_afet_transaction','transaction_type','loan_approve']
    
    def save_model(self, request, obj, form, change):
        if obj.loan_approve ==True:
            obj.account.balance +=obj.amount
            obj.balance_afet_transaction=obj.account.balance
            obj.save()
            user_transaction_email(obj.account.user, "loan approval message", "loan_approval_mail.html", obj.amount )
        super().save_model(request, obj, form, change)