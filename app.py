import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    
    # Define function for Home page
    def home_page():
        st.write("Welcome to the Home page!")

    # Define function for Profile page
    def profile_page():
        st.write("Welcome to the Profile page!")

    # Define function for Settings page
    def settings_page():
      st.write("Welcome to the setting page!")
    
    menu_selection = st.sidebar.radio("Menu", ["Home", "Profile", "Settings"])
    if menu_selection == "Home":
        home_page()
    elif menu_selection == "Profile":
        profile_page()
    elif menu_selection == "Settings":
        settings_page()

