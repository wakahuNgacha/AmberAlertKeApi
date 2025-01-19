from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MissingPerson
from .serializers import MissingPersonSerializer

class MissingPersonView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Retrieve a single missing person
            try:
                missing_person = MissingPerson.objects.get(pk=pk)
                serializer = MissingPersonSerializer(missing_person)
                return Response(serializer.data)
            except MissingPerson.DoesNotExist:
                return Response({"error": "MissingPerson not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all missing persons
            missing_persons = MissingPerson.objects.all()
            serializer = MissingPersonSerializer(missing_persons, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new missing person
        serializer = MissingPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing missing person
        try:
            missing_person = MissingPerson.objects.get(pk=pk)
        except MissingPerson.DoesNotExist:
            return Response({"error": "MissingPerson not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MissingPersonSerializer(missing_person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a missing person
        try:
            missing_person = MissingPerson.objects.get(pk=pk)
            missing_person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MissingPerson.DoesNotExist:
            return Response({"error": "MissingPerson not found"}, status=status.HTTP_404_NOT_FOUND)
