from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'id',
            'name',
            'code',
            'description',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_code(self, value):
        """
        Ensure the code is unique and not empty.
        DRF will handle the unique constraint at the database level,
        but we can raise a nicer validation error here too.
        """
        if not value:
            raise serializers.ValidationError("Code is required.")
        # Check for existing vendor with the same code
        if Vendor.objects.filter(code=value).exists():
            raise serializers.ValidationError("Vendor with this code already exists.")
        return value