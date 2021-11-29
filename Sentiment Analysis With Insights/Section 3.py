import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = "DropDown"

def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('D:\\Jupyter\\Notebooks\\Forsk internship\\Project\\data\\Final_data.csv')

    global data
    data=scrappedReviews['Product Review'].sample(1000).tolist()
    global pickle_model
    file = open("pickle_model.pkl", 'rb')
    pickle_model = pickle.load(file)



    global vocab
    file = open("features.pkl", 'rb')
    vocab = pickle.load(file)



def check_review(reviewText):



#reviewText has to be vectorised, that vectorizer is not saved yet
#load the vectorize and call transform and then pass that to model preidctor
#load it later



    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))




    # Add code to test the sentiment of using both the model
    # 0 == negative 1 == positive

    return pickle_model.predict(vectorised_review)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")



def create_app_ui():
    
    global project_name
    main_layout = dbc.Container(
            
                [
                 html.H3(children = 'Sentiment Analysis with Dropdown', id='result',style = {'textAlign': 'center','background-color':'Pink'}),
                 html.Marquee(id='text',children='Lets predict the Sentiment ',style = {'width':'100%', 'height':50,'color':'grey'}),
                 html.Br(),
                 dcc.Dropdown(id='DropDown',options=[{'label': k, 'value': k} for k in (data)],style = {"margin-left": "100px",'width':1000, 'height':50}),
                 html.Br(),
                 html.Marquee(id='text1',children='The Prediction is made down ',style = {'width':'100%','height':50,'color':'blue'}),



                 html.H3(children = 'Positive OR Negative', id='result2',style = {'textAlign': 'center','width':'100%', 'height':50}),   
            
                ]
                        
                
            
        )

    return main_layout
@app.callback(

    Output( 'result2' , 'children' ),
    Output('result2','style'),
    [
    Input( 'DropDown' , 'value' )

]
)
def update_app_ui_3(value):
    print("Data Type = ", str(type(value)))
    print("Value = ", str(value))
    response = check_review(value)
    if (response[0] == 0):
        result = 'Negative'
        style= {"margin-left": "600px",'width':500, 'height':50,'color':'red'}
    elif (response[0] == 1 ):
        result = 'Positive'
        style= {"margin-left": "600px",'width':500, 'height':50,'color':'green'}



    else:
        result = 'Unknown'
        style=style = {"margin-left": "500px",'width':1500, 'height':50,'background-color':'grey'}



    return result,style


    
def main():
    print("Start of your project")
    global app
    global project_name
    
    open_browser()
    app.layout = create_app_ui()
    app.title = project_name
    app.run_server()
    app = None
    project_name = None
if __name__ == '__main__':
    main()