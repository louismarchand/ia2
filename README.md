# ia2
ia2_tassadit

<h1>Projet IA2</h1>

    <h2>Automate de reconnaissance</h2>
    
        <p>Reconnaissance de requete et interrogation de base de données.</p>
        <p>librairies requises :</p>
            <li>sqlite 3.11.0</li>
            <li>python 3.5</li>
        </br>    
        <div>
            <p>Il vous faut également : </p>
            <li>Gourdon, Charly</li>
            <li>Deramaix, Jonathan</li>
            <li>Marchand, Louis</li>
        </div>


<h3>Reste à faire</h3>
<p>Pour faire en sorte que les Questions 8 et 9 fonctionnent:</p>
    <li>ajouter au verbes la notion de (objet du verbe et sujet du verbe)</li>
        <p><br/>exemple : preparent:diplome;table1!prenom,nom;table1
            <br/>car on prépare un diplome (l'objet) et c'est prenom,nom (le sujet) qui prépare
     ainsi à l'étape 5 de l'automate on peut determiner si le nom de rubrique qu'on lit doit nous renseigner sur le sujet ou l'objet du precedent verbe
     ainsi à l'étape 3 de l'automate on sait si l'on doit utiliser le sujet du verbe ou pas selon le PI précédent
        </p>

    <li>Et donc ajouter la notion de sujet/objet aux PI</li>
