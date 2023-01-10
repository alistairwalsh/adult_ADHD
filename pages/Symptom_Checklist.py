import streamlit as st
import pandas as pd

st.text('''Instructions:
Please answer the questions below, rating yourself on each of the criteria shown. As you
answer each question, select the box that best describes how you have felt and conducted
yourself over the past 6 months.''')

options = ('Never','Rarely','Sometimes','Often','Very Often')

text = [
'How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?',

'How often do you have difficulty getting things in order when you have to do a task that requires organisation?',

'How often do you have problems remembering appointments or obligations?',

'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?',

'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?',

'How often do you feel overly active and compelled to do things, like you were driven by a motor?',

'How often do you make careless mistakes when you have to work on a boring or difficult project?',

'How often do you have difficulty keeping your attention when you are doing boring or repetitive work?',

'How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?',

'How often do you misplace or have difficulty finding things at home or at work?',

'How often are you distracted by activity or noise around you?',

'How often do you leave your seat in meetings or other situations in which you are expected to remain seated?',

'How often do you feel restless or fidgety?',

'How often do you have difficulty unwinding and relaxing when you have time to yourself?',

'How often do you find yourself talking too much when you are in social situations?',

'When you’re in a conversation, how often do you find yourself finishing the sentences of the people you are talking to, before they can finish them themselves?',

'How often do you have difficulty waiting your turn in situations when turn taking is required?',

'How often do you interrupt others when they are busy?']

results = {q:'' for q in text}

for k,v in results.items():
    results[k] = st.radio(k,options, horizontal = True, index = 2)

st.text(results)