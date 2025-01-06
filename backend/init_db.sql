-- Insérer des administrateurs
INSERT INTO admins (username, firstname, lastname, hashed_password) VALUES
    ('seny_toutou', 'Seny', 'Toutou', 'hashed_password1'),
    ('ali_marco', 'Ali', 'Marco', 'hashed_password2')
ON CONFLICT (username) DO NOTHING;

-- Insérer des groupes
INSERT INTO groups (group_name, admin_info) VALUES
    ('Electroménager', 'seny_toutou'),
    ('Cuisine', 'ali_marco')
ON CONFLICT (group_name) DO NOTHING;

-- Insérer des utilisateurs
INSERT INTO users (username, firstname, lastname, hashed_password, group_id, admin_info) VALUES
    -- Liste des utilisateurs
    ('abdou_ndiaye', 'Abdou', 'Ndiaye', 'hashed_password3', 1, 'seny_toutou'),
    ('awa_diop', 'Awa', 'Diop', 'hashed_password4', 1, 'seny_toutou'),
    ('cheikh_sow', 'Cheikh', 'Sow', 'hashed_password5', 1, 'seny_toutou'),
    ('fatou_faye', 'Fatou', 'Faye', 'hashed_password6', 1, 'seny_toutou'),
    ('mamadou_ndour', 'Mamadou', 'Ndour', 'hashed_password7', 1, 'seny_toutou'),
    ('aminata_sarr', 'Aminata', 'Sarr', 'hashed_password8', 1, 'seny_toutou'),
    ('serigne_kane', 'Serigne', 'Kane', 'hashed_password9', 1, 'seny_toutou'),
    ('khady_ba', 'Khady', 'Ba', 'hashed_password10', 1, 'seny_toutou'),
    ('ibrahima_diallo', 'Ibrahima', 'Diallo', 'hashed_password11', 2, 'ali_marco'),
    ('sokhna_fall', 'Sokhna', 'Fall', 'hashed_password12', 2, 'ali_marco'),
    ('modou_gaye', 'Modou', 'Gaye', 'hashed_password13', 2, 'ali_marco'),
    ('coumba_sy', 'Coumba', 'Sy', 'hashed_password14', 2, 'ali_marco'),
    ('ousmane_diagne', 'Ousmane', 'Diagne', 'hashed_password15', 2, 'ali_marco'),
    ('mariama_toure', 'Mariama', 'Touré', 'hashed_password16', 2, 'ali_marco'),
    ('babacar_seck', 'Babacar', 'Seck', 'hashed_password17', 2, 'ali_marco'),
    ('diarra_gueye', 'Diarra', 'Gueye', 'hashed_password18', 2, 'ali_marco'),
    ('malick_camara', 'Malick', 'Camara', 'hashed_password19', 2, 'ali_marco'),
    ('bineta_cisse', 'Bineta', 'Cissé', 'hashed_password20', 2, 'ali_marco'),
    ('seydou_thiam', 'Seydou', 'Thiam', 'hashed_password21', 2, 'ali_marco'),
    ('adama_mbaye', 'Adama', 'Mbaye', 'hashed_password22', 2, 'ali_marco')
ON CONFLICT (username) DO NOTHING;

-- Insérer des prompts
INSERT INTO prompts (prompt_content, price, note, status, user_info) VALUES
    -- Thème électroménager
    ('Quel est le meilleur réfrigérateur adapté aux conditions climatiques du Sénégal ?', 1500, 10, 'active', 'abdou_ndiaye'),
    ('Quelle est la consommation énergétique des climatiseurs en milieu rural ?', 1200, 8, 'active', 'awa_diop'),
    ('Les congélateurs solaires sont-ils adaptés pour les zones non connectées ?', 1700, 9, 'active', 'cheikh_sow'),
    ('Quel type de cuisinière convient le mieux pour la cuisson au bois ?', 1300, 7, 'review', 'fatou_faye'),
    ('Comparaison des prix des lave-linges à Dakar', 2000, 10, 'active', 'mamadou_ndour'),
    ('Quels sont les mixeurs les plus populaires pour préparer des jus sénégalais ?', 1100, 8, 'review', 'aminata_sarr'),
    ('Guide d’achat des ventilateurs robustes pour les régions chaudes', 1400, 9, 'active', 'serigne_kane'),
    ('Les friteuses modernes sont-elles adaptées à la cuisine sénégalaise ?', 1600, 8, 'pending', 'khady_ba'),
    ('Les micro-ondes consomment-ils beaucoup d’énergie au Sénégal ?', 1000, 7, 'review', 'ibrahima_diallo'),
    ('Comparaison entre les cuisinières à gaz et électriques pour la Thiéboudiène', 1800, 9, 'active', 'sokhna_fall'),

    -- Thème cuisine sénégalaise
    ('Quelle est la recette originale du Yassa Poulet ?', 800, 10, 'active', 'modou_gaye'),
    ('Comment préparer un bon Caldou à base de poisson local ?', 750, 9, 'active', 'coumba_sy'),
    ('Astuces pour cuisiner un Thiéboudiène royal comme à Saint-Louis', 900, 8, 'pending', 'ousmane_diagne'),
    ('Quels sont les secrets de la sauce Kaldou ?', 700, 7, 'review', 'mariama_toure'),
    ('Les meilleures épices pour la préparation du Domoda', 1000, 8, 'review', 'babacar_seck'),
    ('Comment cuisiner du Mbaxal de mil avec du poisson séché ?', 1200, 10, 'active', 'diarra_gueye'),
    ('Les ustensiles traditionnels pour cuisiner le Lakh au Sénégal', 600, 6, 'active', 'malick_camara'),
    ('Recette du Ngalakh pour les fêtes traditionnelles', 850, 9, 'active', 'bineta_cisse'),
    ('Comment faire un Sombi onctueux à base de riz cassé ?', 700, 8, 'review', 'seydou_thiam'),
    ('Le secret des beignets sénégalais moelleux', 950, 9, 'active', 'adama_mbaye'),

    -- Thème électroménager
    ('Quel est le meilleur rapport qualité-prix pour un réfrigérateur à Dakar ?', 1500, 8, 'active', 'khady_ba'),
    ('Les climatiseurs avec option éco sont-ils efficaces dans les zones urbaines ?', 1800, 9, 'active', 'mamadou_ndour'),
    ('Existe-t-il des générateurs solaires pour alimenter les machines à laver ?', 2000, 10, 'active', 'aminata_sarr'),
    ('Les congélateurs à faible consommation sont-ils disponibles au Sénégal ?', 1700, 9, 'pending', 'serigne_kane'),
    ('Quelle marque de mixeur est recommandée pour le bissap et le jus de bouye ?', 1300, 8, 'review', 'cheikh_sow'),
    ('Comment choisir un bon presse-agrumes pour les oranges locales ?', 1200, 8, 'review', 'awa_diop'),
    ('Les machines à café sont-elles adaptées aux habitudes sénégalaises ?', 1000, 7, 'review', 'fatou_faye'),
    ('Quels sont les meilleurs aspirateurs pour les maisons sablonneuses ?', 1900, 9, 'active', 'abdou_ndiaye'),
    ('Les cuisinières portables au gaz sont-elles fiables ?', 1400, 8, 'review', 'ibrahima_diallo'),
    ('Comment choisir une télévision adaptée aux zones rurales ?', 2100, 10, 'active', 'modou_gaye'),
    ('Les fers à repasser modernes consomment-ils moins d’électricité ?', 800, 8, 'pending', 'coumba_sy'),
    ('Les machines à coudre électriques sont-elles populaires au Sénégal ?', 1100, 8, 'active', 'ousmane_diagne'),
    ('Existe-t-il des réchauds économiques pour les petits commerces ?', 1500, 9, 'review', 'mariama_toure'),
    ('Quel lave-vaisselle convient pour une famille nombreuse ?', 2300, 10, 'active', 'babacar_seck'),
    ('Les bouilloires électriques sont-elles adaptées pour les zones hors réseau ?', 950, 7, 'review', 'diarra_gueye'),
    ('Guide d’achat des mini-réfrigérateurs pour chambres étudiantes', 1700, 9, 'active', 'malick_camara'),
    ('Les ampoules LED sont-elles plus durables au Sénégal ?', 700, 6, 'pending', 'bineta_cisse'),
    ('Les micro-ondes sont-ils nécessaires pour la cuisine moderne ?', 1200, 8, 'active', 'seydou_thiam'),
    ('Les réchauds à pétrole sont-ils encore utilisés ?', 600, 5, 'review', 'adama_mbaye'),
    ('Quel blender choisir pour les noix de cajou ?', 1600, 9, 'active', 'khady_ba'),

    -- Thème cuisine
    ('Comment réussir un bon Mbaxal de niébé ?', 950, 9, 'active', 'abdou_ndiaye'),
    ('Recette facile pour préparer un Thiéré au poisson fumé', 800, 8, 'pending', 'awa_diop'),
    ('Comment conserver le nététou pour la cuisine sénégalaise ?', 700, 7, 'review', 'cheikh_sow'),
    ('Quelles sont les étapes pour préparer le Sombi au lait de coco ?', 850, 9, 'active', 'fatou_faye'),
    ('Les meilleures techniques pour un bon Ceebu Yapp', 1000, 8, 'active', 'mamadou_ndour'),
    ('Comment faire un Ngalakh parfait pour le Ramadan ?', 750, 9, 'review', 'aminata_sarr'),
    ('Quelle est la méthode traditionnelle pour préparer le Yassa poisson ?', 1200, 10, 'active', 'serigne_kane'),
    ('Les secrets d’un bon Domoda au bœuf', 1100, 8, 'review', 'ibrahima_diallo'),
    ('Comment cuisiner un bon Mbaxal sans huile ?', 650, 6, 'pending', 'sokhna_fall'),
    ('Recette facile pour le Mafé au poulet', 900, 8, 'active', 'modou_gaye'),
    ('Quelles sont les variétés de riz les plus utilisées au Sénégal ?', 800, 7, 'review', 'coumba_sy'),
    ('Comment réussir des beignets de mil croustillants ?', 700, 9, 'active', 'ousmane_diagne'),
    ('Les astuces pour un bon Thiéboudiène rouge', 950, 10, 'active', 'mariama_toure'),
    ('Comment faire une sauce gombo sans grumeaux ?', 750, 8, 'pending', 'babacar_seck'),
    ('Recette de la soupe Kandia', 700, 7, 'review', 'diarra_gueye'),
    ('Comment mariner le poisson pour un bon Yassa ?', 600, 8, 'active', 'malick_camara'),
    ('Quelles épices utiliser pour un Caldou mémorable ?', 800, 9, 'active', 'bineta_cisse'),
    ('Comment préparer une bonne sauce tomate sénégalaise ?', 900, 8, 'pending', 'seydou_thiam'),
    ('Recette du Lakh avec du lait caillé', 700, 7, 'review', 'adama_mbaye'),
    ('Les étapes pour un Thiéboudiène blanc parfait', 850, 10, 'active', 'khady_ba');