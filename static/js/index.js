window.addEventListener("load", function () {
    const rechercheForm = document.getElementById('rechercheForm');
    const rechercheSelect = document.getElementById('rechercheSelect');

    const rechercheInput = document.getElementById('rechercheInput');
    const results = document.getElementById('results');

    rechercheForm.addEventListener('submit', chercherInstallationsParArrondissement);
    rechercheSelect.addEventListener('change', chercherInstallationsParNom);


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

    function chercherInstallationsParNom() {
        let value = rechercheSelect.value;
        if (value.length > 0) {
            fetch('/api/installations?nom=' + value).then(res => {
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
                    let table = createTable(installations[i], headers[i]);
                    results.append(table);
                }
            }
        } else {
            results.innerHTML = 'Aucun résultat trouvé';
        }
    }

    function createTable(installations, header) {
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
        });
        table.append(tbody)
        return divResponsive;
    }

    const headerGlissade = `<tr><th scope="col">Nom</th>
                            <th scope="col">Arrondissement</th>
                            <th scope="col">Ouvert</th>
                            <th scope="col">Déblayée</th>
                            <th scope="col">Condition</th>
                            <th scope="col">Mise à jour</th>
                            <th scope="col">Actions</th></tr>`;

    const headerPatinoire = `<tr><th scope="col">Nom</th>
                            <th scope="col">Arrondissement</th>
                            <th scope="col">Ouvert</th>
                            <th scope="col">Déblayée</th>
                            <th scope="col">Arrosée</th>
                            <th scope="col">Resurfacée</th>
                            <th scope="col">Mise à jour</th>
                            <th scope="col">Actions</th></tr>`;

    const headerPiscine = `<tr><th scope="col">Nom</th>
                       <th scope="col">Arrondissement</th>                           
                       <th scope="col">Id UEV</th>'
                       <th scope="col">Type de piscine</th>
                       <th scope="col">Adresse</th>
                       <th scope="col">Propriété</th>
                       <th scope="col">Gestion</th>
                       <th scope="col">Équipement</th>
                       <th scope="col">Point X</th>
                       <th scope="col">Point Y</th>
                       <th scope="col">Longitude</th>
                       <th scope="col">Latitude</th>
                       <th scope="col">Actions</th></tr>`;


    function createRow(inst) {
        let row = document.createElement('tr');
        updateRow(row, inst)
        return row;
    }

    function updateRow(row, inst) {
        row.setAttribute('data-object', JSON.stringify(inst))
        row.innerHTML = `<th>${inst.nom}</th>
                        <td>${inst.arrondissement}</td>`;
        if (inst.type === 'glissade') {
            row.innerHTML += `<td>${inst.ouvert}</td>
                            <td>${inst.deblaye}</td>
                            <td>${inst.condition}</td>
                            <td>${inst.mise_a_jour}</td>`;
        } else if (inst.type === 'patinoire') {
            row.innerHTML += `<td>${inst.ouvert}</td>
                            <td>${inst.deblaye}</td>
                            <td>${inst.arrose}</td>
                            <td>${inst.resurface}</td>
                            <td>${inst.mise_a_jour}</td>`;
        } else {
            row.innerHTML += `<td>${inst.id_uev}</td>
                         <td>${inst.type_piscine}</td>
                         <td>${inst.adresse}</td>
                         <td>${inst.propriete}</td>
                         <td>${inst.gestion}</td>
                         <td>${inst.equipement}</td>
                         <td>${inst.point_x}</td>
                         <td>${inst.point_y}</td>
                         <td>${inst.longitude}</td>
                         <td>${inst.latitude}</td>`;
        }
        const actions = document.createElement('td');
        actions.append(createButton('Modifier', 'btn btn-outline-success', modifierInstallation));
        actions.append(createButton('Supprimer', 'btn btn-outline-danger', supprimerInstallation));
        row.append(actions);
    }

    function createButton(texte, classeName, callback) {
        const button = document.createElement('button');
        button.className = classeName;
        button.innerText = texte;
        button.addEventListener('click', callback);
        return button;
    }

    function modifierInstallation(event) {
        const row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        row.innerHTML = `<th><input type="text" class="form-control" value="${inst.nom}"></th>
                        <td><input type="text" class="form-control" value="${inst.arrondissement}"></td>`;
        if (inst.type === 'glissade') {
            row.append(createSelectOuiNon(inst.ouvert));
            row.append(createSelectOuiNon(inst.deblaye));
            row.innerHTML += `<td><input type="text" class="form-control" value="${inst.condition}"></td>
                          <td><input type="datetime-local" class="form-control" value="${inst.mise_a_jour}"></td>`;
        } else if (inst.type === 'patinoire') {
            row.append(createSelectOuiNon(inst.ouvert));
            row.append(createSelectOuiNon(inst.deblaye));
            row.append(createSelectOuiNon(inst.arrose));
            row.append(createSelectOuiNon(inst.resurface));
            row.innerHTML += `<td><input type="datetime-local" class="form-control" value="${inst.mise_a_jour}"></td>`;
        } else {
            row.innerHTML += `<td><input type="text" class="form-control" value="${inst.id_uev}"></td>
                              <td><input type="text" class="form-control" value="${inst.type_piscine}"></td>
                              <td><input type="text" class="form-control" value="${inst.adresse}"></td>
                              <td><input type="text" class="form-control" value="${inst.propriete}"></td>
                              <td><input type="text" class="form-control" value="${inst.gestion}"></td>
                              <td><input type="text" class="form-control" value="${inst.equipement}"></td>
                              <td><input type="text" class="form-control" value="${inst.point_x}"></td>
                              <td><input type="text" class="form-control" value="${inst.point_y}"></td>
                              <td><input type="number" class="form-control" value="${inst.longitude}"></td>
                              <td><input type="number" class="form-control" value="${inst.latitude}"></td>`;
        }
        const actions = document.createElement('td');
        actions.append(createButton('Confirmer', 'btn btn-outline-info', sauverModification));
        actions.append(createButton('Annuler', 'btn btn-outline-secondary', annulerModification));
        row.append(actions);
        return row;
    }

    function supprimerInstallation(event) {
        const row = event.target.parentElement.parentElement;
        console.log(row)
    }

    function sauverModification(event) {
        let row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        cells = row.children;
        inst.nom = cells[0].firstChild.value;
        inst.arrondissement = cells[1].firstChild.value;
        if (inst.type === 'glissade') {
            inst.ouvert = JSON.parse(cells[2].firstChild.value);
            inst.deblaye = JSON.parse(cells[3].firstChild.value);
            inst.condition = cells[4].firstChild.value;
            inst.mise_a_jour = cells[5].firstChild.value;
        } else if (inst.type === 'patinoire') {
            inst.ouvert = JSON.parse(cells[2].firstChild.value);
            inst.deblaye = JSON.parse(cells[3].firstChild.value);
            inst.arrose = JSON.parse(cells[4].firstChild.value);
            inst.resurface = JSON.parse(cells[5].firstChild.value);
            inst.mise_a_jour = cells[6].firstChild.value;
        } else {
            inst.id_uev = cells[2].firstChild.value;
            inst.type_piscine = cells[3].firstChild.value;
            inst.adresse = cells[4].firstChild.value;
            inst.propriete = cells[5].firstChild.value;
            inst.gestion = cells[6].firstChild.value;
            inst.equipement = cells[7].firstChild.value;
            inst.point_x = cells[8].firstChild.value;
            inst.point_y = cells[9].firstChild.value;
            inst.longitude = cells[10].firstChild.value;
            inst.latitude = cells[11].firstChild.value;
        }
        const inst_api = Object.assign({}, inst);
        delete inst_api.id;
        delete inst_api.type;
        fetch(`/api/${inst.type}/${inst.id}`, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inst_api)
        }).then(res => {
            if (res.status === 200) {
                row.innerHTML = '';
                updateRow(row, inst);
            }
            throw Error
        }).catch(e => {
            console.log('Erreur: ', e);
        });
    }

    function annulerModification(event) {
        const row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        row.innerHTML = '';
        updateRow(row, inst);
    }

    function createSelectOuiNon(value) {
        const td = document.createElement('td');
        td.innerHTML = `<select class="form-control" >
                          <option value="null" ${value === null ? "selected" : ""}  >Sans objet</option>
                          <option value="true" ${value === true ? "selected" : ""} >Oui</option>
                          <option value="false" ${value === false ? "selected" : ""} >Non</option>
                        </select>`;
        return td;
    }


    function setError(formControl, errorMessage) {
        const errorSpan = formControl.parentElement.querySelector('.error');
        errorSpan.style.visibility = 'visible'
        errorSpan.innerHTML = errorMessage
        formControl.className = 'form-control is-invalid'
    }

    function chargerListeInstallations() {
        fetch('/api/liste-installations').then(res => {
            if (res.status === 200) {
                return res.json();
            }
            throw Error
        }).then(installations => {
            installations.forEach(inst => {
                const option = document.createElement('option');
                option.setAttribute('value', inst);
                option.innerText = inst;
                rechercheSelect.append(option);
            });
        }).catch(e => {
            console.log('Erreur: ', e);
        })
    }

    chargerListeInstallations();
});

