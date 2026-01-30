import numpy as np
import plotly.graph_objects as go

aoi_deg = np.linspace(0, 90, 100)
aoi = np.deg2rad(aoi_deg)

# Optical constants for silver at 0.88 um from refractiveindex.info
# using data from Jiang et al. 2016 (https://doi.org/10.1038/srep30605)
n_silver = 0.10400
k_silver = 5.8570

silver = complex(n_silver, k_silver)

air = 1.0

r_s = air * np.cos(aoi) - silver * np.sqrt(1 - (air / silver * np.sin(aoi))**2)
r_s /= air * np.cos(aoi) + silver * np.sqrt(1 - (air / silver * np.sin(aoi))**2)

r_p = - silver * np.cos(aoi) + air * np.sqrt(1 - (air / silver * np.sin(aoi))**2)
r_p /= silver * np.cos(aoi) + air * np.sqrt(1 - (air / silver * np.sin(aoi))**2)

phi_r_s_deg = np.rad2deg(np.angle(r_s))
phi_r_p_deg = np.rad2deg(np.angle(r_p))

phi_r_s_45_deg = np.interp(45, aoi_deg, phi_r_s_deg)
phi_r_p_45_deg = np.interp(45, aoi_deg, phi_r_p_deg)

fig = go.Figure()
fig.add_trace(go.Scatter(x=aoi_deg, y=phi_r_p_deg,
                         mode='lines',
                         name='<i>&#966;</i><sub><i>p</i>-pol</sub>',
                         line=dict(color='#0072B2')
))
fig.add_trace(go.Scatter(x=aoi_deg, y=phi_r_s_deg,
                         mode='lines',
                         name='<i>&#966;</i><sub><i>s</i>-pol</sub>',
                         line=dict(color='#D55E00')
))
fig.add_trace(go.Scatter(x=[45, 45], y=[phi_r_s_45_deg, phi_r_p_45_deg],
                         mode='lines',
                         line=dict(color='black', dash='dot'),
                         showlegend=False
))
fig.add_annotation(
    x=45,
    y=np.max((phi_r_p_45_deg, phi_r_s_45_deg))+1,
    text='<i>&#916;&#966;</i> = %.1f&#186;' % abs(phi_r_p_45_deg - phi_r_s_45_deg),
    font=dict(
        family='crm12',
        size=20
    ),
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    ax=-20,
    ay=-40
)
fig.update_xaxes(
    title_text='Angle of incidence (deg)',
    title_font=dict(size=20),
    showgrid=True,
    automargin=False,
    tickfont=dict(size=16),
    tickmode='array',
    tickvals=[0, 15, 30, 45, 60, 75, 90],
    range=[0, 90]
)
fig.update_yaxes(
    title_text='Phase (deg)',
    title_standoff=20,
    title_font=dict(size=20),
    showgrid=True,
    automargin=False,
    tickfont=dict(size=16),
    tickvals=[0, -30, -60, -90, -120, -150, -180],
    range=[-180, 0]    
)
fig.update_layout(
    width=500,
    height=400,
    margin=dict(l=70, r=50, t=50, b=70),
    template='simple_white',
    font_family='crm12',
    legend=dict(
        font=dict(size=20),
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)
fig.show()
fig.write_image(r'fresnel_silver.pdf', width=500, height=400)
