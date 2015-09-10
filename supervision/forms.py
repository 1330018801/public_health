from django.forms import ModelForm, Textarea, DateInput, TextInput, DateTimeInput
from supervision.models import Patrol, InformationReport

__author__ = 'Administrator'


class PatrolForm(ModelForm):
    class Meta:
        model = Patrol
        fields = '__all__'
        widgets = {
            'place_content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 128px; height: 100px'}),
            'main_problem': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 150px; height: 100px'}),
            'patrol_date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'patrolman': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'remarks': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 128px; height: 100px'})
        }


class InformationReportForm(ModelForm):
    class Meta:
        model = InformationReport
        fields = '__all__'
        widgets = {
            'discover_date': DateTimeInput(attrs={'class': 'easyui-datetimebox',
            'data-options': 'showSeconds:false'}),
            'information_type': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:128px'}),
            'information_content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 180px; height: 100px'}),
            'report_date': DateTimeInput(attrs={'class': 'easyui-datetimebox',
            'data-options': 'showSeconds:false'}),
            'reporter': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'})
        }