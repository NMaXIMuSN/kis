from rest_framework import serializers

from amonic.models import User, Role, UserLog, UserCrashReport

class TitleSerializer(serializers.Serializer):
    title = serializers.CharField()

class IdTitleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "office",
            "is_active",
            "age",
        )

    role = TitleSerializer()
    office = TitleSerializer()
    age = serializers.IntegerField(required=False)

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "office",
            "birthdate",
            "office_id",
            "role_id",
        )

    role_id = serializers.ChoiceField(choices=Role.objects.filter(title__in=["User", "Administrator"]).values_list("id", flat=True))

class EditRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "office_id",
            "role_id",
        )

    role_id = serializers.ChoiceField(choices=Role.objects.filter(title__in=["User", "Administrator"]).values_list("id", flat=True))

class ToggleUserActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_active")

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = (
            "id",
            "login_date",
            "logout_date",
            "time_spent",
            "crash_report",
        )
        depth = 1

    time_spent = serializers.CharField()

class UserCrashReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCrashReport
        fields = ("description", "reason", "userlog")

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["user"] = self.context['request'].user
        return validated_data

    def create(self, validated_data):
        crash_report = UserCrashReport.objects.create(**validated_data)
        userlog = validated_data["userlog"]
        userlog.crash_report_id = crash_report.id
        userlog.save()
        return crash_report

class IsGracefulSerializer(serializers.Serializer):
    user_log_id = serializers.IntegerField()
    last_login = serializers.DateTimeField()
    is_graceful_logout = serializers.BooleanField()
