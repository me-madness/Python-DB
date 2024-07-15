from typing import Any
from django.core.exceptions import ValidationError


def range_value_validator(value: int):
    if not 0 <= value <= 10:
        raise ValidationError("The rating must be between 0.0 and 10.0")
    
    
class RangeValueValidator:
    def __init__(self, min_value: int, max_value: int, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        if not value:
            self.__message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}" 
        else:    
            self.__message = value
        
    def __call__(self,value: int):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)
        
    def deconstruct(self):
        return (
            'main_app.validators.RangeValueValidator',
            [self.min_value, self.max_value],
            {'message': self.message}
        )    
            