from fastapi import APIRouter
from app.schemas.contact import ContactRequest
from app.services.email_service import send_contact_email

router = APIRouter()

@router.post("/contact")
def contact(data: ContactRequest):

    send_contact_email(data)

    return {
        "success": True,
        "message": "Mail Sent Successfully"
    }