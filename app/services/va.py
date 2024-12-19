import json
from datetime import date


def achats(debut: date = date.min, fin: date = date.max, id_projet: int = None):
    with open("app/assets/mock/achats.json") as f:
        achats = json.load(f)

    return [
        achat
        for achat in achats
        if debut <= date.fromisoformat(achat["date"]) <= fin
        and (id_projet is None or achat["id_projet"] == id_projet)
    ]


def ventes(debut: date = date.min, fin: date = date.max, id_projet: int = None):
    with open("app/assets/mock/ventes.json") as f:
        ventes = json.load(f)

    return [
        vente
        for vente in ventes
        if debut <= date.fromisoformat(vente["date"]) <= fin
        and (id_projet is None or vente["id_projet"] == id_projet)
    ]
