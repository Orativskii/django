from django import forms


class UserForm(forms.Form):
    Name = forms.RegexField(label="Имя", regex="[а-яА-Я]")
    Surname = forms.RegexField(regex="[а-яА-Я]", label="Фамилия")
    Date_of_Birth = forms.DateField(help_text="Формат YYYY-MM-DD", label="Дата рождения")
    Telephone = forms.RegexField(label="Номер телефона", regex="(?:\w)(?:(?:(?:(?:\+?3)?8\W{0,5})?0\W{0,5})?[34569]\s?\d[^\w,;(\+]{0,5})?\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d(?!(\W?\d))")
    Email = forms.EmailField(label="Электронная почта")
    Passport_ID = forms.RegexField(regex="^[0-9]+$", label="Номер паспорта")
    Taxpayer_code = forms.RegexField(regex="^[0-9]+$", label="Идентификационный код")

