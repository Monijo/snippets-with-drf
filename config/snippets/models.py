from django.db import models
from django.utils.translation import gettext_lazy as _
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.title
