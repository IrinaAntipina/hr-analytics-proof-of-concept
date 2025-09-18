import pandas as pd
import matplotlib.pyplot as plt
from conn_warehouse import get_job_list

def occupation_chart(table="mart_main"):
    df = get_job_list(query=f"""
                            SELECT 
                                occupation,
                                sum(vacancies) as total_vacancies
                            FROM
                                {table}
                            GROUP BY occupation
                            ORDER BY total_vacancies DESC
                            LIMIT 10
                            """)
    
    fig, ax = plt.subplots(1)

    ax.barh(df["OCCUPATION"], df["TOTAL_VACANCIES"], color="#b07cf4")
    ax.invert_yaxis()

    ax.set_xlabel("Antal lediga jobb")
    ax.set_ylabel("")
   
    ax.text(
    x=-0.25,
    y=1.02,
    s="Yrkesområde",
    transform=ax.transAxes,
    ha="left",
    va="bottom",
    fontsize=10,
    )

    ax.yaxis.get_ticklabels(False)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    
    ax.tick_params(axis='y', which='both', length=0)
    ax.tick_params(axis='x', which='both', length=0)
    
    for i, v in enumerate(df["TOTAL_VACANCIES"]):
        ax.text(v + 5, i, str(v), va='center', fontsize=10)
    
    fig.tight_layout()


    return fig

if __name__ == "__main__":
    occupation_chart()