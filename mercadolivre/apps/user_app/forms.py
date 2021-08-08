from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, PasswordInput, Form, EmailField, EmailInput, TextInput
from apps.user_app.validators import *


class SignUpForm(UserCreationForm):

    username = CharField(
        label='Nome de Usuário',
        max_length=150,
        widget=TextInput(attrs={
            'class': 'form-control',
            'id': 'usernameInput',
            'placeholder': 'Nome de usuário'
        }))
    email = EmailField(
        label='E-mail',
        max_length=255,
        widget=EmailInput(attrs={
            'class': 'form-control',
            'id': 'emailInput',
            'placeholder': 'E-mail'
        }))
    first_name = CharField(
        label='Primeiro nome',
        max_length=100,
        widget=TextInput(attrs={
            'class': 'form-control',
            'id': 'fnameInput',
            'placeholder': 'Primeiro Nome'
        }))
    last_name = CharField(
        label='Último nome',
        max_length=100,
        widget=TextInput(attrs={
            'class': 'form-control',
            'id': 'lnameInput',
            'placeholder': 'Último Nome'
        }))
    password1 = CharField(
        label=("Senha"),
        strip=False,
        widget=PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'passwd1',
            'placeholder': 'Senha'
            }),
        )
    password2 = CharField(
        label=("Confirmação de senha"),
        strip=False,
        widget=PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            'id': 'passwd1',
            'placeholder': 'Senha'

        }),
        )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     lista_erros = {'username': []}
    #     comprimento_minimo_username(username, lista_erros)
    #     verifica_username_existente(username, lista_erros)
    #     if lista_erros is not None:
    #         for erro in lista_erros:
    #             mensagem_erro = lista_erros[erro]
    #             self.add_error(erro, mensagem_erro)
    #     return self.cleaned_data

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     print(self._errors)
    #     lista_erros = {'email': []}
    #     verifica_email_existente(email, lista_erros)
    #     for erro in lista_erros:
    #         mensagem_erro = lista_erros[erro]
    #         self.add_error(erro, mensagem_erro)

    class Meta:
        model = UserModel
        fields = 'email', 'username', 'first_name', 'last_name'


class SignUpForm2(UserCreationForm):
    pass


class LoginForm(AuthenticationForm):
    username = EmailField(label='E-mail', widget=EmailInput(attrs=
                                                            {'class': 'form-control',
                                                            'placeholder': 'nome@dominio.com.br',
                                                            'id': 'emailinput'}))
    password = CharField(label='Senha', widget=PasswordInput(attrs=
                                                            {'class': 'form-control',
                                                            'placeholder': 'Senha',
                                                            'id': 'passwordinput'}))


class AlterUserForm(Form):
    nome = CharField(label='Nome')
    sobrenome = CharField(label='Sobrenome')
    email = EmailField(label='E-mail')
    senha = CharField(label='Confirme sua senha', widget=PasswordInput)
