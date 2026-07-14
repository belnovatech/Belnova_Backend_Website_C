from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.core.config import SENDGRID_API_KEY, EMAIL


def send_contact_email(data):

    sg = SendGridAPIClient(SENDGRID_API_KEY)

    # ==========================
    # Admin Email
    # ==========================

    admin_html = f"""
    <h2>New Contact Form Submission</h2>

    <p><b>Name:</b> {data.name}</p>
    <p><b>Email:</b> {data.email}</p>
    <p><b>Phone:</b> {data.phone}</p>
    <p><b>Subject:</b> {data.subject}</p>
    <p><b>Message:</b></p>

    <p>{data.message}</p>
    """

    admin_mail = Mail(
        from_email=EMAIL,
        to_emails=EMAIL,
        subject=f"New Website Enquiry - {data.subject}",
        html_content=admin_html
    )

    sg.send(admin_mail)

    # ==========================
    # Customer Auto Reply
    # ==========================

    customer_html = f"""
    <html>

    <body
    style="font-family:Arial;
    background:#f5f7fb;
    padding:30px;">

    <h2>Hello {data.name},</h2>

    <p>

    Thank you for contacting
    <b>Belnova Technologies.</b>

    </p>

    <p>

    We have received your enquiry.

    </p>

    <p>

    Our team will contact you within
    <b>24 hours.</b>

    </p>

    <hr>

    <b>Your Subject:</b>

    {data.subject}

    <br><br>

    <b>Your Message:</b>

    <br>

    {data.message}

    <br><br>

    📞 +91 7382405380

    <br>

    📧 info@belnovatech.com

    </body>

    </html>
    """

    reply_mail = Mail(
        from_email=EMAIL,
        to_emails=data.email,
        subject="Thank You for Contacting Belnova Technologies",
        html_content=customer_html
    )

    sg.send(reply_mail)
