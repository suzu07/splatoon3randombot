# coding: utf-8
from typing import Awaitable
from discord import channel, guild
from discord.ext import commands
from selenium import webdriver
import discord
import random
import time
import datetime
import asyncio
from bs4 import BeautifulSoup

import requests
from bs4.element import Tag

# 接続に必要なオブジェクトを生成
client = discord.Client()
bot = commands.Bot(command_prefix='!')

# 自分のBotのアクセストークンに置き換えてください
TOKEN = "token "


# 起動時に動作する処理
@client.event
async def on_ready():
    print('success_connect')


@client.event
async def on_guild_join(guild):
    await  guild.channel.send('はじめまして！！@武器で武器をランダムでおすすめするよ！\n'
                              '武器種ごとのコマンドもあるから詳しくは@helpで表示してみてね！！')


@client.event
async def on_message(message):
    buki = ['スプラシューター', 'スプラシューターコラボ', 'スプラシューターベッチュー', 'プライムシューター',
            'プライムシューターコラボ', 'プライムシューターベッチュー', 'シャープマーカー', 'シャープマーカーネオ', '黒ガロン',
            '黒ガロンデコ',
            'スプラローラー', 'スプラローラーコラボ', 'スプラローラーベッチュー', 'ダイナモローラー',
            'ダイナモローラーベッチュー', 'ダイナモローラーテスラ', 'カーボンローラー', 'カーボンローラーデコ',
            'わかばシューター', 'もみじシューター',
            'おちばシューター', 'プロモデラーMC銀', 'プロモデラーRC金', 'プロモデラーPC銅', 'N-ZAP',
            'N-ZAP赤', 'N-ZAP銅', '52ガロン', '52ガロンベッチュー', '52ガロンデコ', 'ジェットスイーパー',
            'ジェットスイーパーカスタム', 'L3リールガン',
            'L3リールガンベータークイボの方', 'L3リールガンベッチュー', 'H3リールガン',
            'H3リールガンベーターインクアーマーの方', 'H3リールガンチェリー', 'ボールドマーカー', 'ボールドマーカーネオ',
            '銅ボールドマーカー', 'ボトルガイザー', 'ボトルガイザーフォイル',
            'ホットブラスター', 'ホットブラスターカスタム', 'ラピッドブラスター', 'ラピッドブラスターデコ',
            'ラピッドブラスターベッチュー', 'ノヴァブラスター', 'ノヴァブラスターネオ', 'ノヴァブラスターベッチュー',
            'クラッシュブラスター', 'クラッシュブラスターネオ', 'Rブラスターエリート', 'Rブラスターエリートデコ',
            'ロングブラスター', 'ロングブラスターカスタム',
            'ロングブラスターネクロ', 'ホクサイ', 'ホクサイヒュー', 'ホクサイベッチュー', 'パブロ', 'パブロヒュー',
            'パーマネントパブロ', 'スプラチャージャー', 'スプラチャージャーコラボ', 'スプラスコープ',
            'スプラスコープコラボ', 'スプラチャージャーベッチュー', 'スプラスコープベッチュー', '4Kリッター',
            '4Kリッターカスタム', '4Kリッタースコープ', '4Kリッタースコープカスタム', 'ソイチューバー',
            'ソイチューバーカスタム', 'スクイックリンα', 'スクイックリンβ', 'スクイックリンγ', '竹・甲', '竹・乙',
            '竹・丙', 'バケットスロッシャー', 'バケットスロッシャーデコ', 'バケットスロッシャーソーダ',
            'ヒッセン', 'ヒッセンヒュー', 'スクリュースロッシャー', 'スクリュースロッシャーネオ',
            'スクリュースロッシャーベッチュー', 'エクスプロッシャー', 'エクスプロッシャーカスタム', 'オーバーフロッシャー',
            'オーバーフロッシャーデコ',
            'バレルスピナー', 'バレルスピナーデコ', 'バレルスピナーリミックス', 'スプラスピナー', 'スプラスピナーコラボ',
            'スプラスピナーベッチュー', 'ハイドラント', 'ハイドラントカスタム', 'クーゲルシュライバー',
            'クーゲルシュライバーヒュー', 'ノーチラス47', 'ノーチラス79', 'スプラマニューバー', 'スプラマニューバーコラボ',
            'スプラマニューバーベッチュー',
            'スパッタリー', 'スパッタリーヒュー', 'スパッタリークリア', 'デュアルスイーパー', 'デュアルスイーパーカスタム',
            '青ケルビン', '黄色ケルビン', 'ケルビンベッチュー', 'クワッドホッパーブラック', 'クワッドホッパーホワイト',
            'パラシェルター', 'パラシェルターソレーラ', 'キャンピングシェルター', 'キャンピングシェルターソレーラ',
            'キャンピングシェルターカーモ', 'スパイガジェット', 'スパイガジェットソレーラ', 'スパイガジェットベッチュー']

    weapon = [['スプラシューター', 'スプラシューターコラボ', 'プライムシューター',
               'プライムシューターコラボ', 'シャープマーカー', '52ガロン',
               'わかばシューター', 'もみじシューター',
               'プロモデラーMC銀', 'プロモデラーRC金', 'N-ZAP',
               '52ガロン', 'ジェットスイーパー',
               'L3リールガン',
               'H3リールガン',
               'ボールドマーカー',
               'ボトルガイザー'],
              # 1
              ['スプラローラー', 'ダイナモローラー',
               'カーボンローラー', 'カーボンローラーデコ',
               'ワイドローラー', ],
              # 2
              ['ホットブラスター', 'ラピッドブラスター',
               'ノヴァブラスター', 'ノヴァブラスターネオ',
               'クラッシュブラスター',
               'ロングブラスター'],
              # 3
              ['ホクサイ', 'パブロ', 'パブロヒュー', ],
              # 4
              ['スプラチャージャー', 'スプラスコープ',
               '4Kリッター',
               '4Kリッタースコープ', 'ソイチューバー', 'R-PEN/5H',
               'スクイックリンα', '竹・甲'],
              # 5
              ['バケットスロッシャー', 'バケットスロッシャーデコ',
               'ヒッセン', 'スクリュースロッシャー',
               'エクスプロッシャー', 'オーバーフロッシャー'],
              # 6
              ['バレルスピナー', 'スプラスピナー', 'スプラスピナーコラボ',
               'ハイドラント', 'クーゲルシュライバー', 'ノーチラス47'],
              # 7
              ['スプラマニューバー',
               'スパッタリー', 'スパッタリーヒュー', 'デュアルスイーパー',
               '青ケルビン', 'クワッドホッパーブラック'],
              # 8
              ['パラシェルター', 'キャンピングシェルター', 'スパイガジェット']]

    def get_weapon(n):
        return 'おすすめの武器は!!  ' + str(random.choice(weapon[n])) + '  !!です！'

    # if message.isMemberMentioned(client.user):
    #     message.channel.send(message, "@helpですべてのコマンドを表示できます。")
    #     return 0

    # 送られたメッセージが @ helloだったら
    if message.content == '@help':
        await message.channel.send(
            '@武器---ランダムにすべての武器から選びます\n\
@シューター - --ランダムにシューターの武器から選びます\n\
@ローラー - --ランダムにローラーの武器から選びます\n\
@ブラスター - --ランダムにブラスターの武器から選びます\n\
@チャージャー---ランダムにチャージャーの武器から選びます\n\
@スピナー - --ランダムにスピナーの武器から選びます\n\
@傘 - --ランダムに傘の武器から選びます\n\
@マニューバー - --ランダムにマニューバーの武器から選びます\n\
@バケツ - --ランダムにバケツの武器から選びます')

    if message.content == '@武器' or message.content == '@ぶき' or message.content == '@buki':
        await message.channel.send(
            'おすすめの武器は!!  {0}  !!です！'.format(
                str(random.choice(random.choice(weapon)))))
        return 0
    if message.content == '@シューター':
        await message.channel.send(get_weapon(0))
        return 0
    if message.content == '@ローラー':
        await message.channel.send(get_weapon(1))
        return 0
    if message.content == '@ブラスター':
        await message.channel.send(get_weapon(2))
        return 0
    if message.content == '@チャージャー':
        await message.channel.send(get_weapon(4))
        return 0
    if message.content == '@傘':
        await message.channel.send(get_weapon(8))
        return 0
    if message.content == '@筆':
        await message.channel.send(get_weapon(3))
        return 0
    if message.content == '@バケツ':
        await message.channel.send(get_weapon(5))
        return 0
    if message.content == '@スピナー':
        await message.channel.send(get_weapon(6))
        return 0
    if message.content == '@マニューバー ' or message.content == '@マニューバ':
        await message.channel.send(get_weapon(7))
        return 0


client.run(TOKEN)
