from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

#azureAPIのエンドポイント(URL)とAPI認証キー
KEY = 'e760a7ec5e4144bfaca9af627f4cf002'
ENDOPOINT = 'https://udemy-20221228.cognitiveservices.azure.com/'
computervision_client = ComputerVisionClient(ENDOPOINT, CognitiveServicesCredentials(KEY))

#画像を分析してタグづけを行う関数
def get_tags(file_path):
    image = open(file_path, "rb")
    tags_result = computervision_client.tag_image_in_stream(image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

#画像を分析して物体検出を行う関数
def detect_objects(file_path):
    image = open(file_path, "rb")
    detect_objects_result = computervision_client.detect_objects_in_stream(image)
    objects = detect_objects_result.objects
    return objects

import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont

st.title('物体検出アプリ')

#画像ファイルのアップローダー
uploaded_file = st.file_uploader('Choose an image...', type = ['jpg','png','jpeg'])

#アップロードしたファイルを一旦ローカルフォルダに保存してパスを取得する
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    #検出した物体を矩形で囲むための線の描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        #検出した物体の頂点座標の取得
        x = object.rectangle.x
        y = object.rectangle.y
        h = object.rectangle.h
        w = object.rectangle.w
        #検出した物体のキャプションの取得
        caption = object.object_property
        #キャプション用の文字の設定
        myfont = ImageFont.truetype(font='./Helvetica 400.ttf',size = 30)
        text_w, text_h = draw.textsize(caption,font=myfont)
        #検出した物体を囲む矩形の描画
        draw.rectangle([(x, y),(x+w, y+h)], fill = None, outline = 'green', width = 5)
        #キャプション
        draw.rectangle([(x, y),(x+text_w, y+text_h)], fill = 'green')
        draw.text((x, y), caption, fill = 'white', font=myfont)


    st.image(img)

    tags_name = get_tags(img_path)
    tags_name = ', '.join(tags_name)
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(f'> {tags_name}')    