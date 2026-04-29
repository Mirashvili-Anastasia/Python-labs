"Пакет с лабораторными работами №4-6"

# Импорты из lab4
from .lab4.nomber1 import intersect
from .lab4.nomber2 import root
from .lab4.nomber11 import intersect_recursive
from .lab4.nomber21 import root_iterative
# Импорты из lab5
from .lab5.fibonacci import fibonacci_closure
from .lab5.decorator import cache_decorator

# Импорты из lab6
from .lab6.gen import PasswordGenerator

# Список того, что будет доступно
__all__ = [
    'intersect',
    'root',
    'intersect_recursive',
    'root_iterative',
    'fibonacci_closure',
    'cache_decorator',
    'PasswordGenerator'
]