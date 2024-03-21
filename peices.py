from peice_class import peice

peices = []







peices.append(peice('Still Life with a Ginger Jar and Eggplants', 'Paul Cézanne', '1893-94'))
peices.append(peice('New York City Ⅰ', 'Piet Mondrian', '1942'))
peices.append(peice('Girl Before a Mirror', 'Pablo Picasso', '1932'))
peices.append(peice('Oath of the Horatii', 'Jacques-Louis David', '1784'))
peices.append(peice('Watson and the Shark', 'John Singleton Copley', '1778'))
peices.append(peice('La Grande Odalisque', 'Jean Auguste Dominique Ingres', '1814'))
peices.append(peice('La Comtesse d\'Haussonville', 'Jean Auguste Dominique Ingres', '1845'))
peices.append(peice('The Raft of the Medusa', 'Théodore Géricault', '1818-19'))
peices.append(peice('Liberty Leading the People', 'Eugène Delacroix', '1830'))
peices.append(peice('Still Life with a Lobster', 'Eugène Delacroix', '1827'))
peices.append(peice('The Stone Breakers', 'Gustave Courbet', '1849'))
peices.append(peice('The Third-Class Carriage', 'Honoré Daumier', '1862'))
peices.append(peice('Galloping Horse', 'Eadweard Muybridge', '1878'))
peices.append(peice('Déjeuner sur L\'Herbe (Luncheon on the Grass)', 'Édouard Manet', '1863'))
peices.append(peice('Impression- Sunrise', 'Claude Monet', '1872'))
peices.append(peice('Rouen Cathedral', 'Claude Monet', '1894'))
#peices.append(peice('', '', ''))
peices.append(peice('The Glass of Absinth', 'Edgar Dégas', '1876'))
peices.append(peice('The Little 14-year-old Dancer', 'Edgar Dégas', '1878-81'))
peices.append(peice('Le Moulin de la Galette', 'Pierre Auguste Renoir', '1876'))
peices.append(peice('Girl with a Watering Can', 'Pierre Auguste Renoir', '1876'))


for peice in peices:
    print(peice.year)