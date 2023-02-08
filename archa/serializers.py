from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from archa.models import User, Card

class UserSerializer(ModelSerializer):
    companies = SerializerMethodField()
    name = SerializerMethodField()

    def get_companies(self, obj):
        permissions = obj.permission_set.select_related('company').all()
        return [{
            "company_name": next(p.company.name for p in permissions if p.company.id == id),
            "permissions": [p.level for p in permissions if p.company.id == id],
        } for id in [p.company.id for p in permissions]]

    def get_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'companies']

class CardSerializer(ModelSerializer):
    company_name = SerializerMethodField()
    number = SerializerMethodField()
    balance = SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.name

    def get_number(self, obj):
        return '-'.join([''.join(['*' if j < 3 else obj.number[5*j+i] for i in range(4)]) for j in range(4)])

    def get_balance(self, obj):
        return obj.limit - obj.spent

    class Meta:
        model = Card
        fields = ['url', 'company_name', 'number', 'expiration', 'limit', 'balance']

class AdminCardSerializer(CardSerializer):
    url = HyperlinkedIdentityField(view_name='admin-cards-detail')
