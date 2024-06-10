import os
os.environ["DJANGO_SETTINGS_MODULE"] = "it_profi.settings"
import django
django.setup()
import pytest
from main.forms import OrderForm, ProblemForm, ArticleForm


@pytest.mark.parametrize(
    'name, text, source, validity',
    [   # рабочий вариант
        ('Тестовая статья', 'Тестовый текст статьи', 'Тестовый источник', True),
        # превышена длина имени
        ('Статья тест'*10, 'Тестовый текст статьи', 'Тестовый источник', False),
        # превышена длина источника
        ('Тестовая статья', 'Тестовый текст статьи', 'Тестовый источник'*5, False),
    ]
)
def test_valid_article_form(name, text, source, validity):
    form = ArticleForm(data={
        'name': name,
        'text': text,
        'source': source
    })

    f = form.errors.as_data()
    print(f)

    assert form.is_valid() is validity
