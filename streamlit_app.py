import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# **Pradeep M, M.E**
##### *Resume* 
''')

image = Image.open('my_dp.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost Seven years of teaching experience and one year of Industrial experience as a Senior Data Analyst with Python(NLP) works. 
- Strong verbal and written communication skills as demonstrated by extensive participation in various conferences as well as publishing 3+ research articles.
- Strong track record in scholarly research with Research Interest Score of 9.6, H-index of `2` and total citation of 11+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/@kaanpomkarpomkarpipom4468" target="_blank">Pradeep M</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#python-tools">Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Engineering** (Computer Science and Engineering), *Anna University,India.*','2012-2014')
st.markdown('''
- CGPA: `8.1/10`
- Graduated with First Class.
''')
txt('**Bachelor of Engineering** (Computer Science and Engineering), *Anna University,India.*','2008-2021')

st.markdown(''' 
- CGPA:`7.8/10`
- Granduated with First Class.

 ''')

#####################
st.markdown('''
## Work Experience
''')
txt('**Senior Data Analyst**,Business Gateways International,Chennai','2022-Till now')
st.markdown('''
- Obtained Google Analytics Certification for GA4 from Google.

- Created Own Customized Business Intelligence tool(Apache Superset) and created dashboards based on Mysql queries and integrated in Web applications.

- Created Own Cube js tool(Sub layer of BI Tool) for performance improvement(Pre aggregations) for faster data loading in Web applications.

- Created  API Recommendations work for Customers based on their Search integrated with Python - NLP(Cosine Similarity) and Flask(Python -Micro webservices).

- Created AI Model- Entity Relationship(Spacy-Named Entity Recognition) for Customized Search of Customers should get relevant datas faster.

- Created and Integrated Search recommendations using "Fast-Autocomplete" and "Eldar" Python Libraries to be integrated with PHP web applications.

''')

txt('**Assistant Professor**,Department of Information Technology,Rajiv Gandhi College of Engineering and Technology,Pondicherry,India','2014-2021')
st.markdown(''' 

- **Placement Coordinator**:Actively Involved placement activites like managing technical and HR teams and taught technically  to students like Programming,Hackathons etc.

- **Subject Expert**:Taught subjects B.Tech,M.Tech and MCA students with various subjects.

- **Activities**:Involved in all students enriching activites like Freshers day Programs, NSS actvities,Cultural activities,Sports activities, Graduation Programs etc.

- Actively took part in the talent hiring process as well as help employees to plan and develop their career path.

''')

txt('**Content Creator**,[Kannpom Karpom Karpipom](https://www.youtube.com/@kaanpomkarpomkarpipom4468)','2018-Present')

st.markdown(''' 

- `140+` Subscribers on YouTube
- Created `45+` educational videos on Java, Python and many awareness videos for students.

''')
st.markdown('''
## Python Tools
''')

txt4('Flames App', 'A Funny Flames App','[Flames App](https://pradeep987654321-flames-simi-sp26mp.streamlit.app/)')
#####################



#####################
st.markdown('''
## Skills
''')
txt3('Business Intelligence ','`Apache Superset`')
txt3('Performance Layer','`Cube-js`')
txt3('Programming','`Python`')
txt3('Data Processing','`SQL`,`Pandas`')
txt3('Data Visualization','`Matplotlib`,`Plotly`')
txt3('Machine Learning','`Scikit-learn`')
txt3('Web Development','`Flask-API Development`,`CSS`')
txt3('Model Deployment','`Streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/pradeep-marimuthu-268b56ba/')
txt2('Facebook', 'https://www.facebook.com/pra.deep.104')
txt2('GitHub', 'https://github.com/Pradeep987654321')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Pradeep-Marimuthu')
txt2('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=57381413500')
txt2('ResearcherID', 'https://www.webofscience.com/wos/author/record/HTO-5704-2023')
