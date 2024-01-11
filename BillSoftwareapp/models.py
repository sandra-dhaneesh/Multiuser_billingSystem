from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    Company_code = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    pan_number = models.CharField(max_length=255,null=True,blank=True)
    gst_type = models.CharField(max_length=255,null=True,blank=True)
    gst_no = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')


class staff_details(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    user_name = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    img = models.ImageField(null=True,blank = True,upload_to = 'image/staff')    
    position = models.CharField(max_length=255,null=True,blank=True,default='staff')

class party(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True)
    party_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    gst_type = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    openingbalance = models.CharField(max_length=100,default='0',null=True,blank=True)
    payment = models.CharField(max_length=100,null=True,blank=True)
    creditlimit = models.CharField(max_length=100,default='0',null=True,blank=True)
    current_date = models.DateField(max_length=255,null=True,blank=True)
    End_date = models.CharField(max_length=255,null=True,blank=True)
    additionalfield1 = models.CharField(max_length=100,null=True,blank=True)
    additionalfield2 = models.CharField(max_length=100,null=True,blank=True)
    additionalfield3 = models.CharField(max_length=100,null=True,blank=True)


class BankModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,blank=True,null=True)
    bank_name = models.CharField(max_length=255)
    account_num = models.PositiveBigIntegerField(null=True)
    ifsc = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    upi_id = models.CharField(max_length=255)
    as_of_date = models.DateField(null=True)
    card_type = models.CharField(max_length=255)
    open_balance = models.BigIntegerField(null=True)
    current_balance = models.BigIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255,null=True)

class modules_list(models.Model): 
    company = models.ForeignKey(company, on_delete=models.CASCADE,null=True,blank=True) 
    sales_invoice = models.CharField(max_length=100,null=True,default=0)   
    Estimate = models.IntegerField(null=True,default=0)
    Payment_in = models.IntegerField(null=True,default=0) 
    sales_order = models.IntegerField(null=True,default=0)     
    Delivery_challan = models.IntegerField(null=True,default=0) 
    sales_return = models.IntegerField(null=True,default=0) 

    Purchase_bills = models.IntegerField(null=True,default=0)   
    Payment_out = models.IntegerField(null=True,default=0)  
    Purchase_order = models.IntegerField(null=True,default=0)   
    Purchase_return = models.IntegerField(null=True,default=0)  

    Bank_account = models.IntegerField(null=True,default=0)   
    Cash_in_hand = models.IntegerField(null=True,default=0)  
    cheques = models.IntegerField(null=True,default=0)   
    Loan_account = models.IntegerField(null=True,default=0) 
    Upi = models.IntegerField(null=True,default=0) 

    update_action = models.IntegerField(null=True,default=0) 
    status = models.CharField(max_length=100,null=True,default='New') 

class ItemModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=255)
    item_hsn = models.PositiveIntegerField(null=True)
    item_unit = models.CharField(max_length=255)
    item_taxable = models.CharField(max_length=255)
    item_gst = models.CharField(max_length=255,null=True)
    item_igst = models.CharField(max_length=255,null=True)
    item_sale_price = models.PositiveIntegerField()
    item_purchase_price = models.PositiveBigIntegerField()
    item_opening_stock = models.PositiveBigIntegerField(default=0)
    item_current_stock = models.PositiveBigIntegerField(default=0)
    item_at_price = models.PositiveBigIntegerField(default=0)
    item_date = models.DateField()
    item_min_stock_maintain = models.PositiveBigIntegerField(default=0)


class UnitModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    unit_name = models.CharField(max_length=255)

class purchasedebit(models.Model):
    pdebitid = models.AutoField(('pdid'), primary_key=True)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    party = models.ForeignKey(party, on_delete=models.CASCADE,null=True,blank=True)
    reference_number=models.TextField(max_length=100,null=True,blank=True)
    debitdate = models.DateField(null=True)
    billno = models.CharField(max_length=150,null=True)
    billdate = models.CharField(max_length=100,null=True)
    supply = models.CharField(max_length=150,null=True)
    subtotal = models.CharField(max_length=100,null=True)
    sgst = models.CharField(max_length=100,null=True)
    cgst = models.CharField(max_length=100,null=True)
    igst = models.CharField(max_length=100,null=True)
    taxamount = models.CharField(max_length=100,null=True)
    grandtotal = models.CharField(max_length=100,null=True)
    adjustment = models.FloatField(default=0,null=True,blank=True)
    paid_amount = models.FloatField(blank=True,null=True)
    balance_amount = models.FloatField(blank=True,null=True)
    payment_type = models.CharField(max_length=100,null=True)
    cheque_no = models.CharField(max_length=255, default='', null=True)
    upi_no = models.CharField(max_length=255, default='', null=True)
    tot_debt_no = models.IntegerField(default=0, null=True)

class purchasedebit1(models.Model):
    pdebit = models.ForeignKey(purchasedebit, on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(company,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(ItemModel,on_delete=models.CASCADE,null=True)
    qty = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    tax = models.CharField(max_length=100,null=True)
    discount = models.IntegerField(default=0, null=True)


class DebitnoteTransactionHistory(models.Model):
    debitnote = models.ForeignKey(purchasedebit,on_delete=models.CASCADE)
    staff = models.ForeignKey(staff_details,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,null=True,blank=True)
    CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
    ]
    action = models.CharField(max_length=20, choices=CHOICES)
    transactiondate = models.DateField(auto_now=True)

