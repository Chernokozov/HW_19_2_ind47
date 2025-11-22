from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Fill database with sample data'

    def handle(self, *args, **options):
        # Очистка старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Starting to fill database...')

        # Создание категорий
        categories_data = [
            {'name': 'Электроника', 'description': 'Электронные устройства'},
            {'name': 'Книги', 'description': 'Книжная продукция'},
            {'name': 'Одежда', 'description': 'Одежда и аксессуары'},
            {'name': 'Мебель', 'description': 'Мебель для дома и офиса'},
            {'name': 'Спорт', 'description': 'Спортивные товары'},
        ]

        categories = []
        for i, cat_data in enumerate(categories_data):
            category = Category.objects.create(**cat_data)
            categories.append(category)
            self.stdout.write(f'{i + 1}. Created category: {category.name}')

        self.stdout.write(f'Total categories created: {len(categories)}')

        # Создание продуктов - теперь безопасно обращаемся к индексам
        products_data = [
            {'name': 'Смартфон iPhone', 'description': 'Современный смартфон', 'category': categories[0],
             'price': 79999.99},
            {'name': 'Ноутбук Gaming', 'description': 'Игровой ноутбук', 'category': categories[0], 'price': 125999.99},
            {'name': 'Наушники Wireless', 'description': 'Беспроводные наушники', 'category': categories[0],
             'price': 8999.99},
            {'name': 'Программирование на Python', 'description': 'Учебник по Python', 'category': categories[1],
             'price': 2500.00},
            {'name': 'Война и мир', 'description': 'Роман Л.Н. Толстого', 'category': categories[1], 'price': 1200.00},
            {'name': 'Футболка хлопковая', 'description': 'Хлопковая футболка', 'category': categories[2],
             'price': 1999.99},
            {'name': 'Джинсы классические', 'description': 'Классические джинсы', 'category': categories[2],
             'price': 3999.99},
            {'name': 'Офисное кресло', 'description': 'Эргономичное кресло', 'category': categories[3],
             'price': 15999.99},
            {'name': 'Футбольный мяч', 'description': 'Профессиональный мяч', 'category': categories[4],
             'price': 2999.99},
            {'name': 'Беговая дорожка', 'description': 'Электрическая беговая дорожка', 'category': categories[4],
             'price': 45999.99},
        ]

        for i, prod_data in enumerate(products_data):
            product = Product.objects.create(**prod_data)
            self.stdout.write(f'{i + 1}. Created product: {product.name} - {product.price} руб.')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully filled database! '
                f'Created {Category.objects.count()} categories and {Product.objects.count()} products.'
            )
        )