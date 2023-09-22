from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.models import Review, RATING_CHAR_ON, RATING_CHAR_OFF, RATING_RANGE
from follows.models import UserFollows
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from itertools import chain
from django.db.models import CharField, Value


class FeedPage(View):
    """View to see and interact with publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        # Get the currently logged in user
        current_user = request.user

        # Get the users that the current user is subscribed to
        subscribed_users = [subscription.followed_user for subscription in
                            UserFollows.objects.filter(user=current_user)]

        # Get tickets created by the current user and the subscribed users
        tickets = Ticket.objects.filter(user__in=[current_user] + subscribed_users)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        # Get tickets that have not been reviewed yet
        tickets_not_reviewed = tickets.exclude(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=tickets)]).annotate(
            ticket_status=Value('not_reviewed', CharField()))

        # Get tickets that have been reviewed
        tickets_reviewed = tickets.filter(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=tickets)]).annotate(
            ticket_status=Value('already_reviewed', CharField()))

        # Get reviews created by the current user
        own_reviews = Review.objects.filter(user=current_user)
        own_reviews = own_reviews.annotate(content_type=Value('REVIEW', CharField()))

        # Get reviews for tickets created by the current user (excluding the current user's own reviews)
        reviews_current_user_tickets = Review.objects.filter(
            ticket__in=Ticket.objects.filter(user=current_user)).exclude(user=current_user)
        reviews_current_user_tickets = reviews_current_user_tickets.annotate(content_type=Value('REVIEW', CharField()))

        # Get reviews from users that the current user is subscribed to
        subscriptions_reviews = Review.objects.filter(
            user__in=[user_follow.followed_user for user_follow in UserFollows.objects.filter(user=current_user)])
        subscriptions_reviews = subscriptions_reviews.annotate(content_type=Value('REVIEW', CharField()))

        # Combine all the posts (tickets and reviews) into a single iterable
        posts = chain(tickets_not_reviewed, tickets_reviewed,
                      own_reviews, reviews_current_user_tickets, subscriptions_reviews)

        # Render the feed template with the posts and other context variables
        return render(request, 'feed/feed.html',
                      context={'posts': posts,
                               'rating_range': RATING_RANGE,
                               'rating_char_on': RATING_CHAR_ON,
                               'rating_char_off': RATING_CHAR_OFF})