import streamlit as st

pages =  {"Home":[st.Page("VHP.py", title="Vehicle Health Predictor"),],
        "Mileage":[st.Page("m_tc.py", title="Tyre Condition"),
                   st.Page("m_oil.py",title="Oil Level"),
                   st.Page("m_bat.py",title="Battery Voltage"),
                   st.Page("m_load.py",title="Vehicle Load"),],
       "Engine Health Score": [st.Page("ehs_tc.py", title="Tyre Condition"),
                   st.Page("ehs_oil.py",title="Oil Level"),
                   st.Page("ehs_bat.py",title="Battery Voltage"),
                   st.Page("ehs_load.py",title="Vehicle Load"),],
        "Time Until Next Service":[st.Page("tuns_tc.py", title="Tyre Condition"),
                   st.Page("tuns_oil.py",title="Oil Level"),
                   st.Page("tuns_bat.py",title="Battery Voltage"),
                   st.Page("tuns_load.py",title="Vehicle Load")]}
    

pg = st.navigation(pages,position="sidebar",expanded=False)
pg.run()