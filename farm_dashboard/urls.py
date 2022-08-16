
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^index$', views.index, name='index'),

    re_path(r'^Reg$', views.Reg, name='Reg'),
    re_path(r'^registration$', views.registration, name='registration'),

    re_path(r'^$', views.log, name='log'),

    #------------------------ADMIN----------------------------
    re_path(r'^Admin_index$', views.Admin_index,
        name='Admin_index'),
    re_path(r'^Admin_Settings$', views.Admin_Settings,
        name='Admin_Settings'),
    re_path(r'^Admin_Dashboard$', views.Admin_Dashboard,
        name='Admin_Dashboard'),
    re_path(r'^Admin_clients$', views.Admin_clients,
        name='Admin_clients'),
    re_path(r'^Admin_clientdashboard/(?P<id>\d+)$', views.Admin_clientdashboard,
        name='Admin_clientdashboard'),
    re_path(r'^Admin_client_chart/(?P<id>\d+)$', views.Admin_client_chart,
        name='Admin_client_chart'),
    re_path(r'^Admin_staffs$', views.Admin_staffs,
        name='Admin_staffs'),
    re_path(r'^Admin_staffdashboard/(?P<id>\d+)$', views.Admin_staffdashboard,
        name='Admin_staffdashboard'),
    re_path(r'^Admin_Staff_chart/(?P<id>\d+)$', views.Admin_Staff_chart,
        name='Admin_Staff_chart'),
    re_path(r'^Admin_registration_details$', views.Admin_registration_details,
        name='Admin_registration_details'),
    re_path(r'^registersave/(?P<id>\d+)$', views.registersave,
        name='registersave'),
    re_path(r'^Admin_plant_details$', views.Admin_plant_details,
        name='Admin_plant_details'),
    re_path(r'^Admin_farm_weather$', views.Admin_farm_weather,
        name='Admin_farm_weather'),
    re_path(r'^Admin_find_weather$', views.Admin_find_weather,
        name='Admin_find_weather'),
    re_path(r'^Admin_weather$', views.Admin_weather,
        name='Admin_weather'),
    re_path(r'^Admin_soil_sample_test$', views.Admin_soil_sample_test,
        name='Admin_soil_sample_test'),
    re_path(r'^Admin_fertilizer_applications$', views.Admin_fertilizer_applications,
        name='Admin_fertilizer_applications'),
    re_path(r'^Admin_periodic_tests$', views.Admin_periodic_tests,
        name='Admin_periodic_tests'),
    re_path(r'^Admin_farm_machineries$', views.Admin_farm_machineries,
        name='Admin_farm_machineries'),
    re_path(r'^Admin_man_power_usage$', views.Admin_man_power_usage,
        name='Admin_man_power_usage'),
    re_path(r'^Admin_farm_expenses$', views.Admin_farm_expenses,
        name='Admin_farm_expenses'),
    re_path(r'^Admin_find_expense$', views.Admin_find_expense,
        name='Admin_find_expense'),
    re_path(r'^Admin_expense$', views.Admin_expense,
        name='Admin_expense'),
    re_path(r'^Admin_farm_revenue$', views.Admin_farm_revenue,
        name='Admin_farm_revenue'),
    re_path(r'^Admin_find_revenue$', views.Admin_find_revenue,
        name='Admin_find_revenue'),
    re_path(r'^Admin_revenue$', views.Admin_revenue,
        name='Admin_revenue'),
    re_path(r'^logout_admin$', views.logout_admin,
        name='logout_admin'),

    #------------------------USER----------------------------

    re_path(r'^user_index$', views.user_index,
        name='user_index'),
    re_path(r'^user_dashboard$', views.user_dashboard,
        name='user_dashboard'),
    re_path(r'^user_chart$', views.user_chart,
        name='user_chart'),
    re_path(r'^user_settings$', views.user_settings,
        name='user_settings'),
    re_path(r'^user_Profile_Imagechange/(?P<id>\d+)$', views.user_Profile_Imagechange,
        name='user_Profile_Imagechange'),
    re_path(r'^user_change_password/(?P<id>\d+)$', views.user_change_password,
        name='user_change_password'),
    re_path(r'^user_plant_details$', views.user_plant_details,
        name='user_plant_details'),
    re_path(r'^user_add_plant_details$', views.user_add_plant_details,
        name='user_add_plant_details'),
    re_path(r'^user_viewedit_plantdetails/(?P<id>\d+)$', views.user_viewedit_plantdetails,
        name='user_viewedit_plantdetails'),
    re_path(r'^user_plantdetails_update/(?P<id>\d+)$', views.user_plantdetails_update,
        name='user_plantdetails_update'),
    re_path(r'^user_farm_weather$', views.user_farm_weather,
        name='user_farm_weather'),
    re_path(r'^user_weather_print$', views.user_weather_print,
        name='user_weather_print'),
    re_path(r'^user_add_farm_weather$', views.user_add_farm_weather,
        name='user_add_farm_weather'),
    re_path(r'^user_viewedit_farmweather/(?P<id>\d+)$', views.user_viewedit_farmweather,
        name='user_viewedit_farmweather'),
    re_path(r'^user_farmweather_update/(?P<id>\d+)$', views.user_farmweather_update,
        name='user_farmweather_update'),
    re_path(r'^user_find_weather$', views.user_find_weather,
        name='user_find_weather'),
    re_path(r'^user_weather$', views.user_weather,
        name='user_weather'),
    re_path(r'^user_soil_sample_test$', views.user_soil_sample_test,
        name='user_soil_sample_test'),
    re_path(r'^user_add_soil_sample_test$', views.user_add_soil_sample_test,
        name='user_add_soil_sample_test'),
    re_path(r'^user_viewedit_soilsampletest/(?P<id>\d+)$', views.user_viewedit_soilsampletest,
        name='user_viewedit_soilsampletest'),
    re_path(r'^user_soilsampletest_update/(?P<id>\d+)$', views.user_soilsampletest_update,
        name='user_soilsampletest_update'),
    re_path(r'^user_fertilizer_applications$', views.user_fertilizer_applications,
        name='user_fertilizer_applications'),
    re_path(r'^user_fertilizer$', views.user_fertilizer,
        name='user_fertilizer'),
    re_path(r'^user_fertilizer_list$', views.user_fertilizer_list,
        name='user_fertilizer_list'),
    re_path(r'^user_add_fertilizer_applications$', views.user_add_fertilizer_applications,
        name='user_add_fertilizer_applications'),
    re_path(r'^user_viewedit_fertilizer/(?P<id>\d+)$', views.user_viewedit_fertilizer,
        name='user_viewedit_fertilizer'),
    re_path(r'^user_fertilizer_update/(?P<id>\d+)$', views.user_fertilizer_update,
        name='user_fertilizer_update'),
    re_path(r'^user_periodic_tests$', views.user_periodic_tests,
        name='user_periodic_tests'),
    re_path(r'^user_add_periodic_tests$', views.user_add_periodic_tests,
        name='user_add_periodic_tests'),
    re_path(r'^user_viewedit_periodictest/(?P<id>\d+)$', views.user_viewedit_periodictest,
        name='user_viewedit_periodictest'),
    re_path(r'^user_periodictest_update/(?P<id>\d+)$', views.user_periodictest_update,
        name='user_periodictest_update'),
    re_path(r'^user_farm_machineries$', views.user_farm_machineries,
        name='user_farm_machineries'),
    re_path(r'^user_add_farm_machineries$', views.user_add_farm_machineries,
        name='user_add_farm_machineries'),
    re_path(r'^user_viewedit_farmmachineries/(?P<id>\d+)$', views.user_viewedit_farmmachineries,
        name='user_viewedit_farmmachineries'),
    re_path(r'^user_farmmachineries_update/(?P<id>\d+)$', views.user_farmmachineries_update,
        name='user_farmmachineries_update'),
    re_path(r'^user_man_power_usage$', views.user_man_power_usage,
        name='user_man_power_usage'),
    re_path(r'^user_add_man_power_usage$', views.user_add_man_power_usage,
        name='user_add_man_power_usage'),
    re_path(r'^user_viewedit_manpower/(?P<id>\d+)$', views.user_viewedit_manpower,
        name='user_viewedit_manpower'),
    re_path(r'^user_manpower_update/(?P<id>\d+)$', views.user_manpower_update,
        name='user_manpower_update'),
    re_path(r'^user_farm_expenses$', views.user_farm_expenses,
        name='user_farm_expenses'),
    re_path(r'^user_add_farm_expenses$', views.user_add_farm_expenses,
        name='user_add_farm_expenses'),
    re_path(r'^user_viewedit_farmexpenses/(?P<id>\d+)$', views.user_viewedit_farmexpenses,
        name='user_viewedit_farmexpenses'),
    re_path(r'^user_farmexpense_update/(?P<id>\d+)$', views.user_farmexpense_update,
        name='user_farmexpense_update'),
    re_path(r'^user_find_expense$', views.user_find_expense,
        name='user_find_expense'),
    re_path(r'^user_expense$', views.user_expense,
        name='user_expense'),
    re_path(r'^user_farm_revenue$', views.user_farm_revenue,
        name='user_farm_revenue'),
    re_path(r'^user_add_farm_revenue$', views.user_add_farm_revenue,
        name='user_add_farm_revenue'),
    re_path(r'^user_viewedit_farmrevenue/(?P<id>\d+)$', views.user_viewedit_farmrevenue,
        name='user_viewedit_farmrevenue'),
    re_path(r'^user_farmrevenue_update/(?P<id>\d+)$', views.user_farmrevenue_update,
        name='user_farmrevenue_update'),
    re_path(r'^user_find_revenue$', views.user_find_revenue,
        name='user_find_revenue'),
    re_path(r'^user_revenue$', views.user_revenue,
        name='user_revenue'),
    re_path(r'^logout_user$', views.logout_user,
        name='logout_user'),

    #------------------------STAFF----------------------------

    re_path(r'^Staff_index$', views.Staff_index,
        name='Staff_index'),
    re_path(r'^Staff_clients$', views.Staff_clients,
        name='Staff_clients'),
    re_path(r'^Staff_clientdashboard/(?P<id>\d+)$', views.Staff_clientdashboard,
        name='Staff_clientdashboard'),
    re_path(r'^Staff_client_chart/(?P<id>\d+)$', views.Staff_client_chart,
        name='Staff_client_chart'),
    re_path(r'^Staff_dashboard$', views.Staff_dashboard,
        name='Staff_dashboard'),
    re_path(r'^Staff_chart$', views.Staff_chart,
        name='Staff_chart'),
    re_path(r'^Staff_settings$', views.Staff_settings,
        name='Staff_settings'),
    re_path(r'^Staff_Profile_Imagechange/(?P<id>\d+)$', views.Staff_Profile_Imagechange,
        name='Staff_Profile_Imagechange'),
    re_path(r'^Staff_change_password/(?P<id>\d+)$', views.Staff_change_password,
        name='Staff_change_password'),
    re_path(r'^Staff_plant_details$', views.Staff_plant_details,
        name='Staff_plant_details'),
    re_path(r'^Staff_add_plant_details$', views.Staff_add_plant_details,
        name='Staff_add_plant_details'),
    re_path(r'^Staff_viewedit_plantdetails/(?P<id>\d+)$', views.Staff_viewedit_plantdetails,
        name='Staff_viewedit_plantdetails'),
    re_path(r'^Staff_plantdetails_update/(?P<id>\d+)$', views.Staff_plantdetails_update,
        name='Staff_plantdetails_update'),
    re_path(r'^Staff_farm_weather$', views.Staff_farm_weather,
        name='Staff_farm_weather'),
    re_path(r'^Staff_add_farm_weather$', views.Staff_add_farm_weather,
        name='Staff_add_farm_weather'),
    re_path(r'^Staff_viewedit_farmweather/(?P<id>\d+)$', views.Staff_viewedit_farmweather,
        name='Staff_viewedit_farmweather'),
    re_path(r'^Staff_farmweather_update/(?P<id>\d+)$', views.Staff_farmweather_update,
        name='Staff_farmweather_update'),
    re_path(r'^Staff_find_weather$', views.Staff_find_weather,
        name='Staff_find_weather'),
    re_path(r'^Staff_weather$', views.Staff_weather,
        name='Staff_weather'),
    re_path(r'^Staff_soil_sample_test$', views.Staff_soil_sample_test,
        name='Staff_soil_sample_test'),
    re_path(r'^Staff_add_soil_sample_test$', views.Staff_add_soil_sample_test,
        name='Staff_add_soil_sample_test'),
    re_path(r'^Staff_viewedit_soilsampletest/(?P<id>\d+)$', views.Staff_viewedit_soilsampletest,
        name='Staff_viewedit_soilsampletest'),
    re_path(r'^Staff_soilsampletest_update/(?P<id>\d+)$', views.Staff_soilsampletest_update,
        name='Staff_soilsampletest_update'),
    re_path(r'^Staff_fertilizer_applications$', views.Staff_fertilizer_applications,
        name='Staff_fertilizer_applications'),
    re_path(r'^Staff_fertilizer$', views.Staff_fertilizer,
        name='Staff_fertilizer'),
    re_path(r'^Staff_fertilizer_list$', views.Staff_fertilizer_list,
        name='Staff_fertilizer_list'),
    re_path(r'^Staff_add_fertilizer_applications$', views.Staff_add_fertilizer_applications,
        name='Staff_add_fertilizer_applications'),
    re_path(r'^Staff_viewedit_fertilizer/(?P<id>\d+)$', views.Staff_viewedit_fertilizer,
        name='Staff_viewedit_fertilizer'),
    re_path(r'^Staff_fertilizer_update/(?P<id>\d+)$', views.Staff_fertilizer_update,
        name='Staff_fertilizer_update'),
    re_path(r'^Staff_periodic_tests$', views.Staff_periodic_tests,
        name='Staff_periodic_tests'),
    re_path(r'^Staff_add_periodic_tests$', views.Staff_add_periodic_tests,
        name='Staff_add_periodic_tests'),
    re_path(r'^Staff_viewedit_periodictest/(?P<id>\d+)$', views.Staff_viewedit_periodictest,
        name='Staff_viewedit_periodictest'),
    re_path(r'^Staff_periodictest_update/(?P<id>\d+)$', views.Staff_periodictest_update,
        name='Staff_periodictest_update'),
    re_path(r'^Staff_farm_machineries$', views.Staff_farm_machineries,
        name='Staff_farm_machineries'),
    re_path(r'^Staff_add_farm_machineries$', views.Staff_add_farm_machineries,
        name='Staff_add_farm_machineries'),
    re_path(r'^Staff_viewedit_farmmachineries/(?P<id>\d+)$', views.Staff_viewedit_farmmachineries,
        name='Staff_viewedit_farmmachineries'),
    re_path(r'^Staff_farmmachineries_update/(?P<id>\d+)$', views.Staff_farmmachineries_update,
        name='Staff_farmmachineries_update'),
    re_path(r'^Staff_man_power_usage$', views.Staff_man_power_usage,
        name='Staff_man_power_usage'),
    re_path(r'^Staff_add_man_power_usage$', views.Staff_add_man_power_usage,
        name='Staff_add_man_power_usage'),
    re_path(r'^Staff_viewedit_manpower/(?P<id>\d+)$', views.Staff_viewedit_manpower,
        name='Staff_viewedit_manpower'),
    re_path(r'^Staff_manpower_update/(?P<id>\d+)$', views.Staff_manpower_update,
        name='Staff_manpower_update'),
    re_path(r'^Staff_farm_expenses$', views.Staff_farm_expenses,
        name='Staff_farm_expenses'),
    re_path(r'^Staff_add_farm_expenses$', views.Staff_add_farm_expenses,
        name='Staff_add_farm_expenses'),
    re_path(r'^Staff_viewedit_farmexpenses/(?P<id>\d+)$', views.Staff_viewedit_farmexpenses,
        name='Staff_viewedit_farmexpenses'),
    re_path(r'^Staff_farmexpense_update/(?P<id>\d+)$', views.Staff_farmexpense_update,
        name='Staff_farmexpense_update'),
    re_path(r'^Staff_find_expense$', views.Staff_find_expense,
        name='Staff_find_expense'),
    re_path(r'^Staff_expense$', views.Staff_expense,
        name='Staff_expense'),
    re_path(r'^Staff_farm_revenue$', views.Staff_farm_revenue,
        name='Staff_farm_revenue'),
    re_path(r'^Staff_add_farm_revenue$', views.Staff_add_farm_revenue,
        name='Staff_add_farm_revenue'),
    re_path(r'^Staff_viewedit_farmrevenue/(?P<id>\d+)$', views.Staff_viewedit_farmrevenue,
        name='Staff_viewedit_farmrevenue'),
    re_path(r'^Staff_farmrevenue_update/(?P<id>\d+)$', views.Staff_farmrevenue_update,
        name='Staff_farmrevenue_update'),
    re_path(r'^Staff_find_revenue$', views.Staff_find_revenue,
        name='Staff_find_revenue'),
    re_path(r'^Staff_revenue$', views.Staff_revenue,
        name='Staff_revenue'),
    re_path(r'^logout_staff$', views.logout_staff,
        name='logout_staff'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)