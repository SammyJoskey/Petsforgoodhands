from ..pets.models import Pet

def title(sex, breed):
    if sex == 'm' and breed == 'c':
        return "Кот"
    elif sex == 'f' and breed == 'c':
        return "Кошечка"