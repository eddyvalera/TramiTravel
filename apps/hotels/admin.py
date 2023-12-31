from django.contrib import admin

from apps.hotels.models import Bill, Booking, Hotel, Room, RoomType, VacationPackage, Transport,Client
    
class TransportAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Transport._meta.fields]
    search_fields = ["id","name","nameCode"]
    list_filter = ["actived",]
    model = Transport
        
class RoomTypeAdmin(admin.ModelAdmin):
    list_display=[field.name for field in RoomType._meta.fields]
    search_fields = ["id","name","actived"]
    model = RoomType
    
class HotelAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Hotel._meta.fields]
    search_fields = ["id","name","actived"]
    list_filter = ["location"]
    model = Hotel

class VacationPackageAdmin(admin.ModelAdmin):
    list_display=[field.name for field in VacationPackage._meta.fields]
    model = VacationPackage

class BillAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Bill._meta.fields]
    search_fields = ["id","code","zelle","zelle_owner"]
    list_filter = ["paid",]
    model = Bill
    
class ClientAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Client._meta.fields]
    search_fields = ["id"]
    """
    ,"firstName","middleName",
    "lastName","motherLastName",
    "birth","gender","email","phone",
    "documentNumber","documentExpiration",
    "documentType","documentCountry",
    "secondaryDocumentNumber",
    "secondaryDocumentExpiration",
    "secondaryDocumentType","secondaryDocumentCountry",
    "streetBegin","cityBegin","stateBegin",
    "streetTo","cityTo","stateTo"
    """
    model = Client

class BookingAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Booking._meta.fields]
    search_fields = ["id","reservationCode","pnr","pnr_return"]
    
    list_filter = ["user","actived"]
    date_hierarchy = "date"
    model = Booking

class RoomAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Room._meta.fields]
    model = Room
    
admin.site.register(Bill,BillAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(RoomType,RoomTypeAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(VacationPackage,VacationPackageAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Transport,TransportAdmin)