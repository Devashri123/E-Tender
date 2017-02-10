from django.conf.urls import url

from . import views


urlpatterns = [
    
    #/tenderApp
    url(r'^$', views.index, name='index'),
    url(r'^demo$', views.demo, name='demo'),

   
    #/tenderApp/homepage
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^help$', views.help, name='help'),
    url(r'^services$', views.services, name='services'),
    url(r'^openTenders$', views.openTenders, name='openTenders'),
    url(r'^closedTenders$', views.closedTenders, name='closedTenders'),

    #/tenderApp/login
    url(r'^login$', views.login, name='login'),
    url(r'^validate_login$', views.validate_login, name='validate_login'),
    url(r'^logout$', views.logout, name='logout'),
    
    




    #/tenderApp/create_buyer
    url(r'^create_buyer$', views.create_buyer, name='create_buyer'),
    #/tenderApp/create_vendor
    url(r'^create_vendor$', views.create_vendor, name='create_vendor'),

    #/tenderApp/vendorSignup
    url(r'^vendorSignup$', views.vendorSignup, name='vendorSignup'),
    #/tenderApp/buyerSignup
    url(r'^buyerSignup$', views.buyerSignup, name='buyerSignup'),

    #/tenderApp/vendorDashboard
    url(r'^vendorDashboard$', views.vendorDashboard, name='vendorDashboard'),
    #/tenderApp/allocatedTenders
    url(r'^allocatedTenders$', views.allocatedTenders, name='allocatedTenders'),
    #/tenderApp/openTenders
    url(r'^openTenders$', views.openTenders, name='openTenders'),
    #/tenderApp/appliedTenders
    url(r'^appliedTenders$', views.appliedTenders, name='appliedTenders'),

    #/tenderApp/buyerDashboard
    url(r'^buyerDashboard$', views.buyerDashboard, name='buyerDashboard'),
    #/tenderApp/createTender
    url(r'^createTender$', views.createTender, name='createTender'),
    #/tenderApp/trackTender
    url(r'^trackTender$', views.trackTender, name='trackTender'),


    url(r'^hello$', views.hello, name='hello'),
    url(r'^sample$', views.sample, name='sample'),
    #/tenderApp/234/
    url(r'^(?P<vendor_id>[0-9]+)/$', views.display_details, name='display_details'),
    url(r'^vendor_list$', views.vendor_list, name='vendor_list'),
    url(r'^buyer_list$', views.buyer_list, name='buyer_list'),
    url(r'^add$', views.add, name='add'),
    url(r'^read_vendor$', views.read_vendor, name='read_vendor'),
    url(r'^read_buyer$', views.read_buyer, name='read_buyer'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^update$', views.update, name='update'),
   
]

