from fpdf import FPDF
from datetime import datetime
from pathlib import Path
import os

def pedir_asistentes():
    print("\n🔹 Lista de asistencia:")
    nombres = input("Escribe los nombres separados por comas: ")
    asistentes = [n.strip() for n in nombres.split(",") if n.strip()]
    return asistentes

def pedir_temas():
    print("\n🔹 Temas tratados:")
    tratados = input("→ ")

    print("\n🔹 Temas para la próxima sesión:")
    pendientes = input("→ ")

    return tratados, pendientes

def pedir_foto():
    print("\n🔹 Foto de la reunión (opcional)")
    ruta = input("Escribe la ruta de la imagen (o deja vacío si no hay): ").strip()
    return ruta if os.path.exists(ruta) else None

def generar_pdf(asistentes, tratados, pendientes, ruta_imagen):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="ACTA DE REUNIÓN", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Asistentes:", ln=True)
    for a in asistentes:
        pdf.cell(200, 10, txt=f"- {a}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt="Temas tratados:", ln=True)
    pdf.multi_cell(0, 10, tratados)

    pdf.ln(5)
    pdf.cell(200, 10, txt="Temas para la próxima sesión:", ln=True)
    pdf.multi_cell(0, 10, pendientes)

    if ruta_imagen:
        try:
            pdf.image(ruta_imagen, x=10, y=pdf.get_y() + 10, w=100)
        except Exception as e:
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"(Error al cargar imagen: {e})", ln=True)

    # Guardar en Documentos/Informes de reunion
    carpeta_docs = Path.home() / "Documents" / "Informes de reunion"
    carpeta_docs.mkdir(parents=True, exist_ok=True)
    nombre_pdf = carpeta_docs / f"acta_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(str(nombre_pdf))

    print(f"\n✅ PDF generado correctamente en:\n{nombre_pdf}")

def chatbot():
    print("🧠 Bienvenido al ChatBot de Asistencia\n")

    asistentes = pedir_asistentes()
    tratados, pendientes = pedir_temas()
    ruta_imagen = pedir_foto()

    generar_pdf(asistentes, tratados, pendientes, ruta_imagen)

if __name__ == "__main__":
    chatbot()
