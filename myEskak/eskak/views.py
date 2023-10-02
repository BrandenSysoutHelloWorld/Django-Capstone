# DEFINE IMPORTS
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry

# START OF FILE: [eskak]: 'views.py'

# LANDING VIEW
def landing_view(request):
    """Display the landing page.

    This view renders the landing page for the Eskak application.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML landing page
    :rtype: HttpResponse
    """
    return render(request, 'landing.html')


# ENTRY CREATE VIEW
def new_entry_view(request):
    """
    Display the new entry form.

    This view renders the new entry form page for the Eskak application.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML page for creating a new entry
    :rtype: HttpResponse
    """
    return render(request, 'newEntry.html')

# ENTRY CREATE FUNCTION
def new_entry_create(request):
    """
    Create a new entry in the database based on user input.

    This view handles the POST request for creating a new entry in the Eskak
    application's database. It extracts the entry details from the request and
    attempts to save the new entry. If successful, it redirects to the previous
    entries view with a success message. If there is an error, it redirects
    back to the new entry form with an error message.

    :param request: HttpRequest object containing user input
    :type request: HttpRequest

    :return: HttpResponseRedirect to previous_entry_view with success or error message
    :rtype: HttpResponseRedirect
    """
    try:
        # Fetch Entry Details from the POST request
        date = request.POST['entryDate']
        time = request.POST['entryTime']
        units = request.POST['entryUnits']

        # Create a new Entry object and save it to the database
        new_entry = Entry(date=date, time=time, units=units, username=request.user.username)
        new_entry.save()

        # Success message
        message = 'SUCCESSFULLY ADDED NEW ENTRY TO DATABASE!'

        return HttpResponseRedirect(reverse('eskak:previous_entry_view') + f'?message={message}')

    except Exception as ex:
        # Get the error message and redirect back to new_entry_view with the error message
        error_message = str(ex)
        return HttpResponseRedirect(reverse('eskak:new_entry_view') + f'?error_message={error_message}')


# PREVIOUS ENTRIES VIEW
def previous_entries_view(request):
    """
    Display a list of previous entries for the logged-in user.

    This view retrieves and displays a list of entries created by the currently
    logged-in user.

    :param request: HttpRequest object
    :type request: HttpRequest

    :return: Rendered HTML page with previous entries
    :rtype: HttpResponse
    """
    # Retrieve any optional message from the request's GET parameters
    message = request.GET.get('message', '')

    # Retrieve all Entry objects from the database
    entries = Entry.objects.filter(username=request.user.username)

    return render(request, 'previousEntry.html', {'entries': entries, 'message': message})


# DELETE A ENTRY
def delete_entry(request, entry_id):
    """
    Delete an entry from the database.

    This view handles the deletion of a specific entry from the Eskak application's
    database based on the provided entry_id. It retrieves all Entry objects,
    searches for the entry with the given ID, deletes it if found, and redirects
    to the previous entries view with a success message.

    :param request: HttpRequest object
    :type request: HttpRequest
    :param entry_id: ID of the entry to be deleted
    :type entry_id: int

    :return: HttpResponseRedirect to previous_entry_view with success message
    :rtype: HttpResponseRedirect
    """
    try:
        # Retrieve the Entry object with the provided entry_id
        entry = Entry.objects.get(pk=entry_id)

        # Delete the entry
        entry.delete()

        # Success message
        message = 'SUCCESSFULLY REMOVED ENTRY FROM DATABASE'

        return HttpResponseRedirect(reverse('eskak:previous_entry_view') + f'?message={message}')

    except Entry.DoesNotExist:
        # Entry with the provided ID does not exist, redirect with an error message
        error_message = 'Entry not found'
        return HttpResponseRedirect(reverse('eskak:previous_entry_view') + f'?error_message={error_message}')