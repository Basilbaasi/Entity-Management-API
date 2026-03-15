from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = [
            'id',
            'vendor',
            'product',
            'primary_mapping',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        vendor = attrs.get('vendor')
        product = attrs.get('product')
        primary_mapping = attrs.get('primary_mapping', False)

        instance = getattr(self, 'instance', None)

        existing_mapping = VendorProductMapping.objects.filter(
            vendor=vendor,
            product=product
        )

        if instance:
            existing_mapping = existing_mapping.exclude(id=instance.id)

        if existing_mapping.exists():
            raise serializers.ValidationError(
                "This vendor-product mapping already exists."
            )

        if primary_mapping:
            existing_primary = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            )

            if instance:
                existing_primary = existing_primary.exclude(id=instance.id)

            if existing_primary.exists():
                raise serializers.ValidationError(
                    "This vendor already has a primary product mapping."
                )

        return attrs