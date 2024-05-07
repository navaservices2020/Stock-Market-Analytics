import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objs as go

# Set the name of the Streamlit app
st.set_page_config(page_title="Motherson Sumi Wiring India")


def main():                
    st.title("Motherson Sumi Wiring India")
    st.subheader("About Company") 
    st.write("Parent organisation : Motherson Sumi Wiring India Limited")
    st.write("MD/CEO : NA")
    st.write("Founded in : NA")
    st.write("NSE symbol : MSUMI")
    st.write("Auto Components")

    st.markdown("---")

    st.subheader("Performance")
    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        todays_low = 67.30
        st.write(f"Today's Low : {todays_low}")

    # Display greeting
    with col2:
        todays_high = 68.95
        st.write(f"Today's High : {todays_high}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        week_52_low = 52.10
        st.write(f"52 Week Low : {week_52_low}")

    # Display greeting
    with col2:
        week_52_high = 74.80
        st.write(f"52 Week High : {week_52_high}")


    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        open = 68.65
        st.write(f"Open : {open}")

    with col2:
        prev_close = 68.65
        st.write(f"Prev. Close : {prev_close}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        volume = 4340356
        st.write(f"Volume : {volume}")

    with col2:
        beta = 0.80
        st.write(f"Beta : {beta}")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        lower_circuit = 54.95
        st.write(f"Lower circuit : {lower_circuit}")

    with col2:
        upper_circuit = 82.35
        st.write(f"Upper circuit : {upper_circuit}")

    # Add line separator
    st.markdown("---")

    st.subheader("Fundamentals")
    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        mkt_cap = 30,435
        st.write(f"Mkt Cap : {mkt_cap} Cr")

    with col2:
        roe = 39.77
        st.write(f"ROE : {roe} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_ratio = 52.15
        st.write(f"P/E Ratio(TTM) : {p_e_ratio}")

    with col2:
        eps = 1.32
        st.write(f"EPS(TTM) : {eps} ")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_b_ratio = 23.12
        st.write(f"P/B Ratio : {p_b_ratio}")

    with col2:
        div_yield = 0.94
        st.write(f"Div Yield : {div_yield} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_industry = 47.20
        st.write(f"Industry P/E : {p_e_industry}")

    with col2:
        book_value = 2.98
        st.write(f"Book Value : {book_value} ")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        d_t_e = 0.21
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
    'Quarter': [ "Dec'22","Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Value': [1688, 1877, 1872, 2110, 2118, 2000]
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
    'Quarter': ["Dec'22","Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Profit Value': [106, 138, 123, 156, 168, 150]
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
    'Year': ["2021", "2022", "2023", "2024"],
    'Revenue Value': [3961, 5665, 7080, 5000]
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
    'Year': ["2021", "2022", "2023", "2024"],
    'Profit Value': [396, 411, 487, 500]
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
    'Year': ["2021", "2022", "2023", "2024"],
    'Net Worth': [710, 1115, 1330, 1500]
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
    'Category': ["Promoters", "Mutual Funds", "Retail", "Foreign Institutions",  "Other Domestic Institutions"],
    'Value': [61.73, 14.28, 11.11, 10.95, 1.93]
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
    'Category': ["Promoters", "Mutual Funds","Foreign Institutions", "Retail",  "Other Domestic Institutions"],
    'Value': [61.73, 14.10, 11.01, 9.94, 3.23]
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
    'Category': ["Promoters","Mutual Funds" ,  "Foreign Institutions","Retail", "Other Domestic Institutions"],
    'Value': [61.74, 13.92, 11.08, 9.41, 3.85]
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
    'Category': ["Promoters","Mutual Funds", "Foreign Institutions", "Retail", "Other Domestic Institutions" ],
    'Value': [61.73, 14.25, 10.91, 9.37, 3.73]
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
    'Value': [61.73,15.32, 9.91, 9.32, 3.71]
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


