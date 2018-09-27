from django.test import TestCase

from django.db import models

import json
import requests

import inspect
from typing import Dict

from urllib.parse import urlencode

from .models import Pdf


class PdfTest(TestCase):

    def setUp(self):
        #self.pdf_item = Pdf.objects.get(pk=1) #get_object_or_404(Pdf, pk=1)

        self.data="""<?xml version="1.0"?>
<root>
  <ОтступЗаголовка значение="2" />
  <ФиоГлавыОмс значение="Иванов И.И." />
  <ПриказМзио номер="123" дата="01.02.2018" название="о порядке проведения" />
  <ГодПроведения значение="2019" />
  <Сегменты>
    <Сегмент значение="особо охраняемых территорий и объектов" />
    <Сегмент значение="промышленности, энергетики, транспорта, связи" />
  </Сегменты>
  <КонтактныйТелефон значение="2323232" />
  <ПодписывающееЛицо должность="Руководитель" фио="Петров П.П." />
  <Исполнитель значение="Сидоров С.С." />
  
  <ПредоставленныеСведения>
    <Сведения кадастрНомер="02:01:010125:22" адресКладр="Башкортостан, Абзелиловский р-н, Аскаровский c/c, с Аскарово, ул Салавата Юлаева, д 48" вриПоКлассификатору ="Для размещения промышленных объектов" вриПоДокументу="Размещение производственной базы"
              наличиеОксНаЗу="застроенный" центрЭлектр="в наличии" центрГаз="в наличии" центрВод="в наличии" центрТепл="в наличии" центрКанал="в наличии"/>
    <Сведения кадастрНомер="02:01:010125:22" адресКладр="Башкортостан, Абзелиловский р-н, Аскаровский c/c, с Аскарово, ул Салавата Юлаева, д 48" вриПоКлассификатору ="Для размещения промышленных объектов" вриПоДокументу="Размещение производственной базы"
              наличиеОксНаЗу="пустой" центрЭлектр="имеется возможность подключения согласно техусловиям" центрГаз="в наличии" центрВод="в наличии" центрТепл="имеется возможность подключения согласно техусловиям" центрКанал="в наличии"/>
    <Сведения кадастрНомер="02:01:010125:22" адресКладр="Башкортостан, Абзелиловский р-н, Аскаровский c/c, с Аскарово, ул Салавата Юлаева, д 48" вриПоКлассификатору ="Для размещения промышленных объектов" вриПоДокументу="Размещение производственной базы"
              наличиеОксНаЗу="застроенный" центрЭлектр="в наличии" центрГаз="нет возможности подключения" центрВод="в наличии" центрТепл="в наличии" центрКанал="нет возможности подключения"/>
  </ПредоставленныеСведения>
</root>"""


        self.pdf_item = Pdf.objects.create(
            template_name='Приложение1 инженерИнфр',
            service_url = 'http://localhost:2448/generatereport',
            data=self.data,
        )

    def test_get_pdf_file(self):

        resp = self.pdf_item.get_pdf_file()

        print(resp.status_code)
        #print(resp.__dict__)

        self.printOjbect(resp, "    ")


    def printOjbect(self, obj, indent):
        if obj is None:
            return

        for prop in obj.__dict__:
            print(indent + prop)
            value = obj.__dict__[prop]

            if prop != "_content":
                print("{0}{1}".format(indent, value))

            if hasattr(value, '__dict__'):
                self.printOjbect(value, indent + indent)
            print(indent + "-----------------------")

        

    #     with open("test.pdf", 'wb') as fd:
    #         for chunk in resp.iter_content(chunk_size=128):
    #             fd.write(chunk)
        
    # def test_request_post(self):

    #     headers = {
    #         'content-type': 'application/xml',
    #     }

    #     params = {
    #         'templateName': 'Приложение1 инженерИнфр',
    #         'fileFormat': 'pdf',
    #         'reportName': 'test_report2.pdf',
    #     }

    #     params = urlencode(sorted(params.items()))

    #     end_point_url = '{baseUrl}?{params}'.format(baseUrl='http://localhost:2448/generatereport', params=params)

    #     body = self.data.encode('utf-8')
    
    #     print(body)
    #     print(end_point_url)

    #     resp = requests.post(url=end_point_url, data=body, headers=headers)
    #     print(resp)

    #     print(resp.status_code)
    #     print(resp.text)
        

