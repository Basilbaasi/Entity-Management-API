from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = [
            'id',
            'product',
            'course',
            'primary_mapping',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        product = attrs.get('product')
        course = attrs.get('course')
        primary_mapping = attrs.get('primary_mapping', False)

        instance = getattr(self, 'instance', None)

        existing_mapping = ProductCourseMapping.objects.filter(
            product=product,
            course=course
        )

        if instance:
            existing_mapping = existing_mapping.exclude(id=instance.id)

        if existing_mapping.exists():
            raise serializers.ValidationError(
                "This product-course mapping already exists."
            )

        if primary_mapping:
            existing_primary = ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
            )

            if instance:
                existing_primary = existing_primary.exclude(id=instance.id)

            if existing_primary.exists():
                raise serializers.ValidationError(
                    "This product already has a primary course mapping."
                )

        return attrs