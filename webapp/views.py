from django.shortcuts import redirect, render
from django.views import generic
from .models import Player
from .forms import *

import pandas as pd
import datetime
import csv
from io import TextIOWrapper, StringIO

from .functions import calc_age


import warnings
warnings.simplefilter('ignore', pd.core.common.SettingWithCopyWarning)

# Create your views here.

# HOMEページ

def index(request):
    index_dict = {
        'player_directory_link':"Player Directory",
        'past_match_results_link':"Past Match results",
        'create_a_formation_link':"Create a Formation",
        "name":"Yuki SHIMBO"
    }
    return render(request,'webapp/index.html', index_dict)



# 選手名鑑

def player_directory(request):
    players_data = Player.objects.values_list('pos', 'num','barth','name')
    players_data = pd.DataFrame(players_data,columns = ['Position', 'Uniform number','Barthday','Name',])
    num_by_pos = [players_data['Position'].value_counts()["GK"],
                players_data['Position'].value_counts()["DF"],
                players_data['Position'].value_counts()["MF"],
                players_data['Position'].value_counts()["FW"]
    ]

    # 今日時点の年齢の計算
    players_data["Age"] = 0
    players_data["id"] = 0
    today = datetime.date.today()
    for i in range(len(players_data)):
        players_data["id"][i] = i + 1
        players_data["Age"][i] = calc_age(players_data["Barthday"][i], today)

    pos_header = ["GK", "DF", "MF", "FW"]
    header = ['id', 'Position', 'Uniform number','Name','Barthday','Age'] # 表示する順序を決定
    players_data = players_data[header]

    pd_dict = {
        "pos_header":pos_header,
        "num_by_pos":num_by_pos,
        "name":"Yuki SHIMBO",
        'title':'テスト',
        'header':header,
        'val':players_data.values,
    }
    return render(request,'webapp/player_directory.html',pd_dict)



# フォーメーション作成

# フォーメーション設定
def create_a_formation(request):
    players_list = list(Player.objects.values_list('name',flat=True))
    player_select_form = SelectPlayers(request.POST)
    formation_select_form = Selectformation(request.POST)
    cf_list = {
        "information":"各ポジションの人数を選択してください。",
        "player_name":players_list,
        "fs_form":formation_select_form,
        "next":"next",
    }
    return render(request,'webapp/create_a_formation.html',cf_list)

# 選手登録
def player_register(request):
    players_list = list(Player.objects.values_list('name',flat=True))
    num_of_df = int(dict(request.POST)['num_of_DF'][0])
    num_of_mf = int(dict(request.POST)['num_of_MF'][0])
    num_of_fw = int(dict(request.POST)['num_of_FW'][0])

    if (request.method == 'POST'):
        if('player' in request.POST):
            selected_players = [int(i) for i in  dict(request.POST)['player']]
            player_names = [players_list[i] for i in selected_players]
            player_forms = []
            forms = []
            for i in range(11):
                forms.append(SelectPlayers(initial={"player":selected_players[i]}))
            forms.reverse()
            i = 11
            for _ in range(num_of_fw):
                player_forms.append({"idx":i,"pos":"FW","form":forms[i-1]})
                i -= 1
            for _ in range(num_of_mf):
                player_forms.append({"idx":i,"pos":"MF","form":forms[i-1]})
                i -= 1
            for _ in range(num_of_df):
                player_forms.append({"idx":i,"pos":"DF","form":forms[i-1]})
                i -= 1
            player_forms.append({"idx":i,"pos":"GK","form":forms[i-1]})
            cf_list = {"information":None,
                        "next":"next",
                        "player_name":players_list,
                        "player_forms":player_forms,
                        "request":dict(request.POST),
                        "num_of_DF":num_of_df,
                        "num_of_MF":num_of_mf,
                        "num_of_FW":num_of_fw,
                        "player":[str(11-x) for x in range(11)],
                    }
            if (len(set(player_names)))==11:
                cf_list['information'] = 'フォーメーションを作成しました。'
                cf_list['player'] = player_names
                return render(request,'webapp/player_register.html',cf_list)
            else:
                cf_list['information'] = '重複者がいます'
                return render(request,'webapp/player_register.html',cf_list)
        else:
            player_forms = []
            player_select_form = SelectPlayers()
            i = 11
            for _ in range(num_of_fw):
                player_forms.append({"idx":i,"pos":"FW","form":player_select_form})
                i -= 1
            for _ in range(num_of_mf):
                player_forms.append({"idx":i,"pos":"MF","form":player_select_form})
                i -= 1
            for _ in range(num_of_df):
                player_forms.append({"idx":i,"pos":"DF","form":player_select_form})
                i -= 1
            player_forms.append({"idx":i,"pos":"GK","form":player_select_form})

            cf_list = {"information":'各ポジションに選手を登録してください',
                        "next":"next",
                        "player_name":players_list,
                        "player_forms":player_forms,
                        "request":dict(request.POST),
                        "num_of_DF":num_of_df,
                        "num_of_MF":num_of_mf,
                        "num_of_FW":num_of_fw,
                        "player":[str(11-x) for x in range(11)],
                    }
            return render(request,'webapp/player_register.html',cf_list)

# 選手データのアップロード(csv)
def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8-sig')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            player, created = Player.objects.get_or_create(name=line[1])
            player.pos = line[0]
            player.num = line[1]
            player.age = line[2]
            player.barth = line[3]
            player.name = line[4]
            player.save()

        return render(request, 'webapp/upload.html')

    else:
        return render(request, 'webapp/upload.html')
