import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objs as go



# Set the name of the Streamlit app
st.set_page_config(page_title="Mahindra & Mahindra")


def main():
    st.title("Mahindra & Mahindra")
    st.subheader("About Company")
    st.write("Parent organisation : Mahindra And Mahindra")
    st.write("MD/CEO : Dr. Anish Shah")
    st.write("Founded in : NA")
    st.write("NSE symbol : M&M")

    st.markdown("---")

    st.subheader("Performance")
    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        todays_low = 2165.10
        st.write(f"Today's Low : {todays_low}")

    # Display greeting
    with col2:
        todays_high = 2204.00
        st.write(f"Today's High : {todays_high}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        week_52_low = 1208.05
        st.write(f"52 Week Low : {week_52_low}")

    # Display greeting
    with col2:
        week_52_high = 2204.00
        st.write(f"52 Week High : {week_52_high}")


    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        open = 2165.10
        st.write(f"Open : {open}")

    with col2:
        prev_close = 2165.35
        st.write(f"Prev. Close : {prev_close}")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        volume = 2122282
        st.write(f"Volume : {volume}")

    with col2:
        beta = 1.15
        st.write(f"Beta : {beta}")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        lower_circuit = 1940.75
        st.write(f"Lower circuit : {lower_circuit}")

    with col2:
        upper_circuit = 2371.95
        st.write(f"Upper circuit : {upper_circuit}")

    # Add line separator
    st.markdown("---")

    st.subheader("Fundamentals")
    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        mkt_cap = 2,68,142
        st.write(f"Mkt Cap : {mkt_cap} Cr")

    with col2:
        roe = 18.47
        st.write(f"ROE : {roe} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_ratio = 24.05
        st.write(f"P/E Ratio(TTM) : {p_e_ratio}")

    with col2:
        eps = 89.67
        st.write(f"EPS(TTM) : {eps} ")

    # Create three columns
    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_b_ratio = 4.43
        st.write(f"P/B Ratio : {p_b_ratio}")

    with col2:
        div_yield = 0.73
        st.write(f"Div Yield : {div_yield} %")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        p_e_industry = 26.39
        st.write(f"Industry P/E : {p_e_industry}")

    with col2:
        book_value = 486.93
        st.write(f"Book Value : {book_value} ")

    col1, col2 = st.columns([1, 2])

    # Get user input
    with col1:
        d_t_e = 1.65
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
    'Quarter': ["Dec'22", "Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Value': [30920, 32850, 34699, 35027, 35810, 50000]
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
    'Quarter': ["Dec'22", "Mar'23","Jun'23", "Sep'23", "Dec'23", "Mar'24"],
    'Profit Value': [2994, 2998, 3684, 2484, 2977, 5000]
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
    'Revenue Value': [105806, 76411, 75311, 91105, 122475, 100000]
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
    'Profit Value': [6017, 2713, 3702, 7253, 11374, 10000]
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
    'Net Worth': [48344, 47661, 50652, 56825, 67082, 50000]
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
    'Category': ["Foreign Institutions", "Promoters", "Retail", "Other Domestic Institutions", "Mutual Funds"],
    'Value': [41.75, 18.59, 13.53, 13.40, 12.72]
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
    'Category': ["Foreign Institutions", "Promoters", "Retail", "Other Domestic Institutions", "Mutual Funds"],
    'Value': [40.87, 19.32, 13.55, 13.21, 13.06]
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
    'Category': ["Foreign Institutions", "Promoters","Mutual Funds", "Retail", "Other Domestic Institutions"],
    'Value': [40.26, 19.34, 13.73, 13.62, 13.06]
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
    'Category': ["Foreign Institutions", "Promoters","Mutual Funds", "Retail", "Other Domestic Institutions" ],
    'Value': [40.14, 19.37, 13.94, 13.62, 12.94]
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
    'Category': ["Foreign Institutions", "Promoters","Mutual Funds", "Retail", "Other Domestic Institutions" ],
    'Value': [39.24, 19.37, 15.06, 13.74, 12.60]
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


