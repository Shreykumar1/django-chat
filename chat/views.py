from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q
from django.utils import timezone
import datetime  # Import the datetime module

@login_required
def chat_room(request, room_name):
    search_query = request.GET.get('search', '')  # Capture search query from GET
    users = User.objects.exclude(id=request.user.id)  # Get all users excluding the current user
    chats = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver__username=room_name)) |
        (Q(receiver=request.user) & Q(sender__username=room_name))
    )

    if search_query:
        chats = chats.filter(Q(content__icontains=search_query))  # Filter chats by search query

    chats = chats.order_by('timestamp')  # Order chats by timestamp in ascending order
    user_last_messages = []

    # Loop through users to fetch the last message for each user
    for user in users:
        last_message = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=user)) |
            (Q(receiver=request.user) & Q(sender=user))
        ).order_by('-timestamp').first()  # Get the most recent message

        user_last_messages.append({
            'user': user,
            'last_message': last_message,
            'timestamp': last_message.timestamp if last_message else datetime.datetime.min
        })

    # Make sure all timestamps are timezone-aware before comparison
    for msg in user_last_messages:
        if msg['timestamp'].tzinfo is None:
            msg['timestamp'] = timezone.make_aware(msg['timestamp'])
    
    user_last_messages.sort(
        key=lambda x: x['timestamp'],
        reverse=True
    )

    return render(request, 'chat.html', {
        'room_name': room_name,
        'chats': chats,
        'users': users,
        'user_last_messages': user_last_messages,
        'search_query': search_query
    })
