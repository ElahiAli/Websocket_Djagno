from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','last','age')

    def save(self, **kwargs):
        request = self.context.get("request")
        name = request.data.get("name")
        last = request.data.get("last")
        age = request.data.get("age")
        student = Student(
            name=name,
            last=last,
            age=age
        )

        student.save()