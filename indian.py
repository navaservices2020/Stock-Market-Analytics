import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objs as go

# Set the name of the Streamlit app
st.set_page_config(page_title="Indian Hotels Company")


def main():                
    st.title("Indian Hotels Company")
    st.subheader("About Company") 
    st.write("Parent organisation : The Indian Hotels Company Limited")
    st.write("MD/CEO : Mr. Puneet Chhatwal")
    st.write("Founded in : NA")
    st.write("NSE symbol : INDHOTEL")

    st.markdown("---")

    st.subheader("Performance")
    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        todays_low = 565.15
        st.write(f"Today's Low : {todays_low}")

    # Display greeting
    with col2:
        todays_high = 581
        st.write(f"Today's High : {todays_high}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        week_52_low = 350.50
        st.write(f"52 Week Low : {week_52_low}")

    # Display greeting
    with col2:
        week_52_high = 622.50
        st.write(f"52 Week High : {week_52_high}")


    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        open = 579.75
        st.write(f"Open : {open}")

    with col2:
        prev_close = 576.15
        st.write(f"Prev. Close : {prev_close}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        volume = 2071931
        st.write(f"Volume : {volume}")

    with col2:
        beta = 0.97
        st.write(f"Beta : {beta}")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        lower_circuit = 514.20
        st.write(f"Lower circuit : {lower_circuit}")

    with col2:
        upper_circuit = 628.40
        st.write(f"Upper circuit : {upper_circuit}")

    # Add line separator
    st.markdown("---")

    st.subheader("Fundamentals")
    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        mkt_cap = 81,983
        st.write(f"Mkt Cap : {mkt_cap} Cr")

    with col2:
        roe = 13.31
        st.write(f"ROE : {roe} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_ratio = 65.08
        st.write(f"P/E Ratio(TTM) : {p_e_ratio}")

    with col2:
        eps = 8.85
        st.write(f"EPS(TTM) : {eps} ")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_b_ratio = 8.67
        st.write(f"P/B Ratio : {p_b_ratio}")

    with col2:
        div_yield = 0.30
        st.write(f"Div Yield : {div_yield} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_industry = 60.93
        st.write(f"Industry P/E : {p_e_industry}")

    with col2:
        book_value = 66.44
        st.write(f"Book Value : {book_value} ")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        d_t_e = 0.29
        st.write(f"Debt to Equity : {d_t_e}")

    with col2:
        face_value = 1
        st.write(f"Face Value : {face_value} ")

    st.markdown("---")

    st.subheader("Financials")
    # Add tabs to the main content area
    tabs = st.selectbox(
    "Choose a tab:",
    ["Quarterly", "Yearly"]
)

# Display content based on selected tab
    if tabs == "Quarterly":
        st.write("## Quarterly Revenue")

        data = {
    'Quarter': ["Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Value': [1655, 1516, 1481, 2004, 1951]
}
        df = pd.DataFrame(data)

# Display the DataFrame
        st.write("Data:")
        st.write(df)

# Create a Plotly bar chart
        fig = go.Figure(data=[
        go.Bar(
        x=df['Quarter'],
        y=df['Value'],
        text=df['Value'],  # values displayed on top of bars
        textposition='auto'  # automatic positioning of text
    )
])

# Update layout
        fig.update_layout(
    title="Quarterly Revenue with Values",
    xaxis_title="Quarter",
    yaxis_title="Value in crore"
)

# Display the Plotly chart
        st.plotly_chart(fig)

        st.markdown("---")
        st.write("## Quarterly Profit")

        data = {
    'Quarter': ["Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Profit Value': [302, 211, 160, 438, 393]
}
        df = pd.DataFrame(data)

# Display the DataFrame
        st.write("Data:")
        st.write(df)

# Create a Plotly bar chart
        fig = go.Figure(data=[
    go.Bar(
        x=df['Quarter'],
        y=df['Profit Value'],
        text=df['Profit Value'],  # values displayed on top of bars
        textposition='auto'  # automatic positioning of text
    )
])

# Update layout
        fig.update_layout(
    title="Quarterly Profit with Values",
    xaxis_title="Quarter",
    yaxis_title="Profit in crore"
)

# Display the Plotly chart
        st.plotly_chart(fig)
    
        st.markdown("---")
    


    elif tabs == "Yearly":
        st.write("## Yearly Revenue")

        data = {
    'Year': ["2019", "2020","2021", "2022", "2023", "2024"],
    'Revenue Value': [4595, 4596, 1740, 3211, 5949, 6000]
}
        df = pd.DataFrame(data)

# Display the DataFrame
        st.write("Data:")
        st.write(df)

# Create a Plotly bar chart
        fig = go.Figure(data=[
        go.Bar(
        x=df['Year'],
        y=df['Revenue Value'],
        text=df['Revenue Value'],  # values displayed on top of bars
        textposition='auto'  # automatic positioning of text
    )
])

# Update layout
        fig.update_layout(
        title="Yearly Revenue with Values",
        xaxis_title="Year",
    yaxis_title="Revenue Value in crore"
)

# Display the Plotly chart
        st.plotly_chart(fig)

        st.markdown("---")


        st.write("## Yearly Profit")

        data = {
    'Year': ["2019", "2020","2021", "2022", "2023", "2024"],
    'Profit Value': [245, 351, -694, -222, 971, 500]
}
        df = pd.DataFrame(data)

# Display the DataFrame
        st.write("Data:")
        st.write(df)

# Create a Plotly bar chart
        fig = go.Figure(data=[
    go.Bar(
        x=df['Year'],
        y=df['Profit Value'],
        text=df['Profit Value'],  # values displayed on top of bars
        textposition='auto'  # automatic positioning of text
    )
])

# Update layout
        fig.update_layout(
    title="Yearly Profit with Values",
    xaxis_title="Year",
    yaxis_title="Profit in crore"
)

# Display the Plotly chart
        st.plotly_chart(fig)
    
        st.markdown("---")

        st.write("## Yearly Net Worth")

        data = {
    'Year': ["2019", "2020","2021", "2022", "2023", "2024"],
    'Net Worth': [5148, 5122, 4283, 7655, 8642, 5000]
}
        df = pd.DataFrame(data)

# Display the DataFrame
        st.write("Data:")
        st.write(df)

# Create a Plotly bar chart
        fig = go.Figure(data=[
    go.Bar(
        x=df['Year'],
        y=df['Net Worth'],
        text=df['Net Worth'],  # values displayed on top of bars
        textposition='auto'  # automatic positioning of text
    )
])

# Update layout
        fig.update_layout(
    title="Yearly Net Worth with Values",
    xaxis_title="Year",
    yaxis_title="Net Worth in crore"
)

# Display the Plotly charts
        st.plotly_chart(fig)
    
        st.markdown("---")
        st.write("## Shareholding pattern")

    # Add tabs to the main content area
    tabs = st.selectbox(
    "Choose a Quarter:",
    ["Mar'24", "Dec'23", "Sep'23", "Jun'23", "Mar'23"]
)

# Display content based on selected tab
    if tabs == "Mar'24":
        st.write("Shareholding pattern Mar'24")
        

# Sample data
        data = {
    'Category': ["Promoters", "Foreign Institutions", "Retail", "Mutual Funds", "Other Domestic Institutions"],
    'Value': [38.12, 24.47, 16.63, 15.92, 4.86]
}
        df = pd.DataFrame(data)

# Function to create pie chart
        def create_pie_chart(data):
            fig = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
            fig.update_layout(title="Pie Chart")
            return fig
        
        st.plotly_chart(create_pie_chart(df))

    elif tabs == "Dec'23":
        st.write("Shareholding pattern Dec'23")
        

# Sample data 
        data = {
    'Category': ["Promoters", "Foreign Institutions", "Retail", "Mutual Funds", "Other Domestic Institutions"],
    'Value': [38.12, 23.28, 17.16, 16.78, 4.67]
}
        df = pd.DataFrame(data)

# Function to create pie chart
        def create_pie_chart(data):
            fig = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
            fig.update_layout(title="Pie Chart")
            return fig
        
        st.plotly_chart(create_pie_chart(df))

    elif tabs == "Sep'23":
        st.write("Shareholding pattern Sep'23")
        

# Sample data
        data = {
    'Category': ["Promoters", "Foreign Institutions","Mutual Funds" , "Retail", "Other Domestic Institutions"],
    'Value': [38.19, 22.17, 18.16, 16.38, 5.10]
}
        df = pd.DataFrame(data)

# Function to create pie chart
        def create_pie_chart(data):
            fig = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
            fig.update_layout(title="Pie Chart")
            return fig
        
        st.plotly_chart(create_pie_chart(df))
       

    elif tabs == "Jun'23":
        st.write("Shareholding pattern Jun'23")
        

# Sample data
        data = {
    'Category': ["Promoters","Foreign Institutions","Mutual Funds", "Retail", "Other Domestic Institutions" ],
    'Value': [38.19, 21.64, 19.27, 15.98, 4.92]
}
        df = pd.DataFrame(data)

# Function to create pie chart
        def create_pie_chart(data):
            fig = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
            fig.update_layout(title="Pie Chart")
            return fig
        
        st.plotly_chart(create_pie_chart(df))
        

    elif tabs == "Mar'23":
        st.write("Shareholding pattern Mar'23")
        

# Sample data
        data = {
    'Category': ["Promoters","Mutual Funds", "Foreign Institutions","Retail",  "Other Domestic Institutions"],
    'Value': [38.19,22.29,18.24,16.29,5.00]
}
        df = pd.DataFrame(data)

# Function to create pie chart
        def create_pie_chart(data):
            fig = go.Figure(data=[go.Pie(labels=data['Category'], values=data['Value'])])
            fig.update_layout(title="Pie Chart")
            return fig
        
        st.plotly_chart(create_pie_chart(df))
        

if __name__ == "__main__":
    main()


