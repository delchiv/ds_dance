from fpdf import FPDF


def export_to_pdf(dances: list, dancers: list, judges: list):
    """Генерирует PDF-отчёт."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Заголовок
    pdf.cell(200, 10, txt="Результаты турнира", ln=True, align="C")

    # Таблица танцев
    pdf.cell(200, 10, txt="Танцы:", ln=True)
    for dance in dances:
        pdf.cell(200, 10, txt=f"- {dance}", ln=True)

    # Таблица участников
    pdf.cell(200, 10, txt="Участники:", ln=True)
    for dancer in dancers:
        pdf.cell(200, 10, txt=f"- {dancer}", ln=True)

    pdf.output("results.pdf")
