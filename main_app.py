import streamlit as st
import pandas as pd
import hydralit_components as hc

st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
# we should only display a few locations at once. Need a button probably which allows to click for next 5
range_data = list(range(1,7,1))
menu_data = []
for val in range_data:
# specify the primary menu definition
    menu_data.append({'icon': "far fa-copy", 'label':"RESTAURANT "+str(val)})

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=False, 
    sticky_nav=True, 
    sticky_mode='pinned', 
)

st.header("Journal entry editable DF")
df = pd.read_csv("sample_data.csv")

accounts = df["account"].unique().tolist()
if menu_id == "RESTAURANT 1":
    editable_df = st.data_editor(df,
                                num_rows="dynamic",
                                use_container_width=True,
                                column_config = {
                                    "account" : st.column_config.SelectboxColumn(
                                        "Account",
                                        help = "The category of expense",
                                        options = accounts,
                                        required = True
                                    )
                                },hide_index=True)

    # you can access the data by just editable_df
    credit_sum = df["credit"].sum()
    debit_sum = df["debit"].sum()
    difference = df["debit"].sum() - df["credit"].sum()
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.write("")


    with col2:
        st.text_input('Difference',difference,disabled=True,key='diff')

    with col3:
        
        st.text_input('Credit Sum',credit_sum,disabled=True,key = 'credit_input')

    with col4:
        st.text_input('Debit Sum',debit_sum,disabled=True,key = 'debit_input')


