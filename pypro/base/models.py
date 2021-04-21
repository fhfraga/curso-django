from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# biblioteca para tradução do inglês para lingua definida no settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail


class User(AbstractBaseUser, PermissionsMixin):
    """
    App base User class

    Email e senha são requeridos. Outros campos são opcionais
    """

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True) # unique é para o email só tenha um usuario
    is_staff = models.BooleanField( # is staff define os usuarios que podem acessar
        _('staff status'),          # o admin do django
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField( # is_active define o usuário que pode se logar
        _('active'),                 # dentro do sistema
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # date_joined define quando um usuário entrou no sistema

    #objects = UserManager()

    EMAIL_FIELD = 'email' # nome do campo respectivo ao email
    USERNAME_FIELD = 'email' # nome qual campo será utilizado como username
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returna o first_name.
        """
        full_name = '%s' % (self.first_name)
        return full_name.strip()

    def get_short_name(self):
        """Return o nome abreviado do usuário."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Envia um email para o usuário."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
