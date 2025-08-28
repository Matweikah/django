from django.db import models
class Podsh(models.Model):
    ID = models.IntegerField(primary_key=True)
    POLN = models.CharField(max_length=255, blank=True, null=True)
    SLITN = models.CharField(max_length=255, blank=True, null=True)
    OSNOVA = models.CharField(max_length=255, blank=True, null=True)
    ANALOG = models.CharField(max_length=50, blank=True, null=True)
    FIRMA = models.CharField(max_length=20, blank=True, null=True)
    WES = models.CharField(max_length=15, blank=True, null=True)
    MIN = models.CharField(max_length=15, blank=True, null=True)
    MAX = models.CharField(max_length=15, blank=True, null=True)
    SHIR = models.CharField(max_length=15, blank=True, null=True)
    ISKIZ = models.ImageField(upload_to='', blank=True, null=True) 
    GDIN = models.CharField(max_length=10, blank=True, null=True)
    GSTAT = models.CharField(max_length=10, blank=True, null=True)
    NPLAST = models.CharField(max_length=10, blank=True, null=True)
    NGIDK = models.CharField(max_length=10, blank=True, null=True)
    KOLTK = models.CharField(max_length=10, blank=True, null=True)
    DTK = models.CharField(max_length=50, blank=True, null=True)
    IMP = models.BooleanField(blank=True, null=True)  # bit → BooleanField
    GOST = models.CharField(max_length=255, blank=True, null=True)
    STEEL = models.CharField(max_length=255, blank=True, null=True)
    SREDN = models.FloatField(blank=True, null=True)  # float → FloatField
    ZAVODS = models.CharField(max_length=255, blank=True, null=True)
        
class Meta:
        db_table = '111'
        managed = False  # ВАЖНО: Django не будет управлять таблицей

def __str__(self):
        return f"{self.ID} - {self.POLN or 'No name'}"
 # ДОБАВЛЯЕМ МЕТОДЫ ДЛЯ ЦЕН
def get_price_offers(self):
        return Price.objects.filter(bearing=str(self.ID)).order_by('cena')
    
def get_min_price(self):
        offer = self.get_price_offers().first()
        return offer.cena if offer else None
    
def get_total_quantity(self):
        result = self.get_price_offers().aggregate(Sum('kolwo'))
        return result['kolwo__sum'] or 0
class City(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name="Айди")
    city = models.CharField(max_length=100, verbose_name="Город")
    country = models.CharField(max_length=100, verbose_name="Страна")
    region = models.CharField(max_length=100, verbose_name="Регион")
    okrug = models.CharField(max_length=100, verbose_name="Округ")
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        
    
    def __str__(self):
        return f"{self.city}, {self.country}"    
    

class Price(models.Model):

    bearing = models.CharField(max_length=100, blank=True, verbose_name="Подшипник")
    kolwo = models.IntegerField( verbose_name="Количество")
    cena = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Стоимость")
    sales = models.CharField(max_length=100, blank=True, verbose_name="Поставщик")
    reserv = models.IntegerField(verbose_name="Резерв")
   
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
    
    def __str__(self):
        return f"{self.bearing} - {self.kolwo}"
 # ДОБАВЛЯЕМ МЕТОД ДЛЯ ДОСТУПНОГО КОЛИЧЕСТВА
    def get_available_quantity(self):
        return self.kolwo - self.reserv
# Create your models here.
