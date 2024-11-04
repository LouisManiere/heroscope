import random

def get_fortune():
    """Return a random fortune for super hero"""
    return random.choice([
        "Votre courage et votre détermination vous mèneront vers une nouvelle mission risquée. Un puissant allié pourrait se manifester, mais gardez votre sang-froid, car même un héros doit parfois tempérer son feu intérieur",
        "Vous êtes sur le point de découvrir un secret qui pourrait changer le cours de l'histoire. Restez vigilant et ne faites confiance à personne, car les ennemis sont partout. Votre force intérieure vous guidera vers la vérité",
        "Un mystérieux artefact pourrait bientôt croiser votre chemin. Soyez prudent, car il pourrait s'agir d'une arme redoutable. Votre intelligence et votre ruse seront vos meilleurs atouts pour déjouer les plans de vos ennemis",
        "Une nouvelle menace plane sur la ville, et vous seul pouvez l'arrêter. Votre sens du devoir et votre loyauté envers vos amis vous permettront de triompher. N'oubliez pas que même les plus grands héros ont parfois besoin d'aide",
        "Un ancien ennemi refait surface, et cette fois-ci, il est plus puissant que jamais. Vous devrez faire preuve de courage et de détermination pour le vaincre. N'oubliez pas que la véritable force réside dans votre cœur, pas dans vos pouvoirs",
        "Une nouvelle aventure vous attend, et elle pourrait vous emmener aux confins de l'univers. Restez ouvert d'esprit et prêt à affronter l'inconnu. Votre curiosité et votre soif de justice vous guideront vers la victoire"
    ])

def zodiaque():
    return random.choice([
        "Bélier",
        "Taureau",
        "Gémeaux",
        "Cancer",
        "Lion",
        "Vierge",
        "Balance",
        "Scorpion",
        "Sagittaire",
        "Capricorne",
        "Verseau",
        "Poissons"
    ])

test