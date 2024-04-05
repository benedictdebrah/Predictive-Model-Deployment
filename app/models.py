from pydantic import BaseModel

class Item(BaseModel):
    wine_type: str
    alcohol: float
    citric_acid: float
    density: float
    ph: float
    residual_sugar: float
    total_sulfur_dioxide: float
    fixed_acidity: float
