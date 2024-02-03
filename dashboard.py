# %%
import plotly
import os
import pandas as pd

cwd = os.getcwd()
print("현재 작업 디렉토리:", cwd
      ,type(cwd))


cwd = cwd.replace('\\','/')
df = pd.read_csv(cwd+'/data/character_info.csv')
print(df.head())

# %%

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# 앱 생성
app = dash.Dash(__name__)

# 레이아웃 정의
app.layout = html.Div([
    dcc.Dropdown(
        id='job-dropdown',
        options=[
            {'label': job, 'value': job} for job in df['job_name'].unique()
        ],
        value=df['job_name'].unique()[0],
        multi=True
    ),
    dcc.Graph(id='histogram')
])

# 콜백 함수 정의
@app.callback(
    Output('histogram', 'figure'),
    Input('job-dropdown', 'value')
)
def update_histogram(selected_jobs):
    filtered_df = df[df['job_name'].isin(selected_jobs)]
    fig = px.histogram(filtered_df, x='fame', nbins=55, title='직업별 명성 분포')
    return fig

# 앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)

# %%
