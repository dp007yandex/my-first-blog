from django.db import models

import requests

from urllib.parse import urlencode
from django.utils import timezone

class Pdf(models.Model):
    class Meta:
        verbose_name = "Данные для получения PDF файла"
        verbose_name_plural = "Реестр pdf файлов"

    service_url = models.CharField("Url сервиса получения pdf файла", max_length=200, default='http://localhost:2448/generatereport')

    template_name = models.CharField("Имя шаблона", max_length=200)
    file_format = models.CharField("Формат файла", max_length=10, default='pdf')
    report_name = models.CharField("Наименование отчёта", max_length=200, default='report')

    data = models.TextField("Данные для отчёта в формате XML")

    #rawData = models.FileField("Pdf файл", null=True, blank=True)
    rawData = models.TextField("Pdf файл", null=True, blank=True)

    def get_pdf_file(self):
        headers = {
            'content-type': 'application/xml',
        }

        params = {
             'templateName': self.template_name,
             'fileFormat': self.file_format,
             'reportName': self.report_name,
        }

        params = urlencode(sorted(params.items()))

        end_point_url = '{baseUrl}?{params}'.format(baseUrl=self.service_url, params=params)

        resp = requests.post(url=end_point_url, data=self.data.encode('utf-8'), headers=headers)

        

        return resp

# #http://docs.python-requests.org/en/latest/user/advanced/#request-and-response-objects

#         s = Session()
#         req = Request('POST', endPointUrl, data=data, headers=headers)

#         prepped = req.prepare()
#         prepped.body = self.data
#         prepped.headers['Content-Type'] = 'application/xml'

#         resp = s.send(prepped,
#             stream=stream,
#             verify=verify,
#             proxies=proxies,
#             cert=cert,
#             timeout=timeout
#         )

#         print(resp.status_code)

#         if resp.status_code == requests.codes.ok:
#             print(resp.body)

#         return resp
