#text area
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = "Text"

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
                 html.H1(id='Main_title', children = "Sentiment Analysis with Insights",style = {'textAlign': 'center','background-color':'orange'}),
html.Marquee(id='text',children='Lets predict the Sentiment ',style = {'width':'100%', 'height':50,'color':'grey'}),



dcc.Textarea(
id = 'textarea_review',
placeholder = 'Enter the review here.....',
style = {"margin-left": "125px",'width':1000, 'height':100}
),

dbc.Button(
children = 'Submit',
id = 'button_review',
color = 'dark',
style={"margin-left": "525px",'width':'220px'}
),
html.Tr(),
html.Marquee(id='text1',children='The Prediction is made down ',style = {'width':'100%','height':50,'color':'blue'}),

html.H3(children = 'Positive/Negative', id='result',style = {'textAlign': 'center','width':'100%', 'height':50}),
                ] )

    return main_layout
@app.callback(
Output( 'result' , 'children' ),
Output('result','style'),

[
Input( 'button_review' , 'n_clicks' )
],
[
State( 'textarea_review' , 'value' )
]
)
def update_app_ui_2(n_clicks, textarea_value):

    if (n_clicks > 0):
        global response
        response = check_review(textarea_value)
        if (response[0] == 0):
            result = 'The above review is Negative'
            style= {"margin-left": "450px",'width':500, 'height':50,'color':'red'}



        elif (response[0] == 1 ):
            result = 'The above review is Positive'
            style={"margin-left": "450px",'width':500, 'height':50,'color':'green'}



        else:
            result = 'Unknown'
            style== {"margin-left": "500px",'width':150, 'height':50,'background-color':'grey'}

        return result,style

    else:
        return ""

    
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