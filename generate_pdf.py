from PIL import Image, ImageDraw, ImageFont

# Charger l'image du plan
image = Image.open("Plan.png")
draw = ImageDraw.Draw(image)

# Exemple d'assignation
assignations = {
    "A1": {"ecole": "École Alpha", "niveau": "Primaire", "couleur": (255, 0, 0)},
    "A2": {"ecole": "École Beta", "niveau": "Secondaire", "couleur": (0, 128, 0)},
    "B1": {"ecole": "École Gamma", "niveau": "Collège", "couleur": (0, 0, 255)}
}

# Police pour annotation
font = ImageFont.load_default()

# Position fictive des sièges
positions = {
    "A1": (100, 100),
    "A2": (150, 100),
    "B1": (100, 150)
}

# Annoter l'image
for seat, info in assignations.items():
    x, y = positions[seat]
    draw.rectangle([x-15, y-15, x+15, y+15], fill=info["couleur"])
    draw.text((x-20, y+20), f"{info['ecole']} ({info['niveau']})", fill="black", font=font)

# Sauvegarder l'image annotée
image.save("assignation_tool/annotated_plan.png")

# Générer le PDF
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("assignation_tool/annotated_plan.png", x=10, y=10, w=180)
pdf.output("assignation_tool/plan_annoté.pdf")
