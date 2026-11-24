import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm

logger = logging.getLogger(__name__)

def ticket_list(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            logger.info("Өтінім сақталды, ID: %s", ticket.id)
            return redirect("ticket_list")
        else:
            logger.warning("Өтінім формасы тексеруден өтпеді")
    else:
        form = TicketForm()

    tickets = Ticket.objects.all()
    return render(request, "tickets/index.html", {"form": form, "tickets": tickets})

def update_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Ticket.STATUS_CHOICES):
            ticket.status = new_status
            ticket.save()
            logger.info("Өтінім мәртебесі жаңартылды, ID: %s -> %s", ticket.id, new_status)
    return redirect("ticket_list")

def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket_id = ticket.id
        ticket.delete()
        logger.info("Өтінім жойылды, ID: %s", ticket_id)
    return redirect("ticket_list")
