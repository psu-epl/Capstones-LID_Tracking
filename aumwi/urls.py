from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static



# Basic Website administration pages ******************************************
urlpatterns = [

  #URL for SM to verify user authorization
    url(r'^sm_login$', views.sm_login,
        name = 'sm_login'),

  #URL for SM to edit logout time
    url(r'^sm_logout$', views.sm_logout,
        name = 'sm_logout'),

  #URL for SM to edit AuthUser table
    url(r'^sm_add$', views.sm_add,
        name='sm_add'),
]



# Manager level pages *********************************************************

urlpatterns += [

  #---User Manipulation------------------------------------------------
  # add a user
    url(r'^adduser/', views.ManagerView.adduser,
        name = 'adduser'),
  # add authorized user
    url(r'^addauthuser/', views.ManagerView.addauthuser,
        name = 'addauthuser'),
  # edit a user
    url(r'^edituser/', views.ManagerView.edituser,
        name = 'edituser'),
  # Process User edit
    url(r'^updateuser/', views.ManagerView.updateuser,
        name = 'updateuser'),
  # confirm the deletion of a user
    url(r'^deluser/', views.ManagerView.deluser,
        name = 'deluser'),
  # confirmation a user was deleted
    url(r'^deluserconf/', views.ManagerView.deluserconf,
        name = 'deluserconf'),

  #---Station Manipulation---------------------------------------------
  # add a new station module
    url(r'^addstation/', views.ManagerView.addstation,
        name = 'addstation'),
  # edit a station module
    url(r'^editstation/', views.ManagerView.editstation,
        name = 'editstation'),
  # Process Station Module edit
    url(r'^updatesm/', views.ManagerView.updatestation,
        name = 'updatestation'),
  # confirm the deletion of a station module
    url(r'^delstation/', views.ManagerView.delstation,
        name = 'delstation'),
  # confirmation a station module was deleted
    url(r'^delstationconf/', views.ManagerView.delstationconf,
        name = 'delstationconf'),

  #---Searches---------------------------------------------------------
  # find a user
    url(r'^finduser/', views.ManagerView.finduser,
        name = 'finduser'),
  # find a station module
    url(r'^findstation/', views.ManagerView.findstation,
        name = 'findstation'),

  #---Reports----------------------------------------------------------
  # "Report Choices"
    url(r'^reports/$', views.ManagerView.reports, name='rpt_base'),

    url(r'^reports/',
        include([
        #Undefined Report
        url(r'^$', views.ManagerView.rpt_err, name='rpt_error'),
        #Reports involving date ranges
        url(r'^(?P<start_date>[0-9]{8})-(?P<end_date>[0-9]{8})/',
            include([
            url(r'^$', #Date Range
                views.ManagerView.usebyd,
                name='use_by_date'),
            url(r'^(?P<user>[\w-]+)/$', #User and Date Range
                views.ManagerView.usebyud,
                name='use_by_user_date'),
            url(r'^(?P<smid>[\d]+)/$',  #Smid and Date Range
                views.ManagerView.usebysmd,
                name='use_by_sm_date'),
            url(r'^(?P<user>[\w-]+)/(?P<smid>[\d]+)/$', #Smid, User, and Date Range
                views.ManagerView.usebysmud,
                name='use_by_sm_user_date'),
            ])),
        #Reports by user
        url(r'^(?P<user>[\w-]+)/',
            include([
            url(r'^$', #User
                views.ManagerView.usebyu,
                name='use_by_user'),
            url(r'^(?P<smid>[\d]+)/$', #User and Smid
                views.ManagerView.usebysmu,
                name='use_by_sm_user')
            ])),
        #Reports by Station Module
        url(r'^(?P<smid>[\d]+)/$', #Smid
            views.ManagerView.usebysm,
            name='use_by_sm'),
        ])),
]




# Owner Level Pages ***********************************************************

urlpatterns += [
  #URL for Database Administration Landing
    url(r'^databaseadmin/', views.OwnerView.databaseadmin,
        name = 'databaseadmin'),

  #URL for Database Backup Landing
    url(r'^databasebackup/', views.OwnerView.databasebackup,
        name = 'databasebackup'),

  #URL for Database Restore Landing
    url(r'^databaserestore/', views.OwnerView.databaserestore,
        name = 'databaserestore'),
]

#*** EOF URLS ***

