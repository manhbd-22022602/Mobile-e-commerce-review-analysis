from data_loader import clean_n_tokenize_data
from vectorizer import W2VLoader
from model import SVCModel
import gradio as gr
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib

#load model
svm_Pin = joblib.load('pretrained_svm/bestModelPin')
svm_Service = joblib.load('pretrained_svm/bestModelService')
svm_General = joblib.load('pretrained_svm/bestModelGeneral')
svm_Others = joblib.load('pretrained_svm/bestModelOthers')

svm_SPin = joblib.load('pretrained_svm/bestModelSPin')
svm_SSer = joblib.load('pretrained_svm/bestModelSSer')
svm_SGeneral = joblib.load('pretrained_svm/bestModelSGeneral')
svm_SOth = joblib.load('pretrained_svm/bestModelSOth')

w2v_300dims = W2VLoader(
    w2v_path='phow2v/word2vec_vi_words_300dims.txt'
)

#demo
aspects = ['Pin', 'Service', 'General', 'Others']
aspects_ratio = []

sentiments = ['Positive', 'Negative', 'Neutral']
sentiments_ratio = []

def sentiment_analysis(sent):
    token_sent = clean_n_tokenize_data(sent, w2v_300dims).reshape(1, -1)

    pin_prob = svm_Pin.predict_proba(token_sent).ravel()
    service_prob = svm_Service.predict_proba(token_sent).ravel()
    general_prob = svm_General.predict_proba(token_sent).ravel()
    others_prob = svm_Others.predict_proba(token_sent).ravel()

    spin_prob = svm_SPin.predict_proba(token_sent).ravel()
    sser_prob = svm_SSer.predict_proba(token_sent).ravel()
    sgen_prob = svm_SGeneral.predict_proba(token_sent).ravel()
    soth_prob = svm_SOth.predict_proba(token_sent).ravel()

    aspects_ratio.clear()
    sentiments_ratio.clear()
    aspects_ratio.extend([pin_prob, service_prob, general_prob, others_prob])
    sentiments_ratio.extend([spin_prob, sser_prob, sgen_prob, soth_prob])

def draw_bar_aspect():
    # Tạo list chứa các thanh bar
    bars = []

    # Vẽ từng thanh bar cho mỗi khía cạnh
    for i in range(len(aspects)):
        bars.append(go.Bar(
            y=[aspects[i]],
            x=[aspects_ratio[i][0]],
            orientation='h',
            name='Không',
            showlegend=True if i == 0 else False,
            marker=dict(color='orange')
        ))
        bars.append(go.Bar(
            y=[aspects[i]],
            x=[aspects_ratio[i][1]],
            orientation='h',
            name='Có',
            showlegend=True if i == 0 else False,
            marker=dict(color='blue')
        ))

    # Tạo layout
    layout = go.Layout(
        title='Aspects',
        barmode='stack',
        xaxis=dict(title='Ratio'),
        yaxis=dict(title='Aspects')
    )

    # Tạo figure
    fig = go.Figure(data=bars, layout=layout)

    return fig

def draw_bar_sentiment():
    bars = []

    # Vẽ từng thanh bar cảm xúc cho mỗi khía cạnh
    for i in range(len(aspects)):
        bars.append(go.Bar(
            y=[aspects[i]],
            x=[sentiments_ratio[i][0]],
            orientation='h',
            name='Negative',
            showlegend=True if i == 0 else False,
            marker=dict(color='red')
        ))
        bars.append(go.Bar(
            y=[aspects[i]],
            x=[sentiments_ratio[i][1]],
            orientation='h',
            name='Neutral',
            showlegend=True if i == 0 else False,
            marker=dict(color='orange')
        ))
        bars.append(go.Bar(
            y=[aspects[i]],
            x=[sentiments_ratio[i][2]],
            orientation='h',
            name='Positive',
            showlegend=True if i == 0 else False,
            marker=dict(color='green')
        ))


    # Tạo layout
    layout = go.Layout(
        title='Sentiments of Aspects',
        barmode='stack',
        xaxis=dict(title='Ratio'),
        yaxis=dict(title='Aspects')
    )

    # Tạo figure
    fig = go.Figure(data=bars, layout=layout)

    return fig

def draw_pie_aspect():
    # Tạo subplot với loại 'pie' và khoảng trống
    fig = make_subplots(rows=1, cols=4, subplot_titles=aspects, horizontal_spacing=0.05, specs=[[{'type':'pie'}]*4])

    # Vẽ biểu đồ pie cho mỗi khía cạnh
    for i, aspect in enumerate(aspects):
        labels = ['Không', 'Có']
        values = aspects_ratio[i]
        
        # Tạo biểu đồ pie và thêm vào subplot tương ứng
        fig.add_trace(go.Pie(labels=labels, values=values, name=aspect), row=1, col=i+1)

    # Cài đặt layout
    fig.update_layout(
        title='Aspect',
    )
    return fig

def draw_pie_sentiment():
    # Tạo subplot với loại 'pie' và khoảng trống
    fig = make_subplots(rows=1, cols=4, subplot_titles=aspects, horizontal_spacing=0.05, specs=[[{'type':'pie'}]*4])

    # Vẽ biểu đồ pie cho mỗi khía cạnh
    for i, aspect in enumerate(aspects):
        labels = sentiments
        values = [sentiments_ratio[i][2], sentiments_ratio[i][1], sentiments_ratio[i][0]] 
        
        # Tạo biểu đồ pie và thêm vào subplot tương ứng
        fig.add_trace(go.Pie(labels=labels, values=values, name=aspect), row=1, col=i+1)

    # Cài đặt layout
    fig.update_layout(
        title='Sentiment Analysis by Aspect',
    )
    return fig

def draw_plot_aspect(type_plot):
    if type_plot == 'Bar':
        return draw_bar_aspect()
    else:
        return draw_pie_aspect()
    
def draw_plot_sentiment(type_plot):
    if type_plot == 'Bar':
        return draw_bar_sentiment()
    else:
        return draw_pie_sentiment()

def draw_plot(type_aspect_plot, type_sentiment_plot):
    return draw_plot_aspect(type_aspect_plot), draw_plot_sentiment(type_sentiment_plot)

def submit(comment, type_aspect_plot, type_sentiment_plot):
    sentiment_analysis(comment)
    plot = draw_plot(type_aspect_plot, type_sentiment_plot)
    return {
        output_plot1: gr.Column(visible=True),
        plot_aspect: plot[0],
        plot_sentiment: plot[1],
    }
    

with gr.Blocks() as demo:
    with gr.Row():
        text_box = gr.Textbox(placeholder="Write your comment here...", visible=True, label="Comment")
        submit_btn = gr.Button(value="Submit")
    with gr.Row(visible=False) as output_plot1:
        with gr.Column():
            choose_plot_aspect_dropdown = gr.Dropdown(
                    choices=['Bar', 'Pie'], 
                    label="Choose Plot Type",
                    value='Bar',
                    )
            plot_aspect = gr.Plot()
        with gr.Column():
            choose_plot_sentiment_dropdown = gr.Dropdown(
                    choices=['Bar', 'Pie'], 
                    label="Choose Plot Type",
                    value='Pie',
                    )
            plot_sentiment = gr.Plot() 

    choose_plot_aspect_dropdown.select(
            fn = draw_plot_aspect,
            inputs = [choose_plot_aspect_dropdown],
            outputs = [plot_aspect],
        )
    choose_plot_sentiment_dropdown.select(
            fn = draw_plot_sentiment,
            inputs = [choose_plot_sentiment_dropdown],
            outputs = [plot_sentiment],
        )

    submit_btn.click(
    fn = submit,
    inputs = [text_box, choose_plot_aspect_dropdown, choose_plot_sentiment_dropdown],
    outputs = [output_plot1, plot_aspect, plot_sentiment],
)
    
def main():
    return demo.launch(share=True)

if __name__ == '__main__':
    main()