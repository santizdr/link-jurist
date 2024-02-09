from rest_framework import serializers
from .models import Case, Apply

class CaseSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField()
    is_applied = serializers.SerializerMethodField()

    def get_account_name(self, obj):
        return obj.account.name
    
    def get_is_applied(self, obj):
        account = self.context.get('account')
        applied = Apply.objects.filter(case=obj, applicant=account).exists()
        
        return applied
    
    class Meta:
        model = Case
        fields = '__all__'


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'