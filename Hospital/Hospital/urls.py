
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.BASE,name='base'),

    path('patient/add',views.ADD_PATIENT,name='add_patient'),
    path('patient/about',views.ABOUT_PATIENT,name='about_patient'),
    path('patient/all',views.ALL_PATIENT,name='all_patient'),
    path('patient/update/<int:patient_id>',views.Update_Patient,name='update_patient'),
    path('patient/edit/<int:patient_id>',views.EDIT_PATIENT,name='edit_patient'),
    path('patient/search',views.Search_PATIENT,name='search_patient'),

    path('doctor/add',views.ADD_DOCTOR,name='add_doctor'),
    path('doctor/about',views.ABOUT_DOCTOR,name='about_doctor'),
    path('doctor/all',views.ALL_DOCTOR,name='all_doctor'),
    path('doctor/update/<int:doctor_id>',views.Update_Doctor,name='update_doctor'),
    path('doctor/edit/<int:doctor_id>',views.EDIT_DOCTOR,name='edit_doctor'),

    path('appointment/add',views.ADD_APPOINTMENT,name='add_appointments'),
    path('appointment/all',views.ALL_APPOINTMENT,name='all_appointment'),
    path('appointment/about',views.ABOUT_APPOINTMENT,name='about_appointment'),
    path('appointment/update/<int:appointment_id>',views.Update_Appointment,name='update_appointment'),
    path('appointment/edit/<int:appointment_id>',views.EDIT_APPOINTMENT,name='edit_appointment'),

    path('payment/add',views.ADD_PAYMENT,name='add_payment'),
    # path('payment/service',views.ADD_SERVICE,name='payment_service'),
    path('payment/all',views.ALL_PAYMENT,name='all_pyment'),
    path('payment/invoice',views.INVOICE,name='invoice_pyment'),
    path('payment/invoice_E/<int:invoice_id>/<int:patient_id>',views.Invoice_E,name='invoice_E'),
    #path('payment/display_invoice/<int:invoice_id>/<int:patient_id>',views.Display_Invoice,name='display_invoice'),


    path('room_allotment/add',views.ADD_ROOM_A,name='add_room_allotment'),
    path('room_allotment/all',views.ALL_ROOM_A,name='all_room_allotment'),
    path('room_allotment/update/<int:room_s__roomnumber>',views.Update_Room_A,name='update_room_allotment'),
    path('room_allotment/edit/<int:room_s__roomnumber>',views.EDIT_ROOM_A,name='edit_room_allotment'),


    path('dashboard/horizontal',views.Horizontal,name='dashboard_horizontal'),
    path('',views.Login,name=''),
    path('other_pages/signup',views.SIGNUP,name='other_pages_signup'),
    path('logout',views.Logout,name='logout'),
    path('dashboard/index',views.homepage,name='dashboard_index'),
    path('dashboard/api/data/',views.GraphData.as_view()),
    path('dashboard/line/data/',views.GraphDataLine.as_view()),
    path('dashboard/help',views.Help, name='help_page'),
    path('dashboard/setting',views.Setting_page, name='setting_page'),
    path('other_pages/faq',views.faq, name='faq_page'),
    path('other_pages/404',views.handler404, name='404_page'),


    path('pdf',views.P_Venue_Pdf,name='pdf'),
    path('d_pdf',views.D_Venue_Pdf,name='d_pdf'),
    path('a_pdf',views.A_Venue_Pdf,name='a_pdf'),
    path('r_pdf',views.R_Venue_Pdf,name='r_pdf'),
    path('pp_pdf',views.PP_Venue_Pdf,name='pp_pdf'),


    path('p_csv',views.P_Venue_csv,name='p_csv'),
    path('d_csv',views.D_Venue_csv,name='d_csv'),
    path('a_csv',views.A_Venue_csv,name='a_csv'),
    path('r_csv',views.R_Venue_csv,name='r_csv'),
    path('pp_csv',views.PP_Venue_csv,name='pp_csv'),


    path('p_excel',views.P_Excel,name='p_excel'),
    path('d_excel',views.D_Excel,name='d_excel'),
    path('a_excel',views.A_Excel,name='a_excel'),
    path('r_excel',views.R_Excel,name='r_excel'),
    path('pp_excel',views.PP_Excel,name='pp_excel'),
    
    
    

    path('p_delete/<int:patient_id>',views.p_delete,name='p_delete'),
    path('d_delete/<int:doctor_id>',views.d_delete,name='d_delete'),
    path('a_delete/<int:appointment_id>',views.a_delete,name='a_delete'),
    path('r_delete/<int:room_s__roomnumber>',views.r_delete,name='r_delete'),
    
    
    path('upcoming_appointment',views.upcoming_appointments,name='upcoming_appointment'),

    path('room/add',views.ADD_ROOM,name='add_room'),
    path('room/all',views.ALL_ROOM,name='all_room'),
    path('room/avalible',views.available_rooms,name='avalible_room'),
    path('room/allocated',views.allocated_rooms,name='allocated_room'),
    path('room/bookroom',views.BookRoom,name='book_room'),
    
    


]
