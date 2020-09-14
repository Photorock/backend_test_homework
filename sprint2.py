# -*- coding: utf-8 -*- 
import datetime as dt
 
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        
    def add_record(self,rec):
        self.records.append(rec)
 
    def get_today_stats(self):
        i=0
        for val in self.records:
            if val.date == dt.date.today():
                i = i + val.amount
        return i
    def get_week_stats(self):
        k = 0
        today = dt.date.today()
        for val in self.records:
            if today - dt.timedelta(days = 6) <= val.date<=today:
                k = k + val.amount
        return k
    
 
class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    def get_today_cash_remained(self,val):
        if val == 'usd':
            val = 'USD'
            balance = round((self.limit - self.get_today_stats()) / self.USD_RATE, 2)
        elif val == 'eur':
            val = 'Euro'
            balance = round((self.limit - self.get_today_stats()) / self.EURO_RATE,2)
        else:
            val = 'руб'
            balance = (self.limit - self.get_today_stats())
 
        if self.get_today_stats()<self.limit:
            answer = ('На сегодня осталось ' + str(balance) + ' ' + val)
        elif self.get_today_stats() == self.limit:
            answer = 'Денег нет, держись'
        else:
            if balance<0:
                balance = balance * (-1)
            answer = ('Денег нет, держись: твой долг - ' + str(balance) + ' ' + val)
        return answer
 
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() <= self.limit:
            l = self.limit - self.get_today_stats()
            answer=('Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' + str(l) + ' кКал')
        else:
            answer = 'Хватит есть!'
        return answer
 
 
 
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе")) 
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("eur"))