# Welcome to GitHub Desktop!

Bonjour ou Bonsoir à tous...
Dans ce fichier README.md, écrivez toutes vos modifications avant un émminent commit
***`Premièrement parlons des modifications obligatoires`***
    -Configurer d'un environnement virtuel (virtualenv)
        [Watch the video](https://youtu.be/u5yIQe8o2zU?si=13XoSHB60Kbr5eT9)
        # Cette vidéo pourra vous aider pour la création de l'environnement virtuel virtualenv 
        mais expliquons pourquoi c'est important? C'est important pour tout ceux qui veulent manipuler la base de données
        Pour la configuration il faut:
            1- Ouvrez le terminal et utiliser la commande cd pour aller dans le répertoire dans lequel vous aviez cloner le dépôt par exemple si vous aviez cloner le dépôt dans /document alors faite un cd vers  /document
            2- Une fois là, exécutez la commande **pip install virtualenv**
            3- maintenant une fois installer vous aller créer un environnement virtuel la commande est **virtualenv nom_de_votre_environnement** assurez vous de remplacez **nom_de_votre_environement** par le nom que vous vouliez lui donnez ce n'est pas nécessaire que ça soit le même nom chez tout le monde 
            4- Maintenant il faut l'activer et pour ce faire il faut:
                # `Windows`: **nom_d'environnement/Script/activate**
                # `Linux` : **source nom_d'environnement/bon/activate**
            5- Ouvrez vscode à partir du terminal: **code .**
    - Utilisation de cette variable d'environnement:
        1- Maintenant une fois que vous avez activer ça vous aller vous déplacer dans le Projet (cd PIL1_2324_11)
        2- Installer maintenant les choses suivantes:
            `dotenv`: **pip install python-dotenv**
            `daphne`: **pip install daphne**
            `channels`: **pip install channels**
            `mysqlclient`: **pip install mysqlclient**
        3- N'oublier pas de créer la variable d'environnement (.env) [Uniquement ceux qui veulent manipulater la base de données, si tu es en front-end alors tu peux laisser]
            Euh pour ça bon j'ai déjà dis dans le groupe... (^_^)
            C'est le truc de DB_NAME etc
        4- Si vous rencontrer toujours des problèmes... (°˛°) Erivez-moi, ChatGPT, Copilot, youtube... (^^)
***`Deuxièmement mes modifs(now)`***
    - Base de données encore modifié, là où il y avait **managed=False**, mis aux oubliette;
    - `last_connect` devient `last_login`;
    - Pour que je puisse créer l'utilisateur, j'ai été contraint à mettre des contraintes pour certains champs de zz_users et de créer un nouveau `is_superuser`
    - Vous vérez toutes ces modifications dans le fichier `models.py` de l'application **commondatab**
    - 
    - Maintenant dans mon local j'ai été contraintes de recréer ma base de données pour que les modification apporter dans `models.py` migrent dans ma base de données.
    -
    - Inconvénients de cette modification, les champs qui étaient des énumération (enum) ne le sont plus, il sont devenus des VARCHAR... Répétez après  moi, ce n'est pas grave (^_^)
    
    - Si tu dois manipuler la base de données, tu seras probablement amené à recréer ta base locale...
    - Les pages de inscription /connexion ne sont pas encore tout à fait au point il manque encore un peu de vie et de formulaire mais tous ça va venir... enfin j'espère
***`Conclusion`***
    No conclusion  404
