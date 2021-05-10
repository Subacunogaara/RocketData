from django.db import models



class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    position = models.ForeignKey('PositionModel', on_delete=models.PROTECT, verbose_name='Должность')
    date_of_receipt = models.DateField(verbose_name='Дата приёма на работу')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Заработная плата')
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Всего выплачено')
    chief = models.ForeignKey('EmployeeModel', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    def __str__(self):
        return self.last_name


class PositionModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.title