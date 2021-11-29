#Importing the libraries
import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output , State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


# Declaring Global variables
project_name = None
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('D:\\Jupyter\\Notebooks\\Forsk internship\\Project\\data\\Final_data.csv')
  
    global pickle_model
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("features.pkl", 'rb') 
    vocab = pickle.load(file)
    reviewText=df['Product Review']

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform(reviewText))
    pred=pickle_model.predict(vectorised_review)
    df['Positivity'] =pred
    df['Sentiment'] =None

    df['Sentiment']=np.where(df['Positivity']==1,'Positive','Negative')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
    [
    html.H1(id='Main_title', children = "Pie chart for web scrapped",style={'textAlign':'center'}),
    dcc.Graph(id='Pie',figure=px.pie(data_frame=df,names=df['Sentiment'])),
    ]    
    )
    
    return main_layout
# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    
    global scrappedReviews
    global project_name
    global app
    
    project_name = "Pie chart"
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
        
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
          
# Calling the main function 
if __name__ == '__main__':
    main()