from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import mm, inch
from django.http import HttpResponse
from io import BytesIO
from apiapp.models import *
from django.shortcuts import  get_object_or_404
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch











doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

pagesize = (140 * mm, 216 * mm)  # width, height
flowables = []
page=[]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


def add_image(img):
    im = Image(img, 2*inch, 2*inch)
    page.append(im)


def add_space():
    page.append(Spacer(1, 12))


def add_text(text, space=0):
    if type(text)==list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space==1:
            add_space()
        add_space()

    #Returning as a PDF in Django
def view_that_returns_pdf(request):  
    event = get_object_or_404(Event)
    context={'request': request}
        
    # =============================== The content =======================
    # ============================== of the document ====================
    add_text([
    ''' <u> SAMPLE RESIDENT/BUSINESS NOTIFICATION LETTER </u>
    
    
    '''.splitlines()])
    add_text(event.company_name)
    add_text(event.date)
    add_text(['Dear Neighbors/Businesses, '.splitlines()])


    add_text(["""This letter is to inform you that on {},{}  
    will be filming scenes at locations in this area from approximately {}  to  {}.{} is produced by
    {}.""".format(

       event.date,
       event.company_name,
       event.start_time,
       event.finish_time,
       event.project_name,
       event.company_name,)
    ])

    add_text([""" In order to facilitate filming, we will need to hold parking for our
    production vehicles beginning {}  {}.The streets
    affected include:  """.format(
            
            event.start_time,
            event.date_to_start,)

            ])

    add_text(["""
        {}
        """.format(
                
                event.street_address,) ])

    add_text(["""
    We are aware of the inconvenience caused by our activity and
    apologize in advance. Rest assured that we will do everything possible
    to minimize the impact of our activities on your neighborhood. If you
    have particular concerns (scheduled deliveries, construction,
    accessibility needs, etc.) that must be addressed, please call the
    Location Department at {}. We will do everything
    possible to find a mutually agreeable solution. """.format(event.phone_number,)])

    add_text(["""
    Your cooperation will help to make this location shoot a success!
    Thank you in advance for your understanding and cooperation. """])



    add_text(["""{}""".format( event.department_Location,)])
    add_text(["""{}""".format(event.phone_number,)])
    add_text(["""{}""".format( event.company_address,)])
    add_text(["""{}""".format(event.fax_number,)])

    # ===========================================================
    pdf_buffer = BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer)
    my_doc.build(flowables)
    my_doc.build(page)

     # all the other stuff
    pdf_value = pdf_buffer.getvalue()
    pdf_buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="some_file.pdf"'
    response.write(pdf_value)
    return response

   

   