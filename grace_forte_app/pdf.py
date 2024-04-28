from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf


def html2pdf(template_source, contect_dict={}):
    template = get_template(template_source)
    html = template.render(contect_dict)
    results = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), results)