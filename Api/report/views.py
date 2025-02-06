from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            # Retrieve a single report
            try:
                report = Report.objects.get(pk=pk)
                serializer = ReportSerializer(report)
                return Response(serializer.data)
            except Report.DoesNotExist:
                return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all reports
            reports = Report.objects.all()
            serializer = ReportSerializer(reports, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new report
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing report
        try:
            report = Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a report
        try:
            report = Report.objects.get(pk=pk)
            report.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Report.DoesNotExist:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
