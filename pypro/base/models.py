from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# biblioteca para tradução do inglês para lingua definida no settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):  # extra_fields é um dicionário
        """
        Criar e salvar um usuário com um dado email e senha
        """
        if not email:  # se email não estiver definido
            raise ValueError('o email passado deve ser definido')  # lança esse erro
        # normalize_email normaliza o email colocando as letras do dominio do email
        # em minúsculo e removendo espaçoes em branco atŕas e na frente da string
        # passada
        email=self.normalize_email(email)
        user=self.model(email = email, **extra_fields)  # cria o modelo user
        user.set_password(password)  # define uma senha
        user.save(using = self._db)  # salva no banco de dados
        return user


    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)  # não criara superusuarios por padrão
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)  # cria superusuario
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    App base User class

    Email e senha são requeridos. Outros campos são opcionais
    """

    first_name=models.CharField(_('first name'), max_length = 30, blank = True)
    email=models.EmailField(_('email address'), unique = True)  # unique é para o email só tenha um usuario
    is_staff=models.BooleanField(  # is staff define os usuarios que podem acessar
        _('staff status'),          # o admin do django
        default = False,
        help_text = _('Designates whether the user can log into this admin site.'),
    )
    is_active=models.BooleanField(  # is_active define o usuário que pode se logar
        _('active'),                 # dentro do sistema
        default = True,
        help_text = _(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined=models.DateTimeField(_('date joined'), default = timezone.now)
    # date_joined define quando um usuário entrou no sistema

    objects=UserManager()

    EMAIL_FIELD='email'  # nome do campo respectivo ao email
    USERNAME_FIELD='email'  # nome qual campo será utilizado como username
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name=_('user')
        verbose_name_plural=_('users')

    def clean(self):
        super().clean()
        self.email=self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returna o first_name.
        """
        full_name='%s' % (self.first_name)
        return full_name.strip()

    def get_short_name(self):
        """Return o nome abreviado do usuário."""
        return self.first_name

    def email_user(self, subject, message, from_email = None, **kwargs):
        """Envia um email para o usuário."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
