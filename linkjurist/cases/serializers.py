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
    case_title = serializers.SerializerMethodField()
    applied_by = serializers.SerializerMethodField()
    case_post_date = serializers.SerializerMethodField()
    case_expiry_date = serializers.SerializerMethodField()
    case_applications = serializers.SerializerMethodField()
    case_visualizations = serializers.SerializerMethodField()

    def get_case_title(self, obj):
        return obj.case.title
    
    def get_applied_by(self, obj):
        return obj.case.account.name
    
    def get_case_post_date(self, obj):
        return obj.case.post_date
    
    def get_case_expiry_date(self, obj):
        return obj.case.expiry_date
    
    def get_case_applications(self, obj):
        return obj.case.applications
    
    def get_case_visualizations(self, obj):
        return obj.case.visualizations
    
    class Meta:
        model = Apply
        fields = '__all__'
        