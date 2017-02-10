from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CurrentUser(models.Model):
    user_email=models.EmailField(max_length=30,default="user@gmail.com")
    user_password=models.CharField(max_length=30,default='user_password')
   
    def __str__(self):
        return self.user_email



class Vendor(models.Model):
    
    vendor_name = models.CharField(max_length=50)
    vendor_email=models.EmailField(max_length=30,default="vendor@gmail.com")
    vendor_password=models.CharField(max_length=30,default='vendor_password')
    vendor_address = models.CharField(max_length=200)
    vendor_contactNo= models.CharField(max_length=10)
    vendor_feedback= models.IntegerField(default=0)
    
    def __unicode__(self):
        return '%s %s %s %s' % (self.vendor_name, self.vendor_email,self.vendor_address,self.vendor_contactNo)  

class Buyer(models.Model):
    
    buyer_name = models.CharField(max_length=50)
    buyer_email=models.EmailField(max_length=30,default="buyer@gmail.com")
    buyer_password=models.CharField(max_length=30,default='buyer_password')
    buyer_address = models.CharField(max_length=200)
    buyer_contactNo= models.CharField(max_length=10)
    buyer_regNo= models.IntegerField(default=0)
    def __unicode__(self):
        return '%s %s %s %s %s' % (self.buyer_name, self.buyer_email,self.buyer_address,self.buyer_contactNo,self.buyer_regNo)  
    




class TenderInfo(models.Model):
    
    buyer1 = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    tender_name = models.CharField(max_length=100)
    product_details = models.CharField(max_length=500)
    estimated_cost= models.IntegerField(default=0)
    tender_deadline= models.DateField(blank =True)
    tender_status= models.IntegerField(default=0)
    win_quote= models.IntegerField(default=0)
    win_vid= models.IntegerField(default=0)
    
    def __unicode__(self):
        return unicode(self.tender_deadline.strftime('%Y-%m-%d')) 


class TenderQuotation(models.Model):
    tender1 = models.ForeignKey(TenderInfo, on_delete=models.CASCADE)
    vendor1 = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    suggested_quotation= models.IntegerField(default=0)
    def __unicode__(self):
        return '%s %s %s ' % (self.tender1, self.vendor1,self.suggested_quotation)  



class VendorFeedback(models.Model):
      buyer2 = models.ForeignKey(Buyer, on_delete=models.CASCADE)
      vendor2 = models.ForeignKey(Vendor, on_delete=models.CASCADE)
      vendor_feedback= models.IntegerField(default=0)
      def __unicode__(self):
        return '%s %s %s ' % (self.buyer2, self.vendor2,self.vendor_feedback)  
      


