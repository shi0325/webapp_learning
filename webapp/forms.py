from django import forms
from django.core.exceptions import ValidationError
from .models import Player

class PlayerForm(forms.Form):
    name = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')
    age = forms.IntegerField(label='数量')
    pos = forms.CharField(label='文字入力')

class Selectformation(forms.Form):
    CHOICE =[(str(x),str(x)) for x in range(6)]
    num_of_DF = forms.ChoiceField(
            label="DF",
            required=False,
            disabled=False,
            initial=['0'],
            choices=CHOICE,
            widget=forms.Select(attrs={
                'id': 'num_of_DF',}))

    num_of_MF = forms.ChoiceField(
            label="MF",
            required=False,
            disabled=False,
            initial=['0'],
            choices=CHOICE,
            widget=forms.Select(attrs={
                'id': 'num_of_MF',}))

    num_of_FW = forms.ChoiceField(
            label="FW",
            required=False,
            disabled=False,
            initial=['0'],
            choices=CHOICE,
            widget=forms.Select(attrs={
                'id': 'num_of_FW',}))

class SelectPlayers(forms.Form):
    labels = ['GK','DF','MF','FW']
    players_name = list(Player.objects.values_list('name',flat=True))
    players_pos = list(Player.objects.values_list('pos',flat=True))
    players_num = list(Player.objects.values_list('num',flat=True))
    players_list = []
    for i in range(len(players_name)):
        players_list.append(str(players_pos[i])+"-"+str(players_num[i])+ "-" +str(players_name[i]))

    CHOICE = [(str(x),player) for x , player in enumerate(players_list)]
    CHOICE.reverse()

    player = forms.ChoiceField(
            label=None,
            required=False,
            disabled=False,
            choices=CHOICE,
            widget=forms.Select(attrs={'class':'select_players'}
                )
            )