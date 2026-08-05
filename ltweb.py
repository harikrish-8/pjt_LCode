import streamlit as st
from namelist import get_leaderboard
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO

st.set_page_config(page_title="LeetTracker", page_icon="🏆", layout="wide")

st.title("🐍 LeetTracker Leaderboard")

df = get_leaderboard()

st.dataframe(df, use_container_width=True, hide_index=True)


# -------- PDF Generator --------
def create_pdf(dataframe):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    data = [list(dataframe.columns)] + dataframe.values.tolist()

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ]))

    doc.build([table])

    pdf = buffer.getvalue()
    buffer.close()

    return pdf


pdf = create_pdf(df)

st.download_button(
    label="📄 Download Leaderboard PDF",
    data=pdf,
    file_name="LeetTracker_Leaderboard.pdf",
    mime="application/pdf"
)