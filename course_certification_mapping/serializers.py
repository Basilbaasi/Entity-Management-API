from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = [
            'id',
            'course',
            'certification',
            'primary_mapping',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        course = attrs.get('course')
        certification = attrs.get('certification')
        primary_mapping = attrs.get('primary_mapping', False)

        instance = getattr(self, 'instance', None)

        existing_mapping = CourseCertificationMapping.objects.filter(
            course=course,
            certification=certification
        )

        if instance:
            existing_mapping = existing_mapping.exclude(id=instance.id)

        if existing_mapping.exists():
            raise serializers.ValidationError(
                "This course-certification mapping already exists."
            )

        if primary_mapping:
            existing_primary = CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
            )

            if instance:
                existing_primary = existing_primary.exclude(id=instance.id)

            if existing_primary.exists():
                raise serializers.ValidationError(
                    "This course already has a primary certification mapping."
                )

        return attrs