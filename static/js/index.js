const rechercheForm = document.getElementById('rechercheForm');
const rechercheInput = document.getElementById('rechercheInput');
const results = document.getElementById('results');

rechercheForm.addEventListener('submit', chercherInstallationsParArrondissement);

function chercherInstallationsParArrondissement(event) {
    event.preventDefault();
    let value = rechercheInput.value.trim();
    if (value.length == 0) {
        setError(rechercheInput, "Ce champ est requis.");
    } else {
        fetch('/api/installations?arrondissement=' + value).then(res => {
            if (res.status === 200) {
                return res.json();
            }
            throw Error
        }).then(installations => {
            displayResults(installations);
        }).catch(e => {
            console.log('Erreur: ', e);
        })
    }
}

function displayResults(resultat) {
    const types = ['glissade', 'patinoire', 'piscine'];
    const headers = [headerGlissade, headerPatinoire, headerPiscine];
    const rows = [createRowGlissade, createRowPatinoire, createRowPiscine];

    results.innerHTML = '';
    if (resultat.length > 0) {
        const installations = []
        for (t of types) {
            installations.push(resultat.filter((inst) => inst.type === t));
        }
        for (let i = 0; i < installations.length; ++i) {
            if (installations[i].length > 0) {
                let title = document.createElement('h2');
                title.innerText = 'Les ' + types[i] + 's';
                results.append(title);
                let table = createTable(installations[i], headers[i], rows[i]);
                results.append(table);
            }
        }
    } else {
        results.innerHTML = 'Aucun résultat trouvé';
    }
}

function createTable(installations, header, createRow) {
    const divResponsive = document.createElement('div');
    divResponsive.className = 'table-responsive';
    let table = document.createElement("table");
    table.className = "table table-hover";
    divResponsive.append(table);
    let thead = document.createElement("thead");
    thead.innerHTML = header;
    table.append(thead);
    let tbody = document.createElement('tbody');
    installations.forEach(inst => {
        let row = createRow(inst);
        tbody.append(row);
    })
    table.append(tbody)
    return divResponsive;
}

const headerGlissade = '<tr><th scope="col">#</th>'
    + '<th scope="col">Nom</th>'
    + '<th scope="col">Arrondissement</th>'
    + '<th scope="col">Ouvert</th>'
    + '<th scope="col">Déblayée</th>'
    + '<th scope="col">Condition</th>'
    + '<th scope="col">Mise à jour</th>'
    + '<th scope="col">Actions</th></tr>';

function createRowGlissade(installation) {
    let row = document.createElement('tr');
    row.innerHTML = '<th scope="row">' + installation.id
        + '</th><td>' + installation.nom
        + '</td><td>' + installation.arrondissement
        + '</td><td>' + installation.ouvert
        + '</td><td>' + installation.deblaye
        + '</td><td>' + installation.condition
        + '</td><td>' + installation.mise_a_jour
        + '</td><td>modifier supprimer</td>'
    return row;
}

const headerPatinoire = '<tr><th scope="col">#</th>'
    + '<th scope="col">Nom</th>'
    + '<th scope="col">Arrondissement</th>'
    + '<th scope="col">Ouvert</th>'
    + '<th scope="col">Déblayée</th>'
    + '<th scope="col">Arrosée</th>'
    + '<th scope="col">Resurfacée</th>'
    + '<th scope="col">Mise à jour</th>'
    + '<th scope="col">Actions</th></tr>';

function createRowPatinoire(installation) {
    let row = document.createElement('tr');
    row.innerHTML = '<th scope="row">' + installation.id
        + '</th><td>' + installation.nom
        + '</td><td>' + installation.arrondissement
        + '</td><td>' + installation.ouvert
        + '</td><td>' + installation.deblaye
        + '</td><td>' + installation.arrose
        + '</td><td>' + installation.resurface
        + '</td><td>' + installation.mise_a_jour
        + '</td><td>modifier supprimer</td>'
    return row;
}

const headerPiscine = '<tr><th scope="col">#</th>'
    + '<th scope="col">Nom</th>'
    + '<th scope="col">Arrondissement</th>'
    + '<th scope="col">Id UEV</th>'
    + '<th scope="col">Type de piscine</th>'
    + '<th scope="col">Adresse</th>'
    + '<th scope="col">Propriété</th>'
    + '<th scope="col">Gestion</th>'
    + '<th scope="col">Équipement</th>'
    + '<th scope="col">Point X</th>'
    + '<th scope="col">Point Y</th>'
    + '<th scope="col">Longitude</th>'
    + '<th scope="col">Latitude</th>'
    + '<th scope="col">Actions</th></tr>';

function createRowPiscine(installation) {
    let row = document.createElement('tr');
    row.innerHTML = '<th scope="row">' + installation.id
        + '</th><td>' + installation.nom
        + '</td><td>' + installation.arrondissement
        + '</td><td>' + installation.id_uev
        + '</td><td>' + installation.type_piscine
        + '</td><td>' + installation.adresse
        + '</td><td>' + installation.propriete
        + '</td><td>' + installation.gestion
        + '</td><td>' + installation.equipement
        + '</td><td>' + installation.point_x
        + '</td><td>' + installation.point_y
        + '</td><td>' + installation.longitude
        + '</td><td>' + installation.latitude
        + '</td><td>modifier supprimer</td>'
    return row;
}

function setError(formControl, errorMessage) {
    const errorSpan = formControl.parentElement.querySelector('.error');
    errorSpan.style.visibility = 'visible'
    errorSpan.innerHTML = errorMessage
    formControl.className = 'form-control is-invalid'
}

