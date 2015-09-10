# coding=utf-8
from django.forms import ModelForm, DateInput, TextInput, Textarea, ClearableFileInput, RadioSelect
from education.models import *
from django.utils.translation import ugettext_lazy as _
__author__ = 'Administrator'

'''
class HealthEducateForm(ModelForm):
    class Meta:
        model = HealthEducate
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'way': RadioSelect,
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:80px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 200px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 200px; height: 200px'}),
            'upload': ClearableFileInput,
        }
'''


class EducationActivityForm(ModelForm):
    class Meta:
        model = EducationActivity
        fields = '__all__'


class AdBoardForm(ModelForm):
    class Meta:
        model = AdBoard
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class AdBoardUpdateForm(ModelForm):
    class Meta:
        model = AdBoardUpdate
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class AdBookForm(ModelForm):
    class Meta:
        model = AdBook
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class AdPageForm(ModelForm):
    class Meta:
        model = AdPage
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class AdBookletForm(ModelForm):
    class Meta:
        model = AdBooklet
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class ShelfForm(ModelForm):
    class Meta:
        model = Shelf
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class AdBoardMaintenanceForm(ModelForm):
    class Meta:
        model = AdBoardMaintenance
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class PublicHealthConsultationForm(ModelForm):
    class Meta:
        model = PublicHealthConsultation
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class HealthKnowledgeLectureForm(ModelForm):
    class Meta:
        model = HealthKnowledgeLecture
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }


class HealthEducationWebsiteForm(ModelForm):
    class Meta:
        model = HealthEducationWebsite
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'class': 'easyui-datebox',
            'data-options': 'formatter:myformatter,parser:myparser'}),
            'place': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:350px'}),
            'way': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:585px'}),
            'topic': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:580px'}),
            'principal': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:590px'}),
            'audience': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'people_number': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:120px'}),
            'material': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'count': TextInput(attrs={'class': 'easyui-textbox', 'style': 'width:200px'}),
            'content': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 580px; height: 200px'}),
            'evaluation': Textarea(attrs={'class': 'easyui-textbox', 'data-options': 'multiline:true',
            'style': 'width: 555px; height: 200px'}),
            'upload': ClearableFileInput,
        }

'''
class AdBoardForm(ModelForm):
    class Meta:
        model = AdBoard
        fields = '__all__'
        labels = {
            'date': _(u'布置时间'),
            'institution': _(u'布置机构'),
            'count': _(u'布置数量'),
            'principal': _(u'负责人'),
            'content': _(u'内容概要'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class AdBoardUpdateForm(ModelForm):
    class Meta:
        model = AdBoardUpdate
        fields = '__all__'
        labels = {
            'date': _(u'更新时间'),
            'institution': _(u'更新机构'),
            'times': _(u'更新次数'),
            'count': _(u'更新数量'),
            'principal': _(u'负责人'),
            'content': _(u'更新内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'times': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class AdBookForm(ModelForm):
    class Meta:
        model = AdBook
        fields = '__all__'
        labels = {
            'date': _(u'印刷时间'),
            'institution': _(u'宣传机构'),
            'count': _(u'宣传数量'),
            'principal': _(u'负责人'),
            'content': _(u'宣传内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class AdPageForm(ModelForm):
    class Meta:
        model = AdPage
        fields = '__all__'
        labels = {
            'date': _(u'印刷时间'),
            'institution': _(u'宣传机构'),
            'count': _(u'宣传单数量'),
            'principal': _(u'负责人'),
            'content': _(u'宣传内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class AdBookletForm(ModelForm):
    class Meta:
        model = AdBooklet
        fields = '__all__'
        labels = {
            'date': _(u'印刷时间'),
            'institution': _(u'宣传机构'),
            'count': _(u'宣传折页数量'),
            'principal': _(u'负责人'),
            'content': _(u'宣传内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class ShelfForm(ModelForm):
    class Meta:
        model = Shelf
        fields = '__all__'
        labels = {
            'date': _(u'摆放时间'),
            'institution': _(u'摆放地点'),
            'count': _(u'摆放数量'),
            'principal': _(u'负责人'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class AdBoardMaintenanceForm(ModelForm):
    class Meta:
        model = AdBoardMaintenance
        fields = '__all__'
        labels = {
            'date': _(u'维护时间'),
            'institution': _(u'维护机构'),
            'count': _(u'维护数量'),
            'principal': _(u'负责人'),
            'content': _(u'宣传栏内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        labels = {
            'date': _(u'播放时间'),
            'end_date': _(u''),
            'institution': _(u'播放机构'),
            'count': _(u'资料数量'),
            'principal': _(u'负责人'),
            'content': _(u'播放内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'end_date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'count': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class PublicHealthConsultationForm(ModelForm):
    class Meta:
        model = PublicHealthConsultation
        fields = '__all__'
        labels = {
            'date': _(u'咨询时间'),
            'institution': _(u'咨询机构'),
            'principal': _(u'负责人'),
            'content': _(u'咨询内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class HealthKnowledgeLectureForm(ModelForm):
    class Meta:
        model = HealthKnowledgeLecture
        fields = '__all__'
        labels = {
            'date': _(u'讲座时间'),
            'institution': _(u'负责机构'),
            'principal': _(u'负责人'),
            'content': _(u'讲座内容'),
            'load': _(u'图片上传')
        }
        widgets = {
            'date': DateInput(attrs={'size': 20, 'class': 'form-control'}),
            'institution': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }


class HealthEducationWebsiteForm(ModelForm):
    class Meta:
        model = HealthEducationWebsite
        fields = '__all__'
        labels = {
            'institution': _(u'负责机构'),
            'principal': _(u'负责人'),
            'content': _(u'网站概况'),
            'load': _(u'网站链接')
        }
        widgets = {
            'institution': TextInput(attrs={'size': 32}),
            'principal': TextInput(attrs={'size': 32}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10}),
            'load': ClearableFileInput(attrs={'size': 20})
        }

'''