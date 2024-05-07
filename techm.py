import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objs as go



# Set the name of the Streamlit app
st.set_page_config(page_title="Tech Mahindra")


def main():                
    st.title("Tech Mahindra")
    st.subheader("About Company") 
    st.write("Parent organisation : Tech Mahindra Limited")
    st.write("MD/CEO : Mr. Mohit Joshi")
    st.write("Founded in : NA")
    st.write("NSE symbol : TECHM")

    st.markdown("---")

    st.subheader("Performance")
    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        todays_low = 1243.05
        st.write(f"Today's Low : {todays_low}")

    # Display greeting
    with col2:
        todays_high = 1272
        st.write(f"Today's High : {todays_high}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        week_52_low = 1028.85
        st.write(f"52 Week Low : {week_52_low}")

    # Display greeting
    with col2:
        week_52_high = 1416.30
        st.write(f"52 Week High : {week_52_high}")


    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        open = 1270
        st.write(f"Open : {open}")

    with col2:
        prev_close = 1266.90
        st.write(f"Prev. Close : {prev_close}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        volume = 2322455
        st.write(f"Volume : {volume}")

    with col2:
        beta = 1.15
        st.write(f"Beta : {beta}")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        lower_circuit = 1140.25
        st.write(f"Lower circuit : {lower_circuit}")

    with col2:
        upper_circuit = 1393.55
        st.write(f"Upper circuit : {upper_circuit}")

    # Add line separator
    st.markdown("---")

    st.subheader("Fundamentals")
    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        mkt_cap = 1,23,751
        st.write(f"Mkt Cap : {mkt_cap} Cr")

    with col2:
        roe = 8.84
        st.write(f"ROE : {roe} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_ratio = 52.48
        st.write(f"P/E Ratio(TTM) : {p_e_ratio}")

    with col2:
        eps = 24.14
        st.write(f"EPS(TTM) : {eps} ")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_b_ratio = 4.63
        st.write(f"P/B Ratio : {p_b_ratio}")

    with col2:
        div_yield = 2.85
        st.write(f"Div Yield : {div_yield} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_industry = 28.02
        st.write(f"Industry P/E : {p_e_industry}")

    with col2:
        book_value = 273.51
        st.write(f"Book Value : {book_value} ")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        d_t_e = 0.10
        st.write(f"Debt to Equity : {d_t_e}")

    with col2:
        face_value = 5
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
    'Value': [14024, 13351, 13128, 13189, 13245]
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
    'Profit Value': [1125, 704, 505, 524, 664]
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
    'Revenue Value': [35276, 38060, 38642, 45758, 54255, 60000]
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
    'Profit Value': [4289, 3897, 4353, 5630, 4857, 5000]
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
    'Net Worth': [20762, 22206, 25244, 27381, 28395, 50000]
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

# Display the Plotly chart
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
    'Category': ["Promoters", "Foreign Institutions", "Other Domestic Institutions", "Mutual Funds", "Retail"],
    'Value': [35.09, 24.15, 15.52, 14.00, 11.24]
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
    'Category': ["Promoters", "Foreign Institutions", "Other Domestic Institutions", "Mutual Funds", "Retail"],
    'Value': [35.11, 24.58, 14.78, 14.24, 11.30]
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
    'Category': ["Promoters", "Foreign Institutions", "Other Domestic Institutions", "Retail", "Mutual Funds"],
    'Value': [35.13, 26.22, 13.20, 13.09, 12.36]
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
    'Category': ["Promoters","Foreign Institutions", "Other Domestic Institutions", "Mutual Funds", "Retail" ],
    'Value': [35.16, 25.68, 14.13, 12.83, 12.20]
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
    'Category': ["Promoters","Foreign Institutions", "Mutual Funds",  "Other Domestic Institutions", "Retail"],
    'Value': [35.18, 26.87, 12.93, 12.92, 12.10]
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


