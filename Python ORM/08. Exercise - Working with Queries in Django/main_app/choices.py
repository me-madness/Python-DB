from django.db import models


class LaptopBrandChoice(models.TextChoices):
    # from django.db import models
    # "Asus", "Acer", "Apple", "Lenovo", and "Dell"
    ASUS = "ASUS", "ASUS"
    ACER = "ACER", "ACER"
    APPLE = "APPLE", "APPLE"
    LENOVO = "LENOVO", "LENOVO"
    DELL = "DELL", "DELL"
    
    
class OperationSystemChoice(models.TextChoices):
    WINDOWS = "WINDOWS", "WINDOWS"    
    MACOS = "MACOS", "MACOS"    
    LINUX = "LINUX", "LINUX"    
    CHROME_OS = "CHROME_OS", "CHROME_OS"    
       
       