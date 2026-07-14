import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import EMAIL, PASSWORD


def send_contact_email(data):

    server = smtplib.SMTP("smtpout.secureserver.net", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    # ==========================================
    # ADMIN EMAIL (To Belnova)
    # ==========================================

    admin = MIMEMultipart("alternative")

    admin["From"] = EMAIL
    admin["To"] = EMAIL
    admin["Subject"] = f" New Website Enquiry - {data.subject}"

    admin_html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:30px;background:#f5f7fb;font-family:Arial,sans-serif;">

    <table width="650" align="center"
    style="background:#ffffff;border-radius:10px;border:1px solid #e5e5e5;">

    <tr>
    <td style="background:#081b3a;padding:25px;text-align:center;">

    <h1 style="color:white;margin:0;">
     New Contact Form Submission
    </h1>

    </td>
    </tr>

    <tr>
    <td style="padding:30px;">

    <table width="100%" cellpadding="10" cellspacing="0">

    <tr>
        <td><b>Name</b></td>
        <td>{data.name}</td>
    </tr>

    <tr>
        <td><b>Email</b></td>
        <td>{data.email}</td>
    </tr>

    <tr>
        <td><b>Phone</b></td>
        <td>{data.phone}</td>
    </tr>

    <tr>
        <td><b>Subject</b></td>
        <td>{data.subject}</td>
    </tr>

    <tr>
        <td valign="top"><b>Message</b></td>
        <td>{data.message}</td>
    </tr>

    </table>

    </td>
    </tr>

    <tr>
    <td style="background:#f3f3f3;padding:18px;text-align:center;color:#666;">
    Belnova Technologies • Hyderabad
    </td>
    </tr>

    </table>

    </body>
    </html>
    """

    admin.attach(MIMEText(admin_html, "html"))

    server.sendmail(
        EMAIL,
        EMAIL,
        admin.as_string()
    )

    # ==========================================
    # CUSTOMER AUTO REPLY
    # ==========================================

    reply = MIMEMultipart("alternative")

    reply["From"] = EMAIL
    reply["To"] = data.email
    reply["Subject"] = "Thank You for Contacting Belnova Technologies"

    html = f"""
    <!DOCTYPE html>
    <html>

    <body style="margin:0;padding:30px;background:#f5f7fb;font-family:Arial,sans-serif;">

    <table width="650" align="center"
    style="background:#ffffff;border-radius:10px;border:1px solid #e5e5e5;">

    <tr>

    <td style="background:#081b3a;padding:35px;text-align:center;">

    <h1 style="color:white;margin:0;">
    Belnova Technologies
    </h1>

    <p style="color:#d7e4ff;">
    Thank you for contacting us
    </p>

    </td>

    </tr>

    <tr>

    <td style="padding:35px;">

    <h2>Hello {data.name},</h2>

    <p style="line-height:28px;color:#444;">

    Thank you for contacting
    <strong>Belnova Technologies.</strong>

    <br><br>

    We have successfully received your enquiry.

    <br><br>

    Our team will review your request and get back to you within
    <strong>24 hours.</strong>

    </p>

    <table
    width="100%"
    style="margin-top:25px;
    background:#f7f9fc;
    border-left:4px solid #081b3a;
    padding:15px;">

    <tr>
    <td>

    <strong>Your Submission</strong>

    <br><br>

    Subject:
    <strong>{data.subject}</strong>

    <br><br>

    Message:

    <br>

    {data.message}

    </td>
    </tr>

    </table>

    <p style="margin-top:30px;line-height:28px;">

    If your enquiry is urgent, please contact us directly.

    </p>

    <hr>

    <p>

    📞 +91 7382405380

    <br>

    📧 info@belnovatech.com

    <br>

    📍 Hyderabad, Telangana, India

    </p>

    </td>

    </tr>

    <tr>

    <td style="background:#081b3a;color:white;padding:20px;text-align:center;">

    © 2026 Belnova Technologies

    <br>

    Building Intelligent Digital Solutions

    </td>

    </tr>

    </table>

    </body>

    </html>
    """

    reply.attach(MIMEText(html, "html"))

    server.sendmail(
        EMAIL,
        data.email,
        reply.as_string()
    )

    server.quit()