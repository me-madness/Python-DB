from django.core.exceptions import ValidationError

class OnlyDigitsValidator:
    def __init__(self, message="Frit name should contain only digits!"):
        self.message = message
        
        
    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError(self.message)
        
        
    def deconstruct(self):
        return (
            'validators.OnlyDigitsValidator',
            (),
            {'message': self.message}
        ) 