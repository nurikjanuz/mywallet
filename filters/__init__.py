from loader import dp
from .admin import IsAdmin, IsAlpha, IsDigit

if __name__== "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsAlpha)
    dp.filters_factory.bind(IsDigit)

