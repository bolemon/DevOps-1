import models
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Group
        fields = ('id', 'name', 'info',
                )

class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Storage
        fields = ('id','disk_size','disk_path','info'
                  )

class HostSerializer(serializers.ModelSerializer):
    systemtype = serializers.CharField(source='get_systemtype_display')
    class Meta:
        model=models.Host
        fields = ('id','systemtype','manage_ip','service_ip','outer_ip','server_position','hostname',
                  'normal_user','sshpasswd','sshport','coreness','memory','root_disk','info'
                  ,'storages'
                  )


class HostUpdateGroupSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True,queryset=models.Host.objects.all())
    class Meta:
        model = models.Group
        fields = ['id', 'hosts']

class SystemTypeSerializer(serializers.CharField):
    name=serializers.CharField()
    percentage=serializers.IntegerField()
    class Meta:
        fields= ['name','percentage']

