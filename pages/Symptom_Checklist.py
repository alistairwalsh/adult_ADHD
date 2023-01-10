import streamlit as st

st.text('''Instructions:
Please answer the questions below, rating yourself on each of the criteria shown. As you
answer each question, select the box that best describes how you have felt and conducted
yourself over the past 6 months.''')

text = '''1
PART A -
How often do you have trouble wrapping up the final details
of a project, once the challenging parts have been done?
0 0 1 1 1
2
How often do you have difficulty getting
things in order when you have to do a
task that requires organisation?
0 0 1 1 1
3
How often do you have problems
remembering appointments or
obligations?
0 0 1 1 1
4
When you have a task that requires a lot
of thought, how often do you avoid or
delay getting started?
0 0 0 1 1
5
How often do you fidget or squirm with
your hands or feet when you have to sit
down for a long time?
0 0 0 1 1
6
How often do you feel overly active and
compelled to do things, like you were
driven by a motor?
0 0 0 1 1
7
PART B -
How often do you make careless mistakes when you
have to work on a boring or difficult project?
0 0 0 1 1
8
How often do you have difficulty keeping
your attention when you are doing boring
or repetitive work?
0 0 0 1 1
9
How often do you have difficulty
concentrating on what people say to you,
even when they are speaking to you directly?
0 0 1 1 1
10
How often do you misplace or have
difficulty finding things at home or at
work?
0 0 0 1 1
11 How often are you distracted by
activity or noise around you? 0 0 0 1 1
12
How often do you leave your seat in
meetings or other situations in which you
are expected to remain seated?
0 0 1 1 1
13 How often do you feel restless or
fidgety? 0 0 0 1 1
14
How often do you have difficulty
unwinding and relaxing when you have
time to yourself?
0 0 0 1 1
15
How often do you find yourself talking
too much when you are in social
situations?
0 0 0 1 1
16
When you’re in a conversation, how often do you
find yourself finishing the sentences of the people
you are talking to, before they can finish them
themselves?
0 0 1 1 1
Page 1 of 2
 NovoPsych
Never Rarely Sometimes Often Very Often
17
How often do you have difficulty waiting
your turn in situations when turn taking is
required?
0 0 0 1 1
18 How often do you interrupt others
when they are busy? '''


text = [part for part in text.split('\n') if part.strip() not in ['Page 1 of 2', 'NovoPsych']]

for line in text:
    if not line.isnumeric():
        st.text(line.strip())

#st.radio('')