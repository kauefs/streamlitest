# https://github.com/PacktPublishing/Streamlit-for-Data-Science/blob/main/trees_app/all_code.py
import      numpy            as   np
import     pandas            as   pd
import  streamlit            as   st
import    seaborn            as   sns
import matplotlib.pyplot     as   plt
import     plotly.express    as   px
# Settings:
# st.secrets['cookie_secret']
pd.options.plotting.matplotlib.register_converters = True
plt.rcParams[  'figure.autolayout']    =             True
plt.rcParams[    'font.family'    ]    =                                         'sans-serif'
sns.set_theme(context='notebook', style='whitegrid', palette='colorblind',  font='sans-serif', font_scale=1.15, color_codes=True, rc={'grid.color':'1','grid.linestyle':':'})
FontT={'family':'sans-serif'    ,'color':'#000000', 'size'  : 13,   'fontweight':'semibold'  }
FontY={'family':'sans-serif'    ,'color':'#FF4500', 'size'  : 10,   'fontweight':'regular'   }
FontX={'family':'sans-serif'    ,'color':'#4CAF50', 'size'  : 10,   'fontweight':'regular'   }
# Page:
st.set_page_config(page_title='ƊⱭȾɅViƧi🧿Ƞ&trade;', page_icon='🧿', layout='wide', initial_sidebar_state='collapsed')
def state( ):
    if 'state' not in st.session_state:st.session_state.state=[ ]
# SIDE
st.sidebar.title   ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider ( )
st.sidebar.success ('ƊⱭȾɅ'              )
st.sidebar.info    ('ViƧi🧿Ƞ'            )
st.sidebar.divider ( )
st.sidebar.warning ('Ʌnalysis'           )
st.sidebar.divider ( )
st.sidebar.markdown('''
![2025.12.05  ](https://img.shields.io/badge/2025.12.05-000000)

[![GitHub     ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium     ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn   ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python     ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![License    ](https://img.shields.io/badge/Apache--2.0-D22128?style=flat&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71&color=D22128)](https://www.apache.org/licenses/LICENSE-2.0)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN:
state      ( )
st.title('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.divider ( )
# @st.cache_data
