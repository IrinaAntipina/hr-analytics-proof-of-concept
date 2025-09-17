





fig_exp = px.pie(
        values=exp.values, 
        names=['Required' if x else 'Not required' for x in exp.index], 
        title="",
        hole=0.5,  # Donut style
        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    )
    
fig_exp.update_traces(
    textposition='inside', 
    textinfo='percent+label',
    textfont_size=12,
    marker=dict(line=dict(color='#FFFFFF', width=3))
)

fig_exp.update_layout(
    height=280,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.05,
        font=dict(size=11)
    ),
    font=dict(family="Arial", size=11),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_exp, use_container_width=True)