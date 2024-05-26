from cx_Freeze import setup, Executable

setup(
    name="Mona Technology Menu d'extinction windows xp",
    version="1.0.0",
    description="Mona Technology Menu d'extinction windows xp est une application inspirée du menu d'arrêt, de redémarrage et de mise en veille de Windows XP. Il offre une interface conviviale et familière pour les utilisateurs, reproduisant fidèlement l'apparence et la fonctionnalité du menu classique de Windows XP.Cette application permet aux utilisateurs de rapidement et facilement éteindre, redémarrer ou mettre en veille leur système Windows, en conservant le charme rétro du célèbre système d'exploitation de Microsoft.Avec son design nostalgique et son utilisation simple, le Mona Technology Menu d'extinction windows xp offre une expérience utilisateur familière tout en ajoutant une touche de modernité grâce à sa compatibilité avec les systèmes d'exploitation actuels.",
    executables=[Executable("main.py", icon="assets/favicon.ico")],
    options={
        "build_exe": {
            "includes": [],  # Liste des modules à inclure
            "include_files": ["assets"]  # Liste des fichiers/dossiers à inclure
        }
    }
)

