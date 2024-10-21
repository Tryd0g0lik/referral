# This is a sample Python script.
# from referral.models_more import create_table, engine

from referral.views import app_router

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    
    app_new = app_router()


  
    app_new.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
