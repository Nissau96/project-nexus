from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer


# Listing All Polls View.
class PollListCreate(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

# View for retrieving a single, specific poll.
class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

# VoteHandling View
class VoteCreate(APIView):
    serializer_class = ChoiceSerializer

    def post(self, request, pk, choice_pk):
        poll = get_object_or_404(Poll, pk=pk)

        if poll.voted_by.filter(id=request.user.id).exists():
            # If they have, return an error response.
            return Response(
                {'detail': 'You have already voted on this poll.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        choice = get_object_or_404(Choice, pk=choice_pk, poll_id=pk)
        choice.votes += 1
        choice.save()

        poll.voted_by.add(request.user)

        serializer = self.serializer_class(choice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)